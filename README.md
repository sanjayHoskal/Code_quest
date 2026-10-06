# CodeQuest – Interactive Programming Quest Platform

---

## 🚀 Overview

**CodeQuest** is a Flask‑based web application that turns learning programming into an engaging adventure game.  Learners embark on *quests* (coding challenges) across multiple tracks—**Python**, **Java**, and **SQL**—and progress through levels, earn points, badges, and climb leaderboards.

The platform implements adaptive recommendation logic to serve challenges tailored to each learner’s performance, provides instant feedback on submissions, and offers a full‑featured admin console for managing content.

---

## ✨ Key Objectives (Implemented)

| # | Objective | Status |
|---|-----------|--------|
| 1 | Interactive platform for learning programming through gameplay | ✅ |
| 2 | Programming challenges arranged by difficulty & learning level | ✅ |
| 3 | Support for Python, Java, SQL tracks | ✅ |
| 4 | Points, badges, levels, leaderboards to encourage practice | ✅ |
| 5 | Immediate feedback for submitted answers or solutions | ✅ |
| 6 | Learner profiles & performance history | ✅ |
| 7 | Analyze learner performance & recommend appropriate challenges | ✅ |
| 8 | Administrator interface for managing questions, levels and content | ✅ |

---

## 🛠️ Technology Stack

- **Backend**: Python 3.11, **Flask**
- **Database**: SQLite (`codequest.db`)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript (see `static/js/quest_engine.js`)
- **Adaptive Engine**: Custom logic in `adaptive_engine.py`
- **Code Execution**: Sandbox wrapper in `code_runner.py`

---

## 📂 Project Structure

```
game_app/
│   app.py                # Flask app, routes & view logic
│   config.py             # Global configuration & constants
│   models.py             # DB access & business logic
│   adaptive_engine.py    # Adaptive recommendation engine
│   code_runner.py        # Safe evaluation of code answers
│   database.py           # DB connection helpers
│   seed_data.py          # Sample data loader
│   requirements.txt      # Python dependencies
│   README.md             # ← **this file**
│
├───templates/           # Jinja2 HTML templates
│   │   index.html
│   │   register.html
│   │   login.html
│   │   dashboard.html
│   │   challenge.html
│   │   profile.html
│   │   analytics.html
│   │   leaderboard.html
│   └───admin/          # Admin UI templates
│           admin_dashboard.html
│           questions.html
│           question_form.html
│           users.html
│
├───static/              # Static assets (CSS, JS, images)
│   └───js/
│           quest_engine.js
│
└───__pycache__/        # Compiled Python files (auto‑generated)
```

---

## 🎮 Features

- **Adaptive Quest Selection** – `adaptive_engine.get_next_adaptive_challenge` analyzes recent attempts, streaks, and topic weaknesses to suggest the next challenge.
- **Gamification** – XP, level progression, streak bonuses, first‑try bonus, speed bonuses, badges, and global/track leaderboards.
- **Immediate Feedback** – Submissions are evaluated instantly via `/api/submit-challenge`; response includes correctness, score, explanation, and next quest suggestion.
- **Learner Profiles** – Persistent user data, performance summary, badge collection, per‑track progress, and analytics page.
- **Admin Console** – CRUD UI for questions, tracks, users, and analytics dashboards.
- **Multi‑Track Support** – Users can switch between Python, Java, and SQL tracks; each track has its own question pool.
- **Extensible Architecture** – Adding new tracks, question types, or difficulty tiers only requires updates to `config.py` and corresponding DB entries.

---

## 📦 Getting Started

1. **Clone the repository** (or open the workspace at `d:/ML Projects/antigravity/game_app`).
2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Initialize the SQLite database** (creates tables and loads seed data):
   ```bash
   python app.py   # The script calls init_db() on first run
   ```
   The DB file `codequest.db` will be created in the project root.
5. **Run the development server**:
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:5000` in a browser.

---

## 🧪 Running Tests

A basic test suite lives in `test_app.py` and `test_core.py`. Run them with:
```bash
python -m unittest discover -s . -p "test_*.py"
```

---

## 📡 API Endpoints (important ones)

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/` | Landing page – redirects to dashboard if logged in |
| `POST`| `/register` | Create a new learner account (select track) |
| `POST`| `/login` | Authenticate user |
| `GET` | `/dashboard` | Learner hub – shows current XP, next quest, stats |
| `GET` | `/challenge/<int:question_id>` | Render a specific challenge |
| `GET` | `/challenge/next` | Adaptive next‑challenge redirect |
| `POST`| `/api/submit-challenge` | Submit an answer; returns JSON with feedback, XP, next‑question ID |
| `GET` | `/leaderboard` | Global & per‑track leaderboards |
| `GET` | `/profile` | Learner profile & recent activity |
| `GET` | `/analytics` | Detailed performance diagnostics |
| **Admin** | `/admin` | Admin dashboard (user & question stats) |
| **Admin** | `/admin/questions` | List / filter questions |
| **Admin** | `/admin/questions/new` | Create a new question |
| **Admin** | `/admin/questions/edit/<int:q_id>` | Edit an existing question |
| **Admin** | `/admin/questions/delete/<int:q_id>` (POST) | Delete a question |
| **Admin** | `/admin/users` | View all users (except admins) |

---

## 🔧 Extending the Platform

1. **Add a new track** –
   - Append the track name to `Config.TRACKS` in `config.py`.
   - Insert a row into the `tracks` table (run a migration or use the admin UI).
2. **New question type** –
   - Extend `code_runner.evaluate_challenge_answer` to handle the new type.
   - Update the admin forms (`templates/admin/question_form.html`) to capture required fields.
3. **Custom scoring** –
   - Adjust XP logic in `api_submit_challenge` or in `models.add_user_xp`.
4. **Styling** –
   - Modify CSS in the `static/` folder or add new stylesheets; the UI uses vanilla CSS for maximum flexibility.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feat/your-feature`).
3. Write tests for any new functionality.
4. Ensure all existing tests pass.
5. Submit a pull request with a clear description of changes.

---

## 📄 License

This project is released under the **MIT License**. See the `LICENSE` file for details.

---

## 📞 Contact

For questions or feedback, open an issue in the repository or contact the project maintainer.

---
*Created with Antigravity – your AI coding co-pilot.*
