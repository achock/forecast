from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager


class Forecast(db.Model):
    """
    Create a Forecast table
    """

    __tablename__ = 'forecasts'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.String(15))
    hc = db.Column(db.Float)
    month_hours = db.Column(db.Integer)
    available = db.Column(db.Integer)
    holiday = db.Column(db.Float)

    holiday_percentage = db.Column(db.Float)
    comp_percentage =  db.Column(db.Float)
    illness_percentage =  db.Column(db.Float)
    others_percentage = db.Column(db.Float)
    vacation_percentage = db.Column(db.Float)
    overtime_percentage = db.Column(db.Float)
    education_percentage = db.Column(db.Float)

    agent_holiday_eight = db.Column(db.Integer)
    agent_holiday_ten   = db.Column(db.Integer)
    holiday_hours = db.Column(db.Integer)
    compensation_hours = db.Column(db.Float)
    illness_hours = db.Column(db.Float)
    others_hours = db.Column(db.Float)
    education_hours = db.Column(db.Float)
    normal_hours = db.Column(db.Float)
    overtime_hours = db.Column(db.Float)
    agent_vacation_eight = db.Column(db.Integer)
    agent_vacation_ten   = db.Column(db.Integer)
    vacation_hours = db.Column(db.Float)
    hc_vacation = db.Column(db.Float)
    chargeable = db.Column(db.Float)
    utilization = db.Column(db.Float)


    def __repr__(self):
        return '<Forecast: {}>'.format(self.id)


class Employee(UserMixin, db.Model):
    """
    Create an User table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('la contrasena no es valida.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))
