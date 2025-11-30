from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for
from forms import RegisterForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '33c2660bb961efaa484a3ed88f478705'

# ✔ تصحيح خط PostgreSQL
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/blog-db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# بيانات مؤقتة للصفحة الرئيسية
# posts = [
#     {
#         "title": "First Post",
#         "description": "This is the content of the first post.",
#         "created_at": "April 20, 2024",
#         "author": "Alice",
#     },
#     {
#         "title": "Second Post",
#         "description": "This is the content of the second post.",
#         "created_at": "April 21, 2024",
#         "author": "Bob",
#     },
#     {
#         "title": "Third Post",
#         "description": "This is the content of the third post.",
#         "created_at": "April 22, 2024",
#         "author": "Charlie",
#     }
# ]


# =======================
#        MODELS
# =======================

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    password = db.Column(db.String(250), nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def ___init__(self, title, description,user_id) -> None:
        self.title = title
        self.description = description
        self.user_id = user_id

    # def __str__(self) -> None:
    #     return f"Post('{self.title}','{self.created_at}')"


    def __repr__(self):
        return f"Post('{self.title}', '{self.created_at}')"


# =======================
#        ROUTES
# =======================

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


# =======================
#       RUN APP
# =======================
if __name__ == "__main__":
    app.run(debug=True)
