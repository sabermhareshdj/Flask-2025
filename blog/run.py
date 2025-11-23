from flask import Flask, render_template, flash, redirect, url_for
from forms import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '33c2660bb961efaa484a3ed88f478705'

posts = [
    {
        
        "title": "First Post",
        "description": "This is the content of the first post.",
        "created_at": "April 20, 2024",
        "author": "Alice",
    },
    {
        "title": "Second Post",
        "description": "This is the content of the second post.",
        "created_at": "April 21, 2024",
        "author": "Bob",
    },
    {
        "title": "Third Post",
        "description": "This is the content of the third post.",
        "created_at": "April 22, 2024",
        "author": "Charlie",
    }
]

@app.route("/")
def home():
    return render_template("home.html", posts=posts, title="Home Page")

@app.route("/about")
def about():
    return render_template("about.html", title="About")



@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Handle registration logic here
        flash(f'{form.username.data} Register successful!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


if __name__ == "__main__":  
    app.run(debug=True)