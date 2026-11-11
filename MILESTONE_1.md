# Milestone 1 — Central AI and Cloud Infrastructure

## What this milestone establishes
This milestone prepares the project for two separate services:
1. A cloud development agent that maintains the website.
2. A research assistant embedded in the website.

They share approved project data and communicate through proposals, not unrestricted commands.

## First implementation sequence
1. Keep the website runnable locally while designing for cloud deployment.
2. Store the complete blueprint in `BLUEPRINT.md`.
3. Add an owner-controlled task/proposal queue.
4. Add an append-only activity log and change checkpoints.
5. Add a development-agent adapter interface. The adapter is intentionally unconfigured until a model provider and cloud host are selected.
6. Add authentication and secure secrets before exposing any service publicly.
7. Deploy a worker and web app to a cloud host only after the owner/guardian has selected an appropriate provider and reviewed any costs.

## Current status
- Blueprint: included.
- Existing Flask website scaffold: included.
- Cloud runtime: NOT deployed.
- AI model connection: NOT configured.
- Background worker: NOT deployed.
- Automatic code-writing: NOT enabled.
- Public internet exposure: NOT enabled.

## Why deployment is not automatic yet
A cloud deployment needs an account, secure credentials, and possibly paid services. Do not put API keys/passwords in chat, source files, screenshots, or Git commits. Use the provider's secret manager or environment variables. A parent/guardian may need to help with account and billing setup.

## Acceptance tests for this milestone
- The website starts locally.
- The blueprint can be opened from the project.
- The development dashboard clearly shows whether a cloud worker is connected.
- New-page and major-change proposals require owner approval.
- Small changes create a concise activity entry and a rollback checkpoint.
- No agent can spend money, publish, or run physical experiments.


## Milestone 2 — Local AI Command Center groundwork

Implemented in this update:
- Page 10 now includes a local development task queue.
- Tasks persist in `data/tasks.json` and are visible in the command center.
- Task submissions create concise activity records in `data/activity.json`.
- A project-status endpoint reports deployment and agent connection state.
- The interface explicitly states that queued tasks are not executed until a cloud worker and model are connected.

Not completed yet:
- No cloud provider has been selected or deployed.
- No model API is connected.
- No background worker executes queued tasks.
- No automatic code editing or deployment is enabled.

Verification note: Python syntax compilation passed. Runtime endpoint tests could not run in this environment because Flask is not installed here; install the listed requirements on the user's machine before running the app.
