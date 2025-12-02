from flask import render_template, redirect, url_for, flash
from blogapp import app
from blogapp.models import Post
from blogapp.forms import RegisterForm, LoginForm



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
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'{form.username.data} registered successfully!', 'success')
        return redirect(url_for('home'))
    return render_template("users/register.html", title="Register", form=form)


# login user مؤقت
user = {"email": "admin@gmail.com", "password": "123456"}


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == user['email'] and form.password.data == user['password']:
            flash("You have been logged in successfully", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid email or password", "danger")

    return render_template("users/login.html", title="Login", form=form)
