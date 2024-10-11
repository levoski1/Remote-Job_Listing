from app import db
from werkzeug.security import check_password_hash, generate_password_hash

class Company(db.Model):
    __tablename__ = 'company'
    id  = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100))
    

    def generate_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self) -> str:
        return f'{self.email} == {self.password_hash}'