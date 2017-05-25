from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,TextAreaField, SubmitField,DecimalField,HiddenField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from wtforms import validators
from wtforms.fields.html5 import EmailField,TelField
from ..models import Forecast, Employee


class ForecastForm(FlaskForm):
    """
    Form for admin to add or edit a forecast
    """
    month = SelectField('Month', choices = [('January', 'January'),
      ('February', 'February'),('March', 'March'),('April', 'April'),('May', 'May'),('June', 'June'),('July', 'July'),
      ('August', 'August'),('September', 'September'),('October', 'October'),('November', 'November'),
      ('December', 'December')])
    year = SelectField('Year', choices = [('2017', '2017'),
      ('2018', '2018'),('2019', '2019'),('2020', '2020'),('2021', '2021'),('2022', '2022'),('2023', '2023'),
      ('2024', '2024'),('2025', '2025'),('2026', '2026'),('2027', '2027'),
      ('2028', '2028')])
    hc = DecimalField('HC', validators=(validators.Optional(),))
    month_hours = DecimalField('Month Hours', validators=(validators.Optional(),))
    available = HiddenField('Available',validators=(validators.Optional(),))
    holiday = DecimalField('Holiday', validators=(validators.Optional(),))
    agent_holiday_eight = IntegerField('Agent Holiday Eight Hours',validators=(validators.Optional(),))
    agent_holiday_ten   = IntegerField('Agent Holiday Ten Hours',validators=(validators.Optional(),))
    holiday_hours = HiddenField('Holiday Hours', validators=(validators.Optional(),))
    compensation_hours = DecimalField('Compensation Hours', validators=(validators.Optional(),))
    illness_hours = DecimalField('Illness Hours', validators=(validators.Optional(),))
    others_hours = DecimalField('Others Hours', validators=(validators.Optional(),))
    education_hours = DecimalField('Education Hours', validators=(validators.Optional(),))
    vacation_hours = HiddenField('Vacation Hours', validators=(validators.Optional(),))
    normal_hours = HiddenField('Compensation Hours', validators=(validators.Optional(),))
    overtime_hours = DecimalField('Overtime Hours', validators=(validators.Optional(),))
    agent_vacation_eight = IntegerField('Agent Vacation Eight Hours',validators=(validators.Optional(),))
    agent_vacation_ten   = IntegerField('Agent Vacation Ten Hours',validators=(validators.Optional(),))

    holiday_percentage = HiddenField('Holiday%', validators=(validators.Optional(),))
    comp_percentage =  HiddenField('Comp%', validators=(validators.Optional(),))
    illness_percentage =  HiddenField('Illness%', validators=(validators.Optional(),))
    others_percentage = HiddenField('Others%', validators=(validators.Optional(),))
    vacation_percentage = HiddenField('Vacation%', validators=(validators.Optional(),))
    overtime_percentage = HiddenField('Overtime%', validators=(validators.Optional(),))
    education_percentage = HiddenField('Education%', validators=(validators.Optional(),))


    hc_vacation = DecimalField('HC Vacation',validators=(validators.Optional(),))
    chargeable = HiddenField('Chargeable',validators=(validators.Optional(),))
    utilization = DecimalField('Utilization',validators=(validators.Optional(),))
    submit = SubmitField('Register')
    
class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label="name")
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label="name")
    submit = SubmitField('Submit')
