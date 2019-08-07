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
from models.Payrolls import PayrollsModel


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
    departments = DepartmentModel.fetch_all()
    return render_template('employees.html', this_department=this_department, deps=departments)

@app.route('/payrolls/<int:emp_id>')
def payrolls(emp_id):
    employee = EmployeesModel.fetch_by_id(emp_id)
    return render_template('payrolls.html', employee=employee)

"""Registering a route"""
@app.route('/')
def home():  # Function to run when clients visit this route
    departments = DepartmentModel.fetch_all()
    return render_template('index.html', deps=departments)

"""Register route for edit employee"""
@app.route('/editEmployee/<int:id>', methods=['POST'])
def editEmployee(id):
    name_of_employee = request.form['name']
    kra_pin = request.form['kra_pin']
    gender = request.form['gender']
    national_id = request.form['national_id']
    email = request.form['email']
    department_id = int(request.form['department'])
    basic_salary = request.form['basic_salary']
    benefits = request.form['benefits']


    if gender == "N/A":
        gender = None

    if department_id == "0":
        department_id = None

    EmployeesModel.update_by_id(id=id, fullName=name_of_employee, gender=gender, kraPin=kra_pin, email=email, nationalId=national_id, departmentId=department_id, basicSalary=basic_salary, benefits=benefits)

    """fetch employee"""
    this_emp = EmployeesModel.fetch_by_id(id=id)
    """fetch employee's department"""
    this_dept = this_emp.department
    return redirect(url_for('employees', dept_id=this_dept.id))

    """call function"""
@app.route('/deleteEmployee/<int:id>')
def deleteEmployee(id) :
    """Function to delete employee"""
    this_emp = EmployeesModel.fetch_by_id(id=id)
    this_dept = this_emp.department
    EmployeesModel.delete_by_id(id)
    return redirect(url_for('employees', dept_id=this_dept.id))




@app.route('/generate_payroll/<int:id>', methods=['POST'])
def generate_payroll(id):
    """instantiating the class"""
    this_employee = EmployeesModel.fetch_by_id(id)
    payroll = Payrollcalc(this_employee.fullName, this_employee.basicSalary, this_employee.benefits)
    nhif = payroll.NHIF_deduct
    nssf = payroll.nssf_deduct
    paye = payroll.paye
    net_Salary = payroll.netSalary
    Gross_Salary = payroll.grossSalary
    Personal_relief = payroll.relief
    Taxable_Income = payroll.taxable_income

    return render_template('payrolls.html', this_employee=EmployeesModel)


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