from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '33c2660bb961efaa484a3ed88f478705'

# ✔ تصحيح خط PostgreSQL
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/blog-db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from blogapp import routes