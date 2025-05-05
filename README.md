# Flask-based Quiz Web Application

This is an educational group project that serves and processes quizzes using a Flask web server.

## Features
- User authentication with hashed password storage
- Add and remove quiz questions
- Serve quizzes by category with a custom number of questions
- Save score history per user profile
- Use Flask flash messages for user feedback
- Styled with Bootstrap for a clean front-end

## Usage
- Run `main.py` to start the server at `http://localhost:5000`
- The `create_db.py` file was used to manually initialize the SQLite database during development. It’s not connected to the main application and mainly included as a reference.
- Login is required for most features; admin-only features include question management
- A pre-existing admin user is available:
  - **Username:** `admin`
  - **Password:** `admin`
- The database includes some sample questions for demonstration
- Install dependencies with pip install -r requirements.txt
