from flask import abort, render_template
from flask_login import current_user, login_required
from .. import db
from ..models import Forecast, Employee
from . import home
import arrow
import datetime

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/admin_dashboard.html', title="Dashboard")


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    
    employees = Employee.query.all()

    
    
    

    return render_template('home/admin_dashboard.html',employees=employees, title="Dashboard")
