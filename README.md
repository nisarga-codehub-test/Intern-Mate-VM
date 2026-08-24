# InternMate Django App

Phase 0/1 baseline build using Django + DRF + Bootstrap + SQLite.

## Local Setup

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_baseline
python manage.py runserver
```

Landing URL: `/` (includes InternMate overview banner + admin login entry)
Login URL: `/login/` or `/accounts/login/`

Seeded users (`password: pass1234`):
- `admin` (Admin)
- `manager` (Manager)
- `mentor` (Mentor)
- `hr` (HR)
- `intern1` (Intern)
- `intern2` (Intern)

## Included
- Modern responsive landing/login UX with InternMate about/help sections
- Common header, menu, and footer shell across authenticated pages
- Role-aware web pages: dashboard, daily logs, daily stats, reports
- Core data model: interns/projects/daily logs/dependencies/AI usage/review/audit
- REST API under `/api/`
- Workflow action endpoint: `POST /api/daily-logs/{id}/workflow/`
- Export endpoint: `/reports/export/?format=csv|xlsx|pdf`

## Notes
- On Hold logic: blocked tasks or unresolved dependencies.
- Overdue logic: calendar-day based.
- HR API responses hide raw task text fields (summary-only visibility).
- Seed command now creates realistic mock daily logs, dependencies, AI usage, and review comments.

## MCP (HTTP) for Codex CLI
- MCP server module: `mcp_server/`
- Tool naming: `InternMate_*`
- Setup/run docs: `mcp_server/README.md`
