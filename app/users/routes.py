from flask import redirect, request, flash, Blueprint, session, url_for, render_template
from .models import Company
from app import db
from app.jobs.models import Job
import datetime


user_bp = Blueprint('user_bp', __name__, url_prefix='/auth')

@user_bp.route('/company-login', methods=['GET', 'POST'], strict_slashes=False)
def company_login():
    ''' Login a user '''
    if request.method == 'POST':
        # Get form data
        email = request.form.get('email')
        password = request.form.get('password')

        # Query for the company based on the email
        company = Company.query.filter_by(email=email).first()

        # Ensure company exists and the password is correct
        if company and company.check_password(password):
            session['company_id'] = company.id
            flash('Logged in successfully', 'success')
            return redirect(url_for('user_bp.company_dashboard'))
        else:
            flash('Invalid credentials', 'danger')
    
    return render_template('company_login.html')


@user_bp.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def company_register():
    '''Register a company'''
    if request.method == 'POST':
        # Get the data from the form
        data = request.form
        email = data.get('email')
        password = data.get('password')

        # Ensure email and password are provided
        if not email or not password:
            flash('Email and password are required', 'warning')
            return redirect(url_for('user_bp.company_register'))

        # Check if the email already exists
        if Company.query.filter_by(email=email).first():
            flash('Email is already registered. Please sign in or use another email.', 'danger')
            return redirect(url_for('user_bp.company_register', email=email))
        
        try:
            # Register the new company
            company = Company(email=email)
            company.generate_password(password)
            
            # Add the company to the database
            db.session.add(company)
            db.session.commit()

            # Store the company ID in the session
            session['company_id'] = company.id

            # Redirect to the company dashboard after successful registration
            return redirect(url_for('user_bp.company_dashboard'))
        
        except Exception as e:
            # Handle any errors during registration
            flash(f'An error occurred: {str(e)}', 'danger')
            db.session.rollback()
            return redirect(url_for('user_bp.company_register'))

    # Render the registration page
    return render_template('company_register.html')



@user_bp.route('/company-dashboard', methods=['GET'], strict_slashes=False)
def company_dashboard():
    # Ensure the company is logged-in
    if 'company_id' not in session:
        flash('Please log in to access your dashboard', 'warning')
        return redirect(url_for('user_bp.company_login'))
    
    # Get the jobs posted by the user company
    company_id = session['company_id']
    jobs = Job.query.filter_by(company_id=company_id).all()
    today_date = datetime.datetime.now(datetime.UTC).date() # get today date
    # Initialize counter
  
    active_count = 0
    expired_count = 0
    if jobs:
        total_list = len(jobs)
        for job in jobs:
            if job.expire_date >= today_date:
                active_count += 1
                active_job = job
            else:
                expired_count += 1
                expired_job = job
    else:
        active_count = 0
        active_job = 0
        expired_count = 0
        expired_job = 0
        total_list = 0

    
    context = {
        'active_job': active_job,
        'expired_job': expired_job,
        'active_count': active_count,
        'expire_count': expired_count,
        'total_list': total_list,
    }
    return render_template('company_dashboard.html', context=context)

@user_bp.route('/logout', methods=['GET'], strict_slashes=False)
def logout():
    session.clear()
    flash('Successfully Logout')
    return redirect(url_for('user_bp.company_login'))