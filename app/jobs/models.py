from datetime import datetime
from app import db


class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key = True)
    job_title = db.Column(db.String(200), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    category = db.Column(db.Text(), nullable=False)
    job_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    requirements = db.Column(db.Text(), nullable=False)
    post_date = db.Column(db.DateTime(), default = datetime.utcnow())
    expire_date = db.Column(db.DateTime(), default = datetime.utcnow())
    application_link = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return f'{self.job_title} in {self.company_name} at {self.location}'