from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the form data
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']

        # Connect to the database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # Insert the new user into the database
        c.execute('INSERT INTO users (fname, lname, phone, email, password) VALUES (?, ?, ?, ?, ?)', (fname, lname, phone, email, password))
        conn.commit()

        # Close the database connection
        conn.close()

        return redirect('/login')
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the form data
        email = request.form['email']
        password = request.form['password']

        # Connect to the database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # Retrieve the user from the database
        c.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
        user = c.fetchone()

        # Close the database connection
        conn.close()

        if user:
            # User is authenticated, so redirect to the to-do list page
            return redirect('/todo')
        else:
            # User is not authenticated, so render the login page with an error message
            error = "Invalid email or password. Please try again."
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')

@app.route('/todo')
def todo():
    # Connect to the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Retrieve all the to-do items from the database
    c.execute('SELECT * FROM todo')
    items = c.fetchall()

    # Close the database connection
    conn.close()

    return render_template
