from flask import Flask, render_template, request, session, redirect, url_for, flash
import random
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
app = Flask(__name__)
app.secret_key = "codequest_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scores.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Load questions dynamically
def load_question_bank():
    with open('questions.json', 'r', encoding='utf-8') as f:
        return json.load(f)

question_bank = load_question_bank()

def normalize_language(lang):
    if not lang:
        return "Python"
    s = str(lang).strip()
    if s.lower() == "sql":
        return "SQL"
    elif s.lower() == "python":
        return "Python"
    elif s.lower() == "java":
        return "Java"
    return s

def normalize_level(level_str):
    if not level_str:
        return "1"
    s = str(level_str).strip()
    if s.lower() in ["master", "4"]:
        return "4"
    return s

# =========================================================
# QUESTION BANK
# =========================================================

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), default='learner')
    total_xp = db.Column(db.Integer, default=0)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to continue.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to continue.', 'warning')
            return redirect(url_for('login'))
        user = db.session.get(User, session['user_id'])
        if not user or user.role != 'admin':
            flash('Access denied. Admins only.', 'danger')
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function

# Question bank is now loaded from questions.json


# =========================================================
# QUESTION SELECTION
# =========================================================

def get_question(language, game_mode, difficulty, level_str, challenge_number, force_new=False):
    global question_bank
    lang_key = normalize_language(language)
    lvl_key = normalize_level(level_str)
    mode_key = str(game_mode).strip() if game_mode else "Drag & Drop"
    diff_key = str(difficulty).strip() if difficulty else "Beginner"

    # Try to drill down into the JSON dictionary
    try:
        lang_dict = question_bank.get(lang_key)
        if not lang_dict:
            question_bank = load_question_bank()
            lang_dict = question_bank.get(lang_key, {})
        
        mode_dict = lang_dict.get(mode_key)
        if not mode_dict:
            # Handle aliases for Syntax Validator / Code Arrangement
            if mode_key == "Code Arrangement":
                mode_dict = lang_dict.get("Syntax Validator", {})
            elif mode_key == "Syntax Validator":
                mode_dict = lang_dict.get("Code Arrangement", {})
            else:
                mode_dict = {}

        diff_dict = mode_dict.get(diff_key, {})
        bank = diff_dict.get(lvl_key) or diff_dict.get(str(level_str)) or diff_dict.get("1")
        if not bank:
            raise KeyError(f"No questions for {lang_key} > {mode_key} > {diff_key} > {lvl_key}")
    except Exception as e:
        return {"type": "fill", "question": f"Error loading question: {e}", "code_snippet": "Missing data", "correct_answer": "404", "hint1": "", "hint2": "", "explanation": ""}

    # Session caching to prevent duplicates in the same run
    current_questions = session.get("current_questions", {})
    key = f"{lang_key}_{mode_key}_{diff_key}_{lvl_key}_{challenge_number}"
    
    if not force_new and key in current_questions:
        idx = current_questions[key]
        if idx < len(bank):
            return bank[idx]

    used_questions = session.get("used_questions", {})
    used_key = f"{lang_key}_{mode_key}_{diff_key}_{lvl_key}"
    used = used_questions.get(used_key, [])
    
    all_indexes = list(range(len(bank)))
    available = [i for i in all_indexes if i not in used]
    
    if not available:
        used = []
        available = all_indexes
        
    selected_index = random.choice(available)
    used.append(selected_index)
    
    used_questions[used_key] = used
    current_questions[key] = selected_index
    
    # Cap session dictionaries to recent items to prevent 4KB cookie overflow
    if len(used_questions) > 8:
        for k in list(used_questions.keys())[:-8]:
            del used_questions[k]
    if len(current_questions) > 12:
        for k in list(current_questions.keys())[:-12]:
            del current_questions[k]

    session["used_questions"] = used_questions
    session["current_questions"] = current_questions
    session.modified = True
    
    return bank[selected_index]


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():
    user = None
    if 'user_id' in session:
        user = db.session.get(User, session['user_id'])
    return render_template("index.html", user=user)

# =========================================================
# AUTHENTICATION
# =========================================================

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash("Username or email already exists.", "danger")
            return redirect(url_for("register"))
            
        hashed_password = generate_password_hash(password)
        
        role = 'admin' if username.lower() == 'admin' else 'learner'
        new_user = User(username=username, email=email, password_hash=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()
        
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            session["player_name"] = user.username
            flash(f"Welcome back, {user.username}!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials.", "danger")
    return render_template("login.html")

@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        flash("Password reset link sent to your email (simulation).", "info")
        return redirect(url_for("login"))
    return render_template("forgot_password.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))

@app.route("/profile")
@login_required
def profile():
    user = db.session.get(User, session['user_id'])
    return render_template("profile.html", user=user)

# =========================================================
# ADMIN DASHBOARD
# =========================================================

@app.route("/admin")
@admin_required
def admin_dashboard():
    users = User.query.all()
    scores = Score.query.order_by(Score.score.desc()).all()
    # Count some stats
    total_users = len(users)
    total_scores = len(scores)
    return render_template("admin.html", users=users, scores=scores, total_users=total_users, total_scores=total_scores)

@app.route("/admin/make_admin/<int:user_id>", methods=["POST"])
@admin_required
def make_admin(user_id):
    user = db.session.get(User, user_id)
    if user:
        user.role = 'admin'
        db.session.commit()
        flash(f"User {user.username} is now an admin.", "success")
    return redirect(url_for("admin_dashboard"))


# =========================================================
# PLAYER SETUP
# =========================================================

@app.route("/player")
@login_required
def player():
    # Since they are logged in, we already know their name. 
    # Let's just pass them straight to language selection.
    user = db.session.get(User, session['user_id'])
    session["player_name"] = user.username
    return render_template("language.html", player_name=user.username)

# =========================================================
# LANGUAGE
# =========================================================

@app.route("/language", methods=["GET", "POST"])
def language():
    player_name = session.get("player_name", "Player")
    if 'user_id' in session:
        user = db.session.get(User, session['user_id'])
        if user:
            player_name = user.username
            session["player_name"] = player_name
    return render_template(
        "language.html",
        player_name=player_name
    )


# =========================================================
# START GAME
# =========================================================

@app.route("/start_game", methods=["GET", "POST"])
def start_game():
    if request.method == "POST":
        language = request.form.get("language")
        if language:
            return render_template(
                "game_mode.html",
                language=language
            )

    # Handled via GET: if language parameter is present in query string
    language = request.args.get("language")
    if language:
        return render_template(
            "game_mode.html",
            language=language
        )

    # Otherwise render the language tracks page for quick play
    player_name = session.get("player_name", "Player")
    if 'user_id' in session:
        user = db.session.get(User, session['user_id'])
        if user:
            player_name = user.username
            session["player_name"] = player_name

    return render_template(
        "language.html",
        player_name=player_name
    )


# =========================================================
# DIFFICULTY
# =========================================================

@app.route("/difficulty", methods=["GET", "POST"])
def difficulty():

    language = request.form.get("language") or request.args.get("language")
    game_mode = request.form.get("game_mode") or request.args.get("game_mode")

    return render_template(
        "difficulty.html",
        language=language,
        game_mode=game_mode
    )


# =========================================================
# LEVEL
# =========================================================

@app.route("/level", methods=["GET", "POST"])
def level():

    language = request.form.get("language") or request.args.get("language")
    game_mode = request.form.get("game_mode") or request.args.get("game_mode")
    difficulty = request.form.get("difficulty") or request.args.get("difficulty")

    unlock_key = f"{language}_{game_mode}_{difficulty}_unlocked"
    unlocked_level = session.get(unlock_key, 1)

    return render_template(
        "level.html",
        language=language,
        game_mode=game_mode,
        difficulty=difficulty,
        unlocked_level=unlocked_level
    )


# =========================================================
# CHALLENGE
# =========================================================

@app.route("/challenge", methods=["GET", "POST"])
def challenge():

    language = request.form.get("language") or request.args.get("language")
    game_mode = request.form.get("game_mode") or request.args.get("game_mode")
    difficulty = request.form.get("difficulty") or request.args.get("difficulty")
    level = request.form.get("level") or request.args.get("level")

    unlock_key = f"{language}_{game_mode}_{difficulty}_unlocked"
    current_unlocked = session.get(unlock_key, 1)

    # Process level unlocking
    if request.form.get("unlock") == "true":
        req_lvl = 4 if str(level).lower() == 'master' else int(level)
        if req_lvl > current_unlocked:
            session[unlock_key] = req_lvl
            session.modified = True
            current_unlocked = req_lvl

    req_lvl_check = 4 if str(level).lower() == 'master' else int(level)
    if req_lvl_check > current_unlocked:
        flash("Level is locked! Complete previous levels first.", "warning")
        return redirect(url_for('level', language=language, game_mode=game_mode, difficulty=difficulty))

    challenge_number = int(
        request.form.get("challenge") or request.args.get("challenge", "1")
    )

    # Fetch question dynamically using all context variables
    question = get_question(
        language,
        game_mode,
        difficulty,
        level,
        challenge_number,
        force_new=False
    )

    # Handle order vs fill types
    question_type = question.get("type", "order")
    correct_order = []
    displayed_blocks = []
    
    if question_type == "order":
        correct_order = [block["id"] for block in question.get("blocks", [])]
        displayed_blocks = question.get("blocks", []).copy()
        random.shuffle(displayed_blocks)
        
    return render_template(
        "challenge.html",
        language=language,
        game_mode=game_mode,
        difficulty=difficulty,
        level=level,
        challenge_number=challenge_number,
        question=question,
        displayed_blocks=displayed_blocks,
        correct_order=correct_order
    )


# =========================================================
# NEXT CHALLENGE
# =========================================================

@app.route("/next_challenge", methods=["POST"])
def next_challenge():

    language = request.form.get("language")
    game_mode = request.form.get("game_mode")
    difficulty = request.form.get("difficulty")
    level = request.form.get("level")

    current_challenge = int(
        request.form.get("current_challenge", "1")
    )

    next_challenge_number = current_challenge + 1

    # Remove the old question for the next challenge
    current_questions = session.get(
        "current_questions", {}
    )

    key = f"{language}_{game_mode}_{difficulty}_{level}_{next_challenge_number}"
    norm_key = f"{normalize_language(language)}_{game_mode}_{difficulty}_{normalize_level(level)}_{next_challenge_number}"
    current_questions.pop(key, None)
    current_questions.pop(norm_key, None)
    current_questions.pop(str(next_challenge_number), None)

    session["current_questions"] = current_questions
    session.modified = True

    question = get_question(
        language,
        game_mode,
        difficulty,
        level,
        next_challenge_number,
        force_new=True
    )

    question_type = question.get("type", "order")
    correct_order = []
    displayed_blocks = []
    
    if question_type == "order":
        correct_order = [block["id"] for block in question.get("blocks", [])]
        displayed_blocks = question.get("blocks", []).copy()
        random.shuffle(displayed_blocks)

    return render_template(
        "challenge.html",
        language=language,
        game_mode=game_mode,
        difficulty=difficulty,
        level=level,
        challenge_number=next_challenge_number,
        question=question,
        displayed_blocks=displayed_blocks,
        correct_order=correct_order
    )


# =========================================================
# SCORING & LEADERBOARD
# =========================================================

@app.route("/submit_score", methods=["POST"])
def submit_score():
    data = request.get_json() or {}
    points = int(data.get("points", 10))
    player_name = session.get("player_name", "Anonymous")

    # Update Score leaderboard
    score_entry = Score.query.filter_by(player_name=player_name).first()
    if not score_entry:
        score_entry = Score(player_name=player_name, score=0)
        db.session.add(score_entry)
    score_entry.score += points
    
    # Update User overall XP if logged in
    if 'user_id' in session:
        user = db.session.get(User, session['user_id'])
        if user:
            user.total_xp += points

    db.session.commit()
    
    return {"status": "success", "new_score": score_entry.score}, 200

@app.route("/leaderboard")
def leaderboard():
    top_scores = Score.query.order_by(Score.score.desc()).limit(10).all()
    return render_template("leaderboard.html", top_scores=top_scores)


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)