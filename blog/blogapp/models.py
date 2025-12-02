from datetime import datetime
from blogapp import db

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
