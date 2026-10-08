# Doruk Village

Doruk Village is an autonomous multi-agent development environment for Godot 4 game projects.

## What is included

- Python backend with FastAPI
- Real orchestrator, task queue, and benchmark logging
- Agent definitions and persistent memory
- NVIDIA NIM provider using the OpenAI-compatible endpoint
- Secure sandboxed tool layer for file, command, and git operations
- Dark moderator dashboard
- Demo Godot 4 football arena project under `workspace/game`

## Environment variables

- `NVIDIA_API_KEY`
- `NVIDIA_MODEL`

## Quick start

1. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Copy environment values:

   ```bash
   cp .env.example .env
   ```

3. Start the village:

   ```bash
   ./start.sh
   ```

4. Open the dashboard:

   http://localhost:8000/

5. Optionally trigger the demo project via the API:

   ```bash
   curl -X POST http://localhost:8000/api/demo/start
   ```

## Structure

```text
.
├── agents/
├── backend/
├── benchmarks/
├── frontend/
├── logs/
├── tasks/
├── tests/
├── workspace/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── pytest.ini
├── start.sh
└── ...
```

## Notes

The NVIDIA provider uses `https://integrate.api.nvidia.com/v1` with a bearer token from `NVIDIA_API_KEY` and a model from `NVIDIA_MODEL`.
