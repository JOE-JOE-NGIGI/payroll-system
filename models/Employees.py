from main import db

class EmployeesModel(db.Model):
    __tablename__ = 'employees'

    """nullability by default is true"""
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fullName = db.Column(db.String(60), nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    kraPin = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    nationalId = db.Column(db.String(50), unique=True, nullable=False)
    departmentId = db.Column(db.Integer, db.ForeignKey('departments.id'))
    basicSalary = db.Column(db.Float)
    benefits = db.Column(db.Float)

    # create
    """This is an instance method"""

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()
    # read
    @classmethod
    def fetch_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    # update
    @classmethod
        # read on keyword[default] functions
    def update_by_id(cls,id,fullName = None,gender = None,kraPin = None,email = None,nationalId = None,departmentId = None,basicSalary = None,benefits = None):

        record = cls.fetch_by_id(id=id)

        if fullName:
            record.fullName = fullName

        if gender:
            record.gender = gender

        if kraPin:
            record.kraPin = kraPin

        if email:
            record.email = email

        if nationalId:
            record.nationalId = nationalId

        if departmentId:
            record.departmentId = departmentId

        if basicSalary:
            record.basicSary = basicSalary

        if benefits:
            record.benefits = benefits

        db.session.commit()
        return True

        #   delete
    @classmethod
    def delete_by_id(cls,id):
        record = cls.query.filter_by(id=id)
        record.delete()
        db.session.commit()
        return True
