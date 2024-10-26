from flask import Flask, render_template, redirect, url_for, request, flash , g, Blueprint, session
import sqlite3
from functools import wraps

profile1 = Blueprint ("profile1", __name__, template_folder="templates")

user_data = {
    'name': 'username',
    'last_name': 'user lastname',
    'email': 'user@email.com',
    'age': 30,
    'username': 'user123',
    'password': '1234',
    'marks': [10, 8 , 7 ,5, 9]
}

@profile1.route('/profile')
def profile():
    return render_template('profile.html', user=user_data)

@profile1.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        user_data['name'] = request.form['name']
        user_data['last_name'] = request.form['last_name']
        user_data['email'] = request.form['email']
        user_data['age'] = request.form['age']
        print(user_data['password'])

        password = request.form.get('password')
        if password:
            user_data['password'] = password
            print(user_data['password']) #something
            pass
        
        flash('Profile updated successfully !', 'success')
        return redirect(url_for('profile1.profile'))

    return render_template('edit_profile.html', user=user_data)

@profile1.route('/quiz_marks')
def quiz_marks():
    return render_template('quiz_marks.html', marks=user_data['marks'])