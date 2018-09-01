from models.db import db
class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    author = db.Column(db.String(100),nullable=False)
    url = db.Column(db.String(100),nullable=False)
    imgurl = db.Column(db.String(100),nullable=False)
    category = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)