from flask import Flask, render_template, jsonify, request
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
SETTINGS_FILE = DATA_DIR / "settings.json"
TASKS_FILE = DATA_DIR / "tasks.json"
ACTIVITY_FILE = DATA_DIR / "activity.json"

DEFAULT_SETTINGS = {
    "mode": "assisted",
    "permissions": {
        "search_research": True,
        "generate_hypotheses": True,
        "run_approved_simulations": True,
        "start_new_projects": False,
        "autonomous_research": False,
        "publish_or_submit": False,
        "spend_money": False,
        "physical_experiments": False
    }
}

def load_settings():
    if not SETTINGS_FILE.exists():
        save_settings(DEFAULT_SETTINGS)
    try:
        return json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return DEFAULT_SETTINGS.copy()

def save_settings(settings):
    SETTINGS_FILE.write_text(json.dumps(settings, indent=2), encoding="utf-8")

def read_json(path, fallback):
    if not path.exists():
        path.write_text(json.dumps(fallback, indent=2), encoding="utf-8")
        return fallback
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return fallback

def write_json(path, value):
    path.write_text(json.dumps(value, indent=2), encoding="utf-8")

app = Flask(__name__)

PAGES = [
    ("anatomy", "Human Anatomy Explorer", "Explore anatomical structures and connected systems."),
    ("brain", "Brain & Neuroscience", "Explore brain regions, neurons, synapses, and virtual networks."),
    ("circuits", "AI Circuit Laboratory", "Design and simulate educational, non-invasive electronic circuits."),
    ("biology", "Biological Modeling", "Explore atoms, molecules, proteins, DNA, cells, and tissues."),
    ("signals", "Signal Analysis", "Inspect, record, and compare simulated signals."),
    ("experiments", "Experiment Laboratory", "Build experiments and collaborate in shared workspaces."),
    ("library", "Research Library", "Organize scientific sources, papers, notes, and citations."),
    ("results", "Results Center", "Review experiments and prepare carefully qualified reports."),
    ("discovery", "Theoretical Physics & Discovery", "Develop and evaluate hypotheses and mathematical models."),
    ("command", "AI Command Center", "Talk to the assistant and manage project settings and permissions.")
]

@app.route("/")
def home():
    return render_template("index.html", pages=PAGES, settings=load_settings())

@app.route("/page/<slug>")
def page(slug):
    selected = next((p for p in PAGES if p[0] == slug), None)
    if selected is None:
        return "Page not found", 404
    return render_template("page.html", page=selected, pages=PAGES, settings=load_settings(), tasks=read_json(TASKS_FILE, []), activity=read_json(ACTIVITY_FILE, []))

@app.get("/api/settings")
def get_settings():
    return jsonify(load_settings())

@app.post("/api/settings")
def update_settings():
    incoming = request.get_json(silent=True) or {}
    current = load_settings()
    if "mode" in incoming and incoming["mode"] in ("manual", "assisted", "autonomous"):
        current["mode"] = incoming["mode"]
    if isinstance(incoming.get("permissions"), dict):
        for key, value in incoming["permissions"].items():
            if key in current["permissions"] and isinstance(value, bool):
                current["permissions"][key] = value
    # High-impact actions remain disabled in this starter; enabling them requires
    # a separately designed approval and safety workflow.
    for key in ("publish_or_submit", "spend_money", "physical_experiments"):
        current["permissions"][key] = False
    save_settings(current)
    return jsonify(current)

@app.get("/api/tasks")
def get_tasks():
    return jsonify(read_json(TASKS_FILE, []))

@app.post("/api/tasks")
def add_task():
    incoming = request.get_json(silent=True) or {}
    title = str(incoming.get("title", "")).strip()[:120]
    details = str(incoming.get("details", "")).strip()[:2000]
    if not title:
        return jsonify({"error": "A task title is required."}), 400
    tasks = read_json(TASKS_FILE, [])
    task = {"id": len(tasks) + 1, "title": title, "details": details,
            "status": "queued_locally", "execution": "not_connected",
            "note": "Saved locally; no AI worker is connected yet."}
    tasks.insert(0, task)
    write_json(TASKS_FILE, tasks)
    activity = read_json(ACTIVITY_FILE, [])
    activity.insert(0, {"type": "Task queued", "message": title,
                        "status": "Waiting for a connected development agent."})
    write_json(ACTIVITY_FILE, activity[:100])
    return jsonify(task), 201

@app.get("/api/project-status")
def project_status():
    state = read_json(DATA_DIR / "project_state.json", {})
    return jsonify({"cloud_deployment": state.get("cloud_deployment", "not_deployed"),
                    "development_ai": state.get("agents", {}).get("cloud_development_ai", {}).get("status", "unknown"),
                    "research_ai": state.get("agents", {}).get("research_ai", {}).get("status", "unknown"),
                    "budget": "strictly $0 — no automatic spending"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
