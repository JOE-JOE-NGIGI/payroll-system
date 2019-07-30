"""Importing sqlAlchemy object from main file --> app"""
from app import db
from models.Employees import EmployeesModel



""""""
class DepartmentModel(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    """Relationship that relates to """
    employees = db.relationship(EmployeesModel, backref='department')


