#!/usr/bin/env python

from flask import Blueprint, jsonify, request
from app.jobs.models import Job
from app import db

jobs_bp = Blueprint('jobs_bp', __name__, url_prefix='/jobs') 

@jobs_bp.route('/all_jobs', strict_slashes=False, methods=['GET'])
def get_jobs():
    jobs = Job.query.all() # returns a list instances of Job class
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
        return jsonify(All_jobs)
    
# route to add new job
@jobs_bp.route('/add_jobs',methods=['POST'],strict_slashes=False)
def add_jobs():
    data = request.get_json()
    
    new_jobs = Job(
        job_title = data.get('job_title'),
        company_name = data.get('company_name'),
        location = data.get('location'),
        job_type = data.get('job_type'),
        category = data.get('category'),
        description = data.get('description'),
        requirements = data.get('requirements'),
        post_date = data.get('post_date'),
        expire_date = data.get('expire_date'),
        application_link = data.get('application_link')
    )
    db.session.add(new_jobs)
    db.session.commit()
    
    return jsonify({"message": "Job added successfully!"}), 201
