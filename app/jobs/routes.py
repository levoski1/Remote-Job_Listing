#!/usr/bin/env python

from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash
from app.jobs.models import Job
from datetime import datetime
from app import db

jobs_bp = Blueprint('jobs_bp', __name__, url_prefix='/jobs') 

@jobs_bp.route('/all_jobs', strict_slashes=False, methods=['GET'])
def get_jobs():
    query = Job.query

    #filter by job type
    job_type  = request.args.get('job_type')
    if job_type:
        query = query.filter(Job.job_type == job_type)

    # filter by location
    location = request.args.get('location')
    if location:
        query = query.filter(Job.location == location)

    # filter by category
    category = request.args.get('category')
    if category:
        query = query.filter(Job.category == category)

    jobs = query.all() # returns a list instances of Job class
    All_jobs = []
    for job in jobs:
        All_jobs.append({
            'job_title': job.job_title,
            'company_name': job.company_name,
            'location': job.location,
            'job_type': job.job_type,
            'category': job.category,
            'description': job.description,
            'requirements': job.requirements,
            'post_date': job.post_date,
            'expire_date': job.expire_date,
            'application_link': job.application_link
        })
    other_info = {'Total': len(All_jobs)}
    All_jobs.append(other_info)
    return jsonify(All_jobs)
    
@jobs_bp.route('/post-jobs', methods=['GET', 'POST'], strict_slashes=False)
def post_jobs():
    if request.method == 'POST':
        data = request.form
        
        # Convert the string expire_date to a date object
        expire_date = datetime.strptime(data.get('expire_date'), '%Y-%m-%d').date()

        # Validate form data
        if not all([data.get('job_title'), data.get('company_name'), data.get('location'),
                    data.get('job_type'), data.get('category'), data.get('description'),
                    data.get('requirements'), data.get('expire_date'), data.get('application_link')]):
            flash('Please fill in all required fields', 'error')
            return redirect(url_for('jobs_bp.post_jobs'))
        
        new_job = Job(
            job_title=data.get('job_title'),
            company_name=data.get('company_name'),
            location=data.get('location'),
            job_type=data.get('job_type'),
            category=data.get('category'),
            description=data.get('description'),
            requirements=data.get('requirements'),
            expire_date=expire_date,  # Make sure this field exists
            application_link=data.get('application_link')
        )
        
        try:
            db.session.add(new_job)
            db.session.commit()
            flash('Job successfully added!', 'success')
            return redirect(url_for('jobs_bp.get_jobs'))
        except Exception as e:
            db.session.rollback()  # Rollback the transaction
            flash(f'Error: {str(e)}', 'error')
            return redirect(url_for('jobs_bp.post_jobs'))
    
    return render_template('job_post.html')

