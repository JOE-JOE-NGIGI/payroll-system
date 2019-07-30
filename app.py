"""importing flask class"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Development, Testing


"""instantiating class flask"""
app = Flask(__name__)

# this is a config parameter that shows where our db lives
app.config.from_object(Development)
#app.config.from_object(Testing)

db = SQLAlchemy(app)  #read this from documentation

from models.Employees import EmployeesModel
from models.Departments import DepartmentModel

@app.before_first_request
def create_tables():
    db.create_all()


"""Registering a route"""
@app.route('/')
def hello_world(): #Function to run when clients visit this route
    return render_template('index.html')


@app.route('/name')
def name():
    return 'Joe Ngigi'


# run flask
"""
if __name__ == '__main__':
    app.run()
"""