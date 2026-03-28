#!/usr/bin/env python3
"""Resolve ${ENV_VAR} placeholders in config.json and start nanobot gateway."""
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config.json"
PLACEHOLDER_PATTERN = re.compile(r"\$\{([A-Z0-9_]+)\}")


def resolve_placeholders(value):
    if isinstance(value, dict):
        return {k: resolve_placeholders(v) for k, v in value.items()}
    if isinstance(value, list):
        return [resolve_placeholders(v) for v in value]
    if isinstance(value, str):
        return PLACEHOLDER_PATTERN.sub(lambda m: os.getenv(m.group(1), ""), value)
    return value


def main() -> int:
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        config = json.load(f)

    config = resolve_placeholders(config)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", encoding="utf-8", delete=False
    ) as tmp:
        json.dump(config, tmp, indent=2)
        tmp_path = tmp.name

    try:
        port = os.getenv("PORT", "8080")
        cmd = ["nanobot", "gateway", "--config", tmp_path, "--port", port]
        completed = subprocess.run(cmd)
        return completed.returncode
    finally:
        Path(tmp_path).unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
