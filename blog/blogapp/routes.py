from flask import render_template, redirect, url_for, flash,request
from blogapp import app, db, bcrypt
from blogapp.models import Post,User
from blogapp.forms import RegisterForm, LoginForm, UpdateProfileForm
from flask_login import login_user,logout_user,current_user, login_required



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
            next_page = request.args.get('next')
            # if next_page:
            #     return redirect(next_page)
            #  return redirect(url_for('home'))
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Invalid email or password", "danger")

    return render_template("users/login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/profile", methods=['GET','POST'])
@login_required
def profile():
    # if not current_user.is_authenticated:
    #     return redirect(url_for('login'))

    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("your info has been updated", "success")
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template("users/profile.html", title="Profile", form=form)