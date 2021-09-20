from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))

    pass_secure  = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Pitches(db.Model):

    all_pitches = []

    def __init__(self,title,author,content):
        self.title = title
        self.author = author
        self.content = content

    def save_pitches(self):
        Pitches.all_pitches.append(self)


    @classmethod
    def clear_pitches(cls):
        Pitches.all_pitches.clear()

    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100),nullable=False)
    author = db.Column(db.String(50),nullable=False,default="N/A")
    content = db.Column(db.Text,nullable=False)
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)

    # def save_pitch(self):
    #     db.session.add(self)
    #     db.session.commit()

    def save_pitches(self):
        Pitches.all_pitches.append(self)

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitches.query.filter_by(user_id=id).all()
        return pitches

    @classmethod
    def get_pitches(cls):
        response = []
        for pitch in cls.all_pitches:
            response.append(pitch)
        return response

    def __repr__(self):
        return f'Pitches {self.content,self.author,self.title}'

class Comments():

    all_comments = []

    def __init__(self,comment,author):
        self.comment = comment
        self.author = author

    def save_comment(self):
        Comments.all_comments.append(self)

    @classmethod
    def clear_comments(cls):
        Comments.all_comments.clear()

    @classmethod
    def get_comments(cls):
        response = []
        for comment in cls.all_comments:
            response.append(comment)
        return response

    def __repr__(self):
        return f'Comments {self.comment,self.author}'

