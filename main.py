"""importing flask class"""
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Development, Testing, Production
from resources.Payrollcalc import Payrollcalc


"""instantiating class flask"""
app = Flask(__name__)

# this is a config parameter that shows where our db lives
app.config.from_object(Development)
# app.config.from_object(Production)

db = SQLAlchemy(app)  #read this from documentation

from models.Employees import EmployeesModel
from models.Departments import DepartmentModel

# TODO: read about flask-migrate
@app.before_first_request
def create_tables():
    db.create_all()
"""This is a comment"""

"""Registering a route"""
"""routes can be placed anywhere after db"""
"""Model is a representation of a table in the real database"""

@app.route('/employees/<int:dept_id>')
def employees(dept_id):
    # departments = DepartmentModel.fetch_all()
    this_department = DepartmentModel.fetch_by_id(dept_id)
    # dept_name = dept.name

    """returns employees within the  department"""
    employees = this_department.employees
    return render_template('employees.html', this_department=this_department)

@app.route('/payrolls/<int:emp_id>')
def payrolls(emp_id):
    employee = EmployeesModel.fetch_by_id(emp_id)
    return render_template('payrolls.html', employee=employee)

@app.route('/')
def home():  # Function to run when clients visit this route
    departments = DepartmentModel.fetch_all()
    return render_template('index.html', deps=departments)


@app.route('/generate_payroll/<int:id>', methods=['POST'])
def generate_payroll(id):
    """instantiating the class"""
    this_employee = EmployeesModel.fetch_by_id(id)
    payroll = Employee(this_employee.fullName, this_employee.basicSalary, this_employee.benefits)
    # nhif = payroll.nhif
    print("nssf ", payroll.nssf_deduct)
    print("paye ", payroll.paye)
    print("net Salary ", payroll.netSalary)
    print("Gross Salary ", payroll.grossSalary)
    print("Personal relief ", payroll.relief)
    print("Taxable Income ", payroll.taxable_income)

@app.route('/name')
def name():
    return 'Joe Ngigi'

@app.route('/newDepartment',methods=['POST'])
def newDepartment():
    department_name = request.form['department']
    if DepartmentModel.fetch_by_name(department_name):
        """Read more on bootstrap alert with flash"""
        flash("Department " + department_name + "already exists!")
        return redirect(url_for('home'))
    department = DepartmentModel(name=department_name)
    department.insert_to_db()
    return redirect(url_for('home'))





@app.route('/newEmployee',methods=['POST'])
def newEmployee():
    name_of_employee = request.form['name']
    kra_pin = request.form['kra_pin']
    gender = request.form['gender']
    national_id = request.form['national_id']
    email = request.form['email']
    department_id = int(request.form['department'])
    basic_salary = request.form['basic_salary']
    benefits = request.form['benefits']

    employee = EmployeesModel(fullName=name_of_employee, gender=gender, kraPin=kra_pin, email=email, nationalId=national_id,
                              basicSalary=basic_salary, benefits=benefits, departmentId=department_id)
    employee.insert_to_db()
    # flash('Employee ' + name + ' has been added', 'success')
    return redirect(url_for('home'))




# run flask
"""
if __name__ == '__main__':
    app.run()
"""