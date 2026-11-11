# NerveGear Lab — Master Blueprint

Version: 1.0  
Prepared: November 10, 2026

## Core architecture: two cooperating AI systems

### AI 1 — Cloud Development AI
- Runs in a cloud development environment, independent of the user's personal computer once deployed.
- Builds and maintains the NerveGear Lab website from this blueprint.
- Can create/edit code, run tests, diagnose bugs, and make small improvements within approved boundaries.
- Uses a task queue, version control, backups, an activity log, and a persistent project workspace.
- Is controlled from Page 10, the AI Command Center.
- Does not claim to work in the cloud until the cloud runtime, credentials, task runner, storage, and deployment are actually configured.

### AI 2 — NerveGear Research AI
- Appears inside the NerveGear Lab website.
- Helps with scientific questions, literature research, mathematical models, and supported virtual simulations.
- Distinguishes established findings, approximations, simulation outputs, hypotheses, and speculation.
- Saves research notes, sources, project history, and experiment results.
- May send feature requests to AI 1, but AI 1 must present the proposal to the user before building new pages or making major changes.

### Owner controls
- The user is the project owner and administrator.
- Both AIs must follow role-based permissions and log important actions.
- The user can pause, resume, or stop development/research tasks.
- External actions such as spending money, publishing, connecting accounts, and physical experiments always require explicit approval.
- Do not infer approval from silence.

## Development change policy

### Allowed automatically
- Fix bugs.
- Make small, reversible improvements.
- Improve performance without changing intended behavior.
- Add tests and documentation.
- Update dependencies only when compatibility and security checks pass; otherwise request approval.

### Must ask the owner first
- Add a new page.
- Make a drastic change to an existing page or workflow.
- Remove major functionality.
- Change security, privacy, account, or permission behavior.
- Add a new external service or incur costs.

### Small-change notifications and undo
- Every change creates a concise activity entry: what changed, why, files affected, test result, and timestamp.
- Small changes do not require a disruptive alert.
- The owner can inspect changes and request an undo.
- Save a version/checkpoint before each change so rollback is possible.
- Major changes require a preview and approval before implementation.

## Page plan

1. Human Anatomy Explorer — layered anatomy, connected pathways, search, cross-sections, annotations.
2. Brain & Neuroscience — brain regions, neuron/synapse models, virtual neural-network builder.
3. AI Circuit Laboratory — 2D schematics, 3D board view, educational non-invasive circuit simulation.
4. Biological Modeling — atoms, molecules, proteins, DNA, cells, tissues, validity checks.
5. Signal Analysis — simulated/measured signal distinction, graphs, recordings, comparisons.
6. Experiment Laboratory — virtual experiments, shared workspace, session owner, private participant workspaces.
7. Research Library — scientific sources, citations, notes, provenance, quality checks.
8. Results Center — experiment history, reports, figures, exports, qualified conclusions.
9. Theoretical Physics & Discovery — mathematical models, theory comparisons, simulations, uncertainty labels.
10. AI Command Center — primary conversation, project controls, permission management, development AI workspace and progress.

The site may later add pages, but only after owner approval.

## Final planned stage: private mobile companion app
- Private access for the owner and a small, explicitly authorized group.
- Individual accounts and permissions.
- Optional notifications for major development milestones and important research updates.
- View progress and pause/resume approved work.
- Quiet activity feed for small changes.
- The website and cloud services remain the primary platform; the mobile app is optional.

## Cloud operation requirements
A real always-on cloud agent requires:
- A cloud host/runtime.
- Secure model-provider credentials stored as secrets (never pasted into chat or committed to source control).
- Persistent database/object storage.
- A task queue and worker process.
- A controlled code workspace and test runner.
- Version control and backups.
- Authentication, authorization, audit logs, and resource limits.
- Monitoring, error handling, and a way to pause/stop jobs.

The ChatGPT conversation itself is not a background worker. A cloud agent can continue only after these components are deployed and tested.

## Scientific integrity and safety
- Use reputable sources and cite them.
- Clearly label simplified models and visual aids.
- A simulation is not empirical proof.
- Do not present generated hypotheses as established discoveries.
- Human review is required for scientific claims, security-sensitive changes, and external publication.
- Keep the project focused on computational/virtual research and safe educational tools.
