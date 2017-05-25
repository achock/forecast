from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import ForecastForm
from .. import db
from ..models import Employee, Forecast
import arrow
import datetime

def check_admin():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)


# Forecast Views


@admin.route('/forecasts')
@login_required
def list_forecasts():
    check_admin()
    """
    List all forecasts
    """
    mDate =  arrow.now().format('YYYY')
    forecasts = Forecast.query.order_by(Forecast.id).all()
    return render_template('admin/forecasts/forecasts.html',
                           forecasts=forecasts, mYear=mDate, title='Forecasts')


@admin.route('/forecasts/add', methods=['GET', 'POST'])
@login_required
def add_forecast():
    """
    Add a forecasts to the database
    """
    check_admin()

    add_forecast = True

    form = ForecastForm()
    if form.validate_on_submit():
        forecasts = Forecast(year=form.year.data,
            month = form.month.data,
            hc = form.hc.data,
            month_hours = form.month_hours.data,
            available = form.available.data,
            holiday = form.holiday.data,
            holiday_percentage = form.holiday_percentage.data,
            comp_percentage =  form.comp_percentage.data,
            illness_percentage =  form.illness_percentage.data,
            others_percentage = form.others_percentage.data,
            vacation_percentage = form.vacation_percentage.data,
            overtime_percentage = form.overtime_percentage.data,
            education_percentage = form.education_percentage.data,
            agent_holiday_ten   = form.agent_holiday_ten.data,
            agent_holiday_eight = form.agent_holiday_eight.data,

            holiday_hours = form.holiday_hours.data,
            compensation_hours = form.compensation_hours.data,
            illness_hours = form.illness_hours.data,
            others_hours = form.others_hours.data,
            education_hours = form.education_hours.data,
            normal_hours = form.normal_hours.data,
            overtime_hours = form.overtime_hours.data,
            agent_vacation_eight = form.agent_vacation_eight.data,
            agent_vacation_ten   = form.agent_vacation_ten.data,
            vacation_hours = form.vacation_hours.data,
            hc_vacation = form.hc_vacation.data,
            chargeable = form.chargeable.data,
            utilization = form.utilization.data)
        db.session.add(forecasts)
        db.session.commit()
        flash('You have added a forecast successfully')

        # redirect to the forecasts page
        return redirect(url_for('admin.list_forecasts'))

    # load role template
    return render_template('admin/forecasts/forecast.html', add_forecast=add_forecast,
                           form=form, title='Add Forecast')


@admin.route('/forecasts/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_forecast(id):
    """
    Edit a forecast
    """
    check_admin()

    add_forecast = False

    forecast = Forecast.query.get_or_404(id)
    form = ForecastForm(obj=forecast)
    if form.validate_on_submit():
        forecast.year=form.year.data
        forecast.month = form.month.data
        forecast.hc = form.hc.data
        forecast.month_hours = form.month_hours.data
        forecast.available = form.available.data
        forecast.holiday = form.holiday.data
        forecast.holiday_percentage = form.holiday_percentage.data
        forecast.comp_percentage =  form.comp_percentage.data
        forecast.illness_percentage =  form.illness_percentage.data
        forecast.others_percentage = form.others_percentage.data
        forecast.vacation_percentage = form.vacation_percentage.data
        forecast.overtime_percentage = form.overtime_percentage.data
        forecast.education_percentage = form.education_percentage.data

        forecast.agent_holiday_eight = form.agent_holiday_eight.data
        forecast.agent_holiday_ten  = form.agent_holiday_ten.data,
        forecast.holiday_hours = form.holiday_hours.data,
        forecast.compensation_hours = form.compensation_hours.data,
        forecast.illness_hours = form.illness_hours.data,
        forecast.others_hours = form.others_hours.data,
        forecast.education_hours = form.education_hours.data,
        forecast.normal_hours = form.normal_hours.data,
        forecast.overtime_hours = form.overtime_hours.data,
        forecast.agent_vacation_eight = form.agent_vacation_eight.data,
        forecast.agent_vacation_ten   = form.agent_vacation_ten.data,
        forecast.vacation_hours = form.vacation_hours.data,
        forecast.hc_vacation = form.hc_vacation.data,
        forecast.chargeable = form.chargeable.data,
        forecast.utilization = form.utilization.data
        db.session.add(forecast)
        db.session.commit()
        flash('You have edited the forecast in the db.')

        # redirect to the roles page
        return redirect(url_for('admin.list_forecasts'))

    form.year.data = forecast.year
    form.month.data = forecast.month
    form.hc.data = forecast.hc
    form.month_hours.data = forecast.month_hours
    form.available.data = forecast.available
    form.holiday.data = forecast.holiday
    form.holiday_percentage.data = forecast.holiday_percentage
    form.comp_percentage.data =  forecast.comp_percentage
    form.illness_percentage.data =  forecast.illness_percentage
    form.others_percentage.data = forecast.others_percentage
    form.vacation_percentage.data = forecast.vacation_percentage
    form.overtime_percentage.data = forecast.overtime_percentage
    form.education_percentage.data = forecast.education_percentage
    form.agent_holiday_eight.data = forecast.agent_holiday_eight
    form.agent_holiday_ten.data  = forecast.agent_holiday_ten
    form.holiday_hours.data = forecast.holiday_hours
    form.compensation_hours.data = forecast.compensation_hours
    form.illness_hours.data = forecast.illness_hours
    form.others_hours.data = forecast.others_hours
    form.education_hours.data = forecast.education_hours
    form.normal_hours.data = forecast.normal_hours
    form.overtime_hours.data = forecast.overtime_hours
    form.agent_vacation_eight.data = forecast.agent_vacation_eight
    form.agent_vacation_ten.data   = forecast.agent_vacation_ten
    form.vacation_hours.data = forecast.vacation_hours
    form.hc_vacation.data = forecast.hc_vacation
    form.chargeable.data = forecast.chargeable
    form.utilization.data = forecast.utilization


    return render_template('admin/forecasts/forecast.html', add_forecast=add_forecast,
                           form=form, title="Modify Forecast")

@admin.route('/forecasts/view/<int:id>', methods=['GET', 'POST'])
@login_required
def view_forecast(id):
    """
    View a forecast
    """
    check_admin()

    add_forecast = False

    forecast = Forecast.query.get_or_404(id)
    form = ForecastForm(obj=forecast)
    if form.validate_on_submit():
        form.year=form.year.data
        form.month = form.month.data
        form.hc = form.hc.data
        form.month_hours = form.month_hours.data
        form.available = form.available.data
        form.holiday = form.holiday.data
        form.holiday_percentage = form.holiday_percentage.data
        form.comp_percentage =  form.comp_percentage.data
        form.illness_percentage =  form.illness_percentage.data
        form.others_percentage = form.others_percentage.data
        form.vacation_percentage = form.vacation_percentage.data
        form.overtime_percentage = form.overtime_percentage.data
        form.education_percentage = form.education_percentage.data

        form.agent_holiday_eight = form.agent_holiday_eight.data
        form.agent_holiday_ten  = form.agent_holiday_ten.data,
        form.holiday_hours = form.holiday_hours.data,
        form.compensation_hours = form.compensation_hours.data,
        form.illness_hours = form.illness_hours.data,
        form.others_hours = form.others_hours.data,
        form.education_hours = form.education_hours.data,
        form.normal_hours = form.normal_hours.data,
        form.overtime_hours = form.overtime_hours.data,
        form.agent_vacation_eight = form.agent_vacation_eight.data,
        form.agent_vacation_ten   = form.agent_vacation_ten.data,
        form.vacation_hours = form.vacation_hours.data,
        form.hc_vacation = form.hc_vacation.data,
        form.chargeable = form.chargeable.data,
        form.utilization = form.utilization.data
        db.session.add(forecast)
        db.session.commit()
        flash('You have modified forecast in db')

        # redirect to the roles page
        return redirect(url_for('admin.list_forecasts'))

    form.year.data = form.year
    form.month.data = form.month
    form.hc.data = form.hc
    form.month_hours.data = form.month_hours
    form.available.data = form.available
    form.holiday.data = form.holiday
    form.holiday_percentage.data = form.holiday_percentage
    form.comp_percentage.data =  form.comp_percentage
    form.illness_percentage.data =  form.illness_percentage
    form.others_percentage.data = form.others_percentage
    form.vacation_percentage.data = form.vacation_percentage
    form.overtime_percentage.data = form.overtime_percentage
    form.education_percentage.data = form.education_percentage

    form.agent_holiday_eight.data = form.agent_holiday_eight
    form.agent_holiday_ten.data  = form.agent_holiday_ten
    form.holiday_hours.data = form.holiday_hours
    form.compensation_hours.data = form.compensation_hours
    form.illness_hours.data = form.illness_hours
    form.others_hours.data = form.others_hours
    form.education_hours.data = form.education_hours
    form.normal_hours.data = form.normal_hours
    form.overtime_hours.data = form.overtime_hours
    form.agent_vacation_eight.data = form.agent_vacation_eight
    form.agent_vacation_ten.data   = form.agent_vacation_ten
    form.vacation_hours.data = form.vacation_hours
    form.hc_vacation.data = form.hc_vacation
    form.chargeable.data = form.chargeable
    form.utilization.data = form.utilization
    return render_template('admin/forecasts/forecast.html', add_forecast=add_forecast,
                           form=form, title="Modificar Expediente")


@admin.route('/forecasts/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_forecast(id):
    """
    Delete a forecast from the database
    """
    check_admin()

    forecast = Forecast.query.get_or_404(id)
    db.session.delete(forecast)
    db.session.commit()
    flash('You have deleted the forecast from the db.')

    # redirect to the roles page
    return redirect(url_for('admin.list_forecasts'))

    return render_template(title="Delete Forecast")


# Employee Views

@admin.route('/employees')
@login_required
def list_employees():
    """
    List all employees
    """
    check_admin()

    employees = Employee.query.all()
    return render_template('admin/employees/employees.html',
                           employees=employees, title='Employees')


@admin.route('/employees/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id):
    """
    Assign a role to an employee
    """
    check_admin()

    employee = Employee.query.get_or_404(id)

    # prevent admin from being assigned a department or role
    if employee.is_admin:
        abort(403)

    form = EmployeeAssignForm(obj=employee)
    if form.validate_on_submit():
        employee.department = form.department.data
        employee.role = form.role.data
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully assigned an engineer.')

        # redirect to the roles page
        return redirect(url_for('admin.list_employees'))

    return render_template('admin/employees/employee.html',
                           employee=employee, form=form,
                           title='Assign Employee')
