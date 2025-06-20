from database import create_db,add_user,check_user,get_all_superheroes,get_superhero
from flask import Flask, render_template, request, redirect, url_for, flash, session

app= Flask(__name__)
app.secret_key= "simplekey"
create_db()

@app.route("/")
def intro():
    render_template("index.html")


@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == 'POST':
        username = request.form['register_username']
        email = request.form['register_email']
        password = request.form['register_password']
        if add_user(username, email, password):#if the have been added the following will happen
            flash('Account created! Please log in.')
            return redirect(url_for('login'))  # This is a Redirect to login form
        flash('Username or email already exists.')
    return render_template('auth.html')  # Render auth.html for GET


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form("login_email")
        password = request.form("login_password")
        user = check_user(email,password)
        if user:#if it doesn't return "None", the folowing should happen
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('superheroes'))
        flash('Invalid email or password.')
    return render_template('auth.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('login'))  # Redirect to login


@app.route('/superheroes')
def superheroes():
    if 'user_id' not in session:
        flash('Please log in to view superheroes.')
        return redirect(url_for('login'))
    heroes = get_all_superheroes()
    username = session.get('username', 'Guest')#Guest is used a fallback incase the user's username is not found, which may be unlikely.
    return render_template('superheroes.html', heroes=heroes, username=username)

@app.route('/superhero/<int:hero_id>')
def hero_detail(hero_id):
    if 'user_id' not in session:
        flash('Please log in to view superhero details.')
        return redirect(url_for('login'))
    hero = get_superhero(hero_id)
    if not hero:
        flash('Superhero not found.')
        return redirect(url_for('superheroes'))
    return render_template('hero_detail.html', hero=hero)
