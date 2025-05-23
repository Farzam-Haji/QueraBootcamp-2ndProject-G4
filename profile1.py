from flask import Flask, render_template, redirect, url_for, request, flash, g, Blueprint, session, abort
from flask_bcrypt import Bcrypt
import sqlite3
from functools import wraps

profile1 = Blueprint("profile1", __name__, template_folder="templates")
bcrypt = Bcrypt()

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('quiz.db')
        g.db.row_factory = sqlite3.Row
    return g.db

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('You need to log in first.')
            return redirect(url_for('login_signup.login'))
        return f(*args, **kwargs)
    return decorated_function

@profile1.route('/profile/<username>')
@login_required
def profile(username):
    if session['username'] != username:
        flash('You cannot access this profile.', 'danger')
        return redirect(url_for('profile1.profile', username=session['username']))

    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()

    if user is None:
        abort(404)  # 404 error

    return render_template('profile.html', user=user)

@profile1.route('/edit_profile/<username>', methods=['GET', 'POST'])
@login_required
def edit_profile(username):
    if session['username'] != username:
        flash('You cannot edit this profile.', 'danger')
        return redirect(url_for('profile1.profile', username=session['username']))

    conn = get_db()

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        age = request.form['age']
        password = request.form['password']

        if password:  #update the password if it's not empty
            hash_pass = bcrypt.generate_password_hash(password).decode('utf-8')
            conn.execute('UPDATE users SET first_name = ?, last_name = ?, email = ?, age = ?, password = ? WHERE username = ?',
                         (first_name, last_name, email, age, hash_pass, username))
        else:  # Update without changing the password
            conn.execute('UPDATE users SET first_name = ?, last_name = ?, email = ?, age = ? WHERE username = ?',
                         (first_name, last_name, email, age, username))

        conn.commit()
        conn.close()
        return redirect(url_for('profile1.profile', username=username))

    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()

    if user is None:
        abort(404)

    return render_template('edit_profile.html', user=user)

@profile1.route('/quiz_marks/<username>')
@login_required
def quiz_marks(username):
    if session['username'] != username:
        flash("You cannot view this user's quiz marks.", 'danger')
        return redirect(url_for('profile1.profile', username=session['username']))

    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()

    if user is None:
        abort(404)

 
    quiz_results = str(user['quiz_results']) if isinstance(user['quiz_results'], float) else user['quiz_results']
    

    quiz_marks = quiz_results.split(',') if quiz_results else []

    return render_template('quiz_marks.html', username=username, marks=quiz_marks)
