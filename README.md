# NerveGear Lab — Starter Foundation

This is the first software foundation for the NerveGear Lab project. It is a local-first browser application scaffold, not the completed scientific simulator.

## Included
- Local Flask web server
- Ten-page navigation scaffold
- AI Command Center with local development task queue and connection status
- Central settings and permission model
- Research/experiment data folders
- Clear placeholders for validated scientific and circuit simulation engines

## Requirements
- Python 3.10+
- Windows, macOS, or Linux

## Run on Windows
1. Extract this folder.
2. Open PowerShell in this folder.
3. Run: `py -m venv .venv`
4. Run: `.venv\\Scripts\\Activate.ps1`
5. Run: `py -m pip install -r requirements.txt`
6. Run: `py app.py`
7. Open `http://127.0.0.1:5000` in your browser.

If PowerShell blocks activation, you can run `.venv\\Scripts\\python.exe -m pip install -r requirements.txt`, then `.venv\\Scripts\\python.exe app.py`.

## Important
The pages are currently navigation and interface scaffolds. They do not yet contain validated 3D anatomy, neural, molecular, circuit, or physics simulators. Those will be added as separate tested modules. The AI permissions default to conservative settings; no autonomous external actions are enabled.

## NerveGear Lab development blueprint
Read `BLUEPRINT.md` for the full agreed product plan and `MILESTONE_1.md` for the first infrastructure milestone. The current app is a starter scaffold, not a connected cloud AI. The cloud development agent and research AI are not yet deployed or connected. Tasks entered in Page 10 are saved locally only; they are not executed until a real cloud worker and model are configured. The current project does not send data to an external service.

## Project status
See `data/project_state.json`. Keep this file updated as real integrations are completed. Never mark a cloud service as connected until it has been deployed and verified.
