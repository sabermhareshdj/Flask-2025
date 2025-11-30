- pip freeze or pip list # show all library in project
- pip freeze > requirements.txt

flask --app run.py db init # create migrations folder
flask --app run.py db migrate # create migration file
flask --app run.py db upgrade # create database