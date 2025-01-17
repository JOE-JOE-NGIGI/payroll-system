from main import db
from models.Employees import EmployeesModel



class PayrollsModel(db.Model):
    __tablename__ = 'payrolls'
    # name = db.Column(db.String(50))
    id = db.Column(db.Integer, primary_key=True)
    overtime = db.Column(db.Float)
    month = db.Column(db.String(20), nullable=False)
    advance_pay = db.Column(db.Float)
    gross_salary = db.Column(db.Float)
    personal_relief = db.Column(db.Float)
    taxable_income = db.Column(db.Float)
    PAYE = db.Column(db.Float)
    NHIF = db.Column(db.Float)
    NSSF = db.Column(db.Float)
    net_salary = db.Column(db.Float)
    """Defining foreign key for Table:Departments"""
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)

    # Create
    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_by_employee(cls, emp_id):
        return cls.query.filter_by(employee_id=emp_id)
