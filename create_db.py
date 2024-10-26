import sqlite3

connection = sqlite3.connect('quiz.db')
cursor = connection.cursor()

# #============================================ Categories ===========================================

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS categories (
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                name TEXT NOT NULL UNIQUE
#                )
# ''')

# #===================================================================================================

# #============================================ Questions ============================================

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS questions (
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                category TEXT NOT NULL,
#                question TEXT NOT NULL,
#                answer TEXT NOT NULL,
#                FOREIGN KEY (category) REFERENCES categories(name)
#                )
# ''')

# #===================================================================================================

# #============================================= Users ===============================================

# # table
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT NOT NULL UNIQUE,
#     first_name TEXT NOT NULL,
#     last_name TEXT NOT NULL,
#     email TEXT NOT NULL UNIQUE,
#     age INTEGER NOT NULL,
#     password TEXT NOT NULL,
#     quiz_results TEXT,
#     login BOOLEAN NOT NULL,
#     admin BOOLEAN NOT NULL
# )
# ''')
# #==================================================================================================

# #=========================================== Deafult rows =========================================

# users:
# cursor.execute("INSERT INTO users (username, first_name, last_name, email, age, password, quiz_results, login, admin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
#                ('user1', 'username1', 'userlastname1', 'useremail1@example.com', 10, 'password1', '10, 20, 30', True, True ))
# cursor.execute("INSERT INTO users (username, first_name, last_name, email, age, password, quiz_results, login, admin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
#                ('user2', 'username2', 'userlastname2', 'useremail2@example.com', 20, 'password2', '20, 30, 40', True, False ))
# cursor.execute("INSERT INTO users (username, first_name, last_name, email, age, password, quiz_results, login, admin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
#                ('user3', 'username3', 'userlastname3', 'useremail3@example.com', 30, 'password3', '30, 40, 50', True, False ))
# cursor.execute("INSERT INTO users (username, first_name, last_name, email, age, password, quiz_results, login, admin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
#                ('user4', 'username4', 'userlastname4', 'useremail4@example.com', 40, 'password4', '40, 50, 60', True, False ))
# cursor.execute("INSERT INTO users (username, first_name, last_name, email, age, password, quiz_results, login, admin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
#                ('user5', 'username5', 'userlastname5', 'useremail5@example.com', 50, 'password5', '50, 60, 70', True, False ))



# categories:
# cursor.execute("PRAGMA foreign_keys = ON")
# cursor.execute("INSERT INTO categories (name) VALUES (?)", ('Math',))
# cursor.execute("INSERT INTO categories (name) VALUES (?)", ('Geography',))
# cursor.execute("INSERT INTO categories (name) VALUES (?)", ('Literature',))

# #questions:
# cursor.execute("INSERT INTO questions (category, question, answer) VALUES (?, ?, ?)",
#                ('Math', '2+2', '4'))
# cursor.execute("INSERT INTO questions (category, question, answer) VALUES (?, ?, ?)",
#                ('Math', '3+4', '7'))
# cursor.execute("INSERT INTO questions (category, question, answer) VALUES (?, ?, ?)",
#                ('Math', '10x10', '100'))
# cursor.execute("INSERT INTO questions (category, question, answer) VALUES (?, ?, ?)",
#                ('Math', '10/5', '2'))
# cursor.execute("INSERT INTO questions (category, question, answer) VALUES (?, ?, ?)",
#                ('Geography', 'Capital of France?', 'Paris'))
# cursor.execute("INSERT INTO questions (category, question, answer) VALUES (?, ?, ?)",
#                ('Geography', 'Capital of England?', 'London'))
# cursor.execute("INSERT INTO questions (category, question, answer) VALUES (?, ?, ?)",
#                ('Literature', 'Author of Hamlet?', 'Shakespeare'))

# #===================================================================================================

# for deleting users:
# def delete_user(user_id):
#     connection = sqlite3.connect('quiz.db')
#     cursor = connection.cursor()
#     cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
#     connection.commit()
#     connection.close()
#     print(f"User with id {user_id} deleted successfully.")


# delete_user(1) # with index

connection.commit()

connection.close()