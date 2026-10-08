# CodeQuest – Interactive Programming Quest Platform

---

## 🚀 Overview

**CodeQuest** is a Flask-based web application that turns learning programming into an engaging adventure game. Learners embark on *quests* (coding challenges) across multiple tracks—**Python**, **Java**, and **SQL**—and progress through levels, earn points, and climb leaderboards.

The platform implements a massive pre-generated JSON question bank (`questions.json`) containing over 45,000 unique programming challenges. It offers instant feedback on submissions, a beautiful dark-mode glassmorphic user interface, and a robust built-in admin console for live content management.

---

## ✨ Key Features & Capabilities

- **Interactive Programming Gameplay**: Engaging gamified progression through various modes (Drag & Drop, MCQ, Fill in the Blanks, Code Arrangement, Syntax Validator, Debug the Code, Predict the Output).
- **Extensive Content**: Tracks in Python, Java, and SQL spanning Beginner to Advanced difficulties and scaling up to "Master" levels.
- **Level Locking & Unlocking**: Automatically unlocks higher levels as players progress through challenges sequentially.
- **Points & Global Leaderboards**: Awards XP/Points upon challenge completion, immediately updating the global ranking system.
- **Dark Mode UI**: Beautiful, modern "Glassmorphism" interface inherited natively across both player and admin views.
- **Full Admin Console (`/admin`)**:
  - Live analytics on total users and total scores.
  - End-to-end data control: Delete users or specific score entries to moderate the leaderboard.
  - **Question Manager (`/admin/questions`)**: Filter, edit (via live JSON editor), add, and delete questions securely. Any updates sync directly to `questions.json`.
  - Seamless "Make Admin" user role controls.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.11, **Flask**
- **Database**: SQLite (`scores.db` - automatically managed by SQLAlchemy)
- **Data Storage**: `questions.json` for all educational content logic.
- **Frontend**: HTML5, CSS3 (Custom variables, Glassmorphism, CSS Grid/Flexbox), Jinja2 Templating
- **Testing**: `pytest` and Flask Test Client (`test_app.py`)

---

## 📂 Project Structure

```
game_app/
│   app.py                # Main Flask application and all routing logic
│   questions.json        # 1.9MB+ JSON database of all programming challenges
│   test_app.py           # Pytest test suite ensuring app integrity
│   requirements.txt      # Python dependencies
│   README.md             # ← **this file**
│
├───templates/            # Jinja2 HTML templates
│       index.html
│       register.html
│       login.html
│       language.html
│       game_mode.html
│       difficulty.html
│       level.html
│       challenge.html
│       leaderboard.html
│       admin.html              # Admin Dashboard
│       admin_questions.html    # Admin Question Editor
│
└───static/               # Static assets
    └───css/
            theme.css     # Global sleek dark mode CSS system
```

---

## 📦 Getting Started (End-to-End Instructions)

1. **Clone the repository** and navigate to the project directory:
   ```bash
   cd "d:/ML Projects/antigravity/game_app"
   ```
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # Windows
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the development server**:
   ```bash
   python app.py
   ```
   The SQLite database (`scores.db`) will automatically initialize itself upon startup.
5. **Open your browser** and navigate to `http://127.0.0.1:5000`.

---

## 🛡️ Admin Setup

To access the Admin dashboard and question editor:
1. Navigate to `http://127.0.0.1:5000/register`.
2. Register a new user with the exact username **`admin`**.
3. Log in. The application will automatically assign you the `admin` role.
4. An **"🛡️ Admin"** button will appear in your top navigation bar.

---

## 🧪 Running Tests

A comprehensive test suite is located in `test_app.py` covering auth, protected routes, database integrity, question bank validations, and template rendering logic. 

Run the tests using pytest:
```bash
python -m pytest test_app.py
```

---

## 🤝 Contributing & Extending

1. **Adding Custom Questions**:
   You no longer need to modify the file directly! Simply log in as an admin, navigate to **Manage Question Bank**, select the category, and click **Add New Question**.
2. **Adding a New Mode/Language**:
   Update the hardcoded category checks in `app.py` (e.g., inside `normalize_language`) and add the category to `questions.json`.
3. **Styling Tweaks**:
   All frontend and backend views share `static/css/theme.css`. Modify the root variables (like `--primary` or `--bg-dark`) to re-theme the entire platform instantly.

---

## 📄 License

This project is released under the **MIT License**.
