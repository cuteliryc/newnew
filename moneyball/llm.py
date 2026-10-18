"""Вызов LLM. По умолчанию — GPT через Codex CLI с входом по аккаунту ChatGPT.

Чтобы подключить другой сервис, добавьте функцию в BACKENDS.
"""

import json
import os
import shutil
import subprocess
import tempfile
import urllib.request
from pathlib import Path


class LLMError(RuntimeError):
    pass


def _codex(prompt, cfg, images=()):
    binary = cfg.get("codex_bin", "codex")
    if not shutil.which(binary):
        raise LLMError(
            "Codex CLI не найден. Установите: npm i -g @openai/codex, затем войдите: codex login"
        )
    status = subprocess.run([binary, "login", "status"], capture_output=True, text=True)
    if "not logged in" in (status.stdout + status.stderr).lower():
        raise LLMError("Нет входа в ChatGPT. Выполните `codex login` — откроется браузер.")
    with tempfile.TemporaryDirectory() as tmp:
        out_file = Path(tmp) / "answer.md"
        # Агенту не нужны команды и файлы: только текст на входе и текст на выходе.
        cmd = [
            binary, "exec", "-",
            "--sandbox", "read-only",
            "--skip-git-repo-check",
            "--ephemeral",
            "--color", "never",
            "-C", tmp,
            "-o", str(out_file),
        ]
        if cfg.get("model"):
            cmd += ["-m", cfg["model"]]
        for image in images:
            cmd += ["-i", str(image)]
        try:
            proc = subprocess.run(
                cmd, input=prompt, capture_output=True, text=True,
                timeout=cfg.get("timeout_sec", 600),
            )
        except subprocess.TimeoutExpired as exc:
            raise LLMError("Codex не ответил за отведённое время") from exc
        if proc.returncode != 0:
            tail = (proc.stderr or proc.stdout or "").strip()[-1500:]
            if "login" in tail.lower() or "auth" in tail.lower():
                tail += "\n\nПохоже, нужен вход: выполните `codex login`."
            raise LLMError(f"Codex завершился с ошибкой:\n{tail}")
        if out_file.exists() and out_file.read_text(encoding="utf-8").strip():
            return out_file.read_text(encoding="utf-8")
        return proc.stdout


def _openai_api(prompt, cfg, images=()):
    key = os.environ.get(cfg.get("api_key_env", "OPENAI_API_KEY"))
    if not key:
        raise LLMError(f"Нет ключа в переменной {cfg.get('api_key_env')}")
    if not cfg.get("model"):
        raise LLMError("Для backend=openai_api укажите llm.model в config.json")
    if images:
        raise LLMError("Картинки поддерживаются только в backend=codex")
    body = {
        "model": cfg["model"],
        "messages": [{"role": "user", "content": prompt}],
        "temperature": cfg.get("temperature", 0.3),
        "max_tokens": cfg.get("max_tokens", 2500),
    }
    req = urllib.request.Request(
        cfg["base_url"].rstrip("/") + "/chat/completions",
        data=json.dumps(body).encode("utf-8"),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=cfg.get("timeout_sec", 600)) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as exc:  # сеть, 4xx/5xx
        raise LLMError(f"Запрос к API не удался: {exc}") from exc
    return data["choices"][0]["message"]["content"]


BACKENDS = {"codex": _codex, "openai_api": _openai_api}


def complete(prompt, llm_cfg, images=(), backend=None, model=None):
    cfg = dict(llm_cfg)
    if model:
        cfg["model"] = model
    name = backend or cfg.get("backend", "codex")
    if name not in BACKENDS:
        raise LLMError(f"Неизвестный backend: {name}. Есть: {', '.join(BACKENDS)}")
    return BACKENDS[name](prompt, cfg, images)


def login_status(llm_cfg):
    binary = llm_cfg.get("codex_bin", "codex")
    if not shutil.which(binary):
        return "Codex CLI не установлен (npm i -g @openai/codex)"
    proc = subprocess.run([binary, "login", "status"], capture_output=True, text=True)
    return (proc.stdout + proc.stderr).strip()
