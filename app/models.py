from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from . import db

@login_manager.user_loader
def load_coach(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_pah = db.Column(db.String())
    joined = db.Column(db.DateTime, default=datetime.utcnow)
    pass_secure = db.Column(db.String(255))
    profile = db.relationship("Profile", backref="user", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'


class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    teamname = db.Column(db.String)
    vision = db.Column(db.String(255))
    mission = db.Column(db.String())
    # category = db.Column(db.String(255))
    members = db.Column(db.String)
    # Foreign key from users table to link teams and profiles
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_profile(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_profiles(cls, id):
        profiles = Profile.query.filter_by(id=id).all()
        return profiles

    @classmethod
    def get_all_profiles(cls):
        profiles = Profile.query.order_by('-id').all()
        return profiles

    def __repr__(self):
        return f'Profile {self.teamname}'