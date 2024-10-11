import datetime
from app import db
from app.users.models import Company


class Job(db.Model):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key = True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=True)
    job_title = db.Column(db.String(200), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    category = db.Column(db.Text, nullable=False)
    job_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    post_date = db.Column(db.DateTime, default = datetime.datetime.now(datetime.UTC).date())
    expire_date = db.Column(db.DateTime, nullable=False)
    application_link = db.Column(db.String(100), nullable=False)

    company = db.relationship('Company', backref=db.backref('job', lazy=True))

    def __str__(self):
        return f'{self.job_title} in {self.company_name} at {self.location}'