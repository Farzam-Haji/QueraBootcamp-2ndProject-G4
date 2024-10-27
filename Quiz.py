from flask import Flask, render_template, request, redirect, url_for, session, g, Blueprint, flash
import sqlite3
import random
from functools import wraps

Quiz = Blueprint("Quiz", __name__)
# app.secret_key = "your_secret_key"

# Database connection
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('quiz.db')
        g.db.row_factory = sqlite3.Row  # Fetch rows as dictionaries
    return g.db

# Fetch all quiz categories from the database
def get_categories():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT name FROM categories")
    categories = [row['name'] for row in cursor.fetchall()]
    return categories

# Fetch questions for a specific category
def get_questions(category):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions WHERE category = ?", (category,))
    question_records = cursor.fetchall()
    questions = []
    for record in question_records:
        wrong_answers = record['wrong'].split(",")
        options = [record['answer']] + wrong_answers
        random.shuffle(options)
        questions.append({
            'question': record['question'],
            'answer': record['answer'],
            'options': options
        })
    
    return questions

# Admin required decorator
def admin_required(f):
    @wraps(f)
    def decoratorrr(*args, **kwargs):
        if 'username' not in session or session['username'] != "admin":
            return render_template('not_allowed.html')
        else:
            return f(*args, **kwargs)
    return decoratorrr


# Show quiz categories
@Quiz.route('/quiz/categories')
def show_categories():
    categories = get_categories()  # Fetch categories from the database
    return render_template('categories.html', categories=categories)

# Start quiz based on selected category
@Quiz.route('/quiz/<category>', methods=['GET', 'POST'])
def start_quiz(category):
    if request.method == 'POST':
        num_questions = int(request.form.get('num_questions'))
        questions = get_questions(category)  # Get available questions
        available_count = len(questions)

        if num_questions > available_count:
            flash(f"You requested {num_questions} questions, but only {available_count} are available.", 'danger')
            return render_template('select_num_questions.html', category=category)

        session['category'] = category
        session['num_questions'] = num_questions
        session['score'] = 0
        questions = get_questions(category)
        selected_questions = random.sample(questions, min(num_questions, available_count))  # Ensure we don't exceed available questions
        session['questions'] = selected_questions
        session['current_question'] = 0
        return redirect(url_for('Quiz.quiz'))
    return render_template('select_num_questions.html', category=category)

# Show quiz questions
@Quiz.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'questions' not in session or session['current_question'] >= session['num_questions']:
        return redirect(url_for('Quiz.show_result'))
    
    question = session['questions'][session['current_question']]
    if request.method == 'POST':
        selected_answer = request.form.get('answer')
        if selected_answer == question['answer']:
            session['score'] += 1
        session['current_question'] += 1
        return redirect(url_for('Quiz.quiz'))
    
    return render_template('quiz.html', question=question, question_num=session['current_question'] + 1)

# Show final result
@Quiz.route('/result')
def show_result():
    score = session.get('score',0)
    num_questions = session.get('num_questions', 1)
    

    username = session.get('username')
    if username:
        db = get_db()
        cursor = db.cursor()
        

        cursor.execute("SELECT quiz_results FROM users WHERE username = ?", (username,))
        result_row = cursor.fetchone()
        
        if result_row:
            current_results = result_row['quiz_results']
            new_results = f"{current_results},{score}" if current_results else str(score)
            cursor.execute("UPDATE users SET quiz_results = ? WHERE username = ?", (new_results, username))
            db.commit()

    feedback = f"Your score is {score} out of {num_questions}."
    return render_template('results.html', score=score, feedback=feedback)
