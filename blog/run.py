from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == "__main__":  
    app.run(debug=True)