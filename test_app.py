import pytest
from app import app, db, User, Score
import json

@pytest.fixture
def client():
    # Configure app for testing
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_index_page(client):
    """Test that the index page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'CodeQuest' in response.data

def test_register_user(client):
    """Test user registration."""
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    # Should redirect to login after successful registration
    assert b'Sign In' in response.data

    # Verify user was created in the database
    with app.app_context():
        user = User.query.filter_by(username='testuser').first()
        assert user is not None
        assert user.role == 'learner'

def test_admin_registration(client):
    """Test that registering as 'admin' grants admin role."""
    client.post('/register', data={
        'username': 'admin',
        'email': 'admin@example.com',
        'password': 'adminpassword'
    })
    
    with app.app_context():
        user = User.query.filter_by(username='admin').first()
        assert user is not None
        assert user.role == 'admin'

def test_login_logout(client):
    """Test user login and logout."""
    # First register a user
    client.post('/register', data={
        'username': 'logintester',
        'email': 'login@example.com',
        'password': 'password123'
    })

    # Test login
    response = client.post('/login', data={
        'username': 'logintester',
        'password': 'password123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    # The index page should greet the user
    assert b'Welcome, logintester!' in response.data
    
    # Test logout
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'You have been logged out' in response.data

def test_protected_routes(client):
    """Test that protected routes require login."""
    # /player is protected
    response = client.get('/player', follow_redirects=True)
    assert b'Please log in to continue' in response.data

def test_submit_score(client):
    """Test submitting a score when logged in."""
    # Register and login
    client.post('/register', data={
        'username': 'scoreuser',
        'email': 'score@example.com',
        'password': 'password'
    })
    client.post('/login', data={
        'username': 'scoreuser',
        'password': 'password'
    })
    
    # Submit score
    response = client.post('/submit_score', json={'points': 20})
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert data['new_score'] == 20
    
    # Verify in DB
    with app.app_context():
        user = User.query.filter_by(username='scoreuser').first()
        assert user.total_xp == 20

def test_question_bank_integrity():
    """Verify that questions.json contains complete, authentic questions for all tracks, modes, and levels."""
    with open('questions.json', 'r', encoding='utf-8') as f:
        qbank = json.load(f)

    for lang in ['Python', 'Java', 'SQL']:
        assert lang in qbank
        for mode in ['Drag & Drop', 'MCQ Challenge', 'Code Arrangement', 'Syntax Validator', 'Debug the Code', 'Predict the Output', 'Fill in the Blanks']:
            assert mode in qbank[lang]
            for diff in ['Beginner', 'Intermediate', 'Advanced']:
                assert diff in qbank[lang][mode]
                for lvl in ['1', '2', '3', '4', 'Master']:
                    slot = qbank[lang][mode][diff][lvl]
                    assert len(slot) >= 3, f"Expected at least 3 questions in {lang} {mode} {diff} L{lvl}, got {len(slot)}"
                    for q in slot:
                        assert q.get('question')
                        assert q.get('hint1')
                        assert q.get('hint2')
                        assert q.get('explanation')

def test_challenge_rendering(client):
    """Test that challenge renders order, fill, mcq, debug, predict modes, SQL, Master level, and Syntax Validator."""
    # Test Drag & Drop (order)
    resp = client.post('/challenge', data={
        'language': 'Python',
        'game_mode': 'Drag & Drop',
        'difficulty': 'Beginner',
        'level': '1',
        'challenge': '1'
    })
    assert resp.status_code == 200
    assert b'Drag and arrange the code blocks' in resp.data

    # Test Fill in the Blanks
    resp_fill = client.post('/challenge', data={
        'language': 'Python',
        'game_mode': 'Fill in the Blanks',
        'difficulty': 'Beginner',
        'level': '1',
        'challenge': '1'
    })
    assert resp_fill.status_code == 200
    assert b'fillInput' in resp_fill.data

    # Test MCQ Challenge
    resp_mcq = client.post('/challenge', data={
        'language': 'Python',
        'game_mode': 'MCQ Challenge',
        'difficulty': 'Beginner',
        'level': '1',
        'challenge': '1'
    })
    assert resp_mcq.status_code == 200
    assert b'mcqOptions' in resp_mcq.data

    # Test Syntax Validator (True/False mode)
    resp_bool = client.post('/challenge', data={
        'language': 'Python',
        'game_mode': 'Syntax Validator',
        'difficulty': 'Beginner',
        'level': '1',
        'challenge': '1'
    })
    assert resp_bool.status_code == 200
    assert b'boolOptions' in resp_bool.data
    assert b'TRUE' in resp_bool.data
    assert b'FALSE' in resp_bool.data
    assert b'Error loading question' not in resp_bool.data

    # Test SQL track
    resp_sql = client.post('/challenge', data={
        'language': 'SQL',
        'game_mode': 'Predict the Output',
        'difficulty': 'Intermediate',
        'level': '2',
        'challenge': '1',
        'unlock': 'true'
    })
    assert resp_sql.status_code == 200
    assert b'predictInput' in resp_sql.data
    assert b'Error loading question' not in resp_sql.data

    # Test Master Level
    resp_master = client.post('/challenge', data={
        'language': 'Java',
        'game_mode': 'Debug the Code',
        'difficulty': 'Advanced',
        'level': 'Master',
        'challenge': '1',
        'unlock': 'true'
    })
    assert resp_master.status_code == 200
    assert b'Master Challenge' in resp_master.data
    assert b'Error loading question' not in resp_master.data


