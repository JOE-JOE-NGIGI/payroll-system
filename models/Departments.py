"""Importing sqlAlchemy object from main file --> app"""
from main import db
from models.Employees import EmployeesModel



""""""
class DepartmentModel(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    """Relationship that relates to """
    employees = db.relationship(EmployeesModel, backref='department')


    # create
    """This is an instance method"""
    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    # Read
    """Read more on classes"""
    @classmethod
    def fetch_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    @classmethod
    def fetch_by_id(cls, dept_id):
        return cls.query.filter_by(id=dept_id).first()


    @classmethod
    def fetch_all(cls):
        return cls.query.all()



    @classmethod
    def fetch_total_payroll_by_id(cls,id):
        this_dept = cls.fetch_by_id(dept_id=id)
        total_payroll = 0
        for each_employee in this_dept.employees:
            total_payroll += each_employee.basicSalary + each_employee.benefits

            return total_payroll