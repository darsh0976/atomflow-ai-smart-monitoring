# AtomFlow AI Smart Monitoring Dashboard

A from-scratch project scaffold for rapid hackathon submission execution.

## What it includes
- Flask-based web app with a polished single-page dashboard.
- Preloaded hackathon timeline, deadline, eligibility, and prize information.
- Submission checklist to keep execution focused and complete.

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000.

## Suggested next upgrades
1. Add authentication + participant profile tracking.
2. Add data ingestion pipeline status cards.
3. Add exportable PDF report for final submission evidence.
4. Add CI pipeline for lint/tests/deploy.
