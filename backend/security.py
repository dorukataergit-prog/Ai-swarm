import os
import shlex

from backend.config import WORKSPACE_DIR

BLOCK_PATTERNS = [
    "rm -rf /",
    "sudo ",
    "chmod -R",
    "chown",
    "curl ",
    "wget ",
    "nc ",
    "ncat ",
    "ssh ",
    "scp ",
    "openssl enc",
    "/etc/passwd",
    "/proc/",
    "LD_PRELOAD",
    "export ",
    "unset ",
    "env ",
]


class SafePathPolicy:
    @staticmethod
    def validate(path: str):
        from pathlib import Path

        candidate = Path(path)
        if candidate.is_absolute():
            root = str(WORKSPACE_DIR.resolve())
            if not str(candidate.resolve()).startswith(root):
                raise ValueError(f"Access outside workspace is blocked: {path}")
            return candidate.resolve()

        resolved = (WORKSPACE_DIR / candidate).resolve()
        if not str(resolved).startswith(str(WORKSPACE_DIR.resolve())):
            raise ValueError(f"Access outside workspace is blocked: {path}")
        return resolved


class CommandPolicy:
    @staticmethod
    def validate(command: str):
        if not command or not command.strip():
            raise ValueError("Empty command is not allowed.")
        lowered = command.lower()
        for pattern in BLOCK_PATTERNS:
            if pattern in lowered:
                raise ValueError(f"Blocked command pattern: {pattern}")

    @staticmethod
    def safe_tokens(command: str):
        CommandPolicy.validate(command)
        return shlex.split(command)


class SecretGuard:
    @staticmethod
    def read_environment(name: str):
        if name not in {"NVIDIA_API_KEY", "NVIDIA_MODEL", "PYTHONPATH", "PATH"}:
            raise PermissionError(f"Reading environment variable '{name}' is blocked.")
        return os.getenv(name)
