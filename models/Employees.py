from app import db

class EmployeesModel(db.Model):
    __tablename__ = 'employees'

    """nullability by default is true"""
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fullName = db.Column(db.String(60), nullable=False)
    kraPin = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    nationalId = db.Column(db.String(50), unique=True, nullable=False)
    departmentId = db.Column(db.Integer, db.ForeignKey('departments.id'))
    basicSalary = db.Column(db.Float)
    benefits = db.Column(db.Float)