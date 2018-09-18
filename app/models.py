# from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from . import db

#
# @login_manager.user_loader
# def load_user(user_id):
#     return Coach.query.get(int(user_id))
#
# # class Coach(UserMixin, db.Model):
# #         __tablename__ = 'coaches'
# #         id = db.Column(db.Integer, primary_key=True)
# #         username = db.Column(db.String(255), index=True)
# #         email = db.Column(db.String(255), unique=True, index=True)
# #         bio = db.Column(db.String(255))
# #         profile_pic_pah = db.Column(db.String())
# #         pass_secure = db.tColumn(db.String(255))
# #         # creating relationship between coach and team,One Coach can have many teams
# #         team = db.relationship("Team", backref="coach", lazy="dynamic")
#
#
#
#     @property
#     def password(self):
#         raise AttributeError('This password is inaccessible')
#
#     @password.setter
#     def password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def verify_password(self, password):
#         return check_password_hash(self.password_hash, password)
#
#     def __repr__(self):
#         return f'User {self.username}'



class Team(db.Model):
    '''
    This is Post class that defines the tables in the post database
    '''

    post_list = []
    __tablename__ = 'team'

    id = db.Column(db.Integer,primary_key = True)
    actual_post = db.Column(db.String(255))
    vote_count = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    # post = db.relationship('Comment',backref = 'post',lazy = "dynamic")
