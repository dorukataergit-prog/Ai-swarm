from pathlib import Path


def ensure_project_dirs() -> None:
    for p in [
        Path("workspace"),
        Path("workspace/game"),
        Path("workspace/game/scenes"),
        Path("workspace/game/scripts"),
        Path("agents"),
        Path("logs"),
        Path("tasks"),
        Path("benchmarks"),
    ]:
        p.mkdir(parents=True, exist_ok=True)
