from flask import render_template, redirect, url_for, flash
from blogapp import app, db, bcrypt
from blogapp.models import Post,User
from blogapp.forms import RegisterForm, LoginForm
from flask_login import login_user,logout_user,current_user



@app.route("/")
def home():
    posts = Post.query.all()
    # print(posts[0])
    # print(posts[1])
    return render_template("main/home.html", posts=posts, title="Home Page")


@app.route("/about")
def about():
    return render_template("main/about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data , pasword=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('registered successfully! , Please log in to your account', 'success')
        return redirect(url_for('login'))
    
    return render_template("users/register.html", title="Register", form=form)




@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user=user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash("Invalid email or password", "danger")

    return render_template("users/login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))