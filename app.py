from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


HACKATHON_CONTEXT = {
    "name": "AtomQuest Hackathon 2026",
    "organizer": "Atomberg Technologies Pvt. Ltd.",
    "mode": "Online",
    "team_size": "Individual Participation",
    "domain": "Data Engineering",
    "eligibility": [
        "Engineering students across all years",
        "Postgraduate & Undergraduate",
        "Management students",
    ],
    "deadline": "2026-05-15 23:59:00",
    "submission_window": {
        "start": "2026-05-16 00:00:00",
        "end": "2026-05-18 08:00:00",
    },
    "final_round": {
        "start": "2026-05-22 00:00:00",
        "end": "2026-05-24 00:01:00",
        "venue": "Atomberg R&D Centre, Pune",
    },
    "prizes": [
        {"position": "Winner", "amount": "₹50,000"},
        {"position": "First Runner-up", "amount": "₹30,000"},
        {"position": "Second Runner-up", "amount": "₹20,000"},
    ],
    "contact": "atomquest2025@atomberg.com",
}


@app.route("/")
def dashboard():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    return render_template("index.html", context=HACKATHON_CONTEXT, generated_at=now)


if __name__ == "__main__":
    app.run(debug=True)
