from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from flask_login import login_required, current_user
from .. import db
from ..models import Profile,User
from app import login_manager
from .forms import ProfileForm

@main.route('/')
def index():
    '''
    View page function that creates and returns the post titles on the index page
    '''

    form = ProfileForm()

    # if form.validate_on_submit():
    #     new_team = Team(actual_post=form.post.data, user_id=current_user.id)
    #     # new_team.save_post()
    #     # flash('Team has been created successfully')
    #     return redirect(url_for('.index'))
    # # team = Team.query.all()
    title= 'moringa'
    return render_template('index.html',title = title)





@main.route('/profile/add',methods = ['GET','POST'])
@login_required
def new_profile():
    '''
    View pitch function that returns the pitch page and data
    '''
    form = ProfileForm()


    if form.validate_on_submit():
        teamname = form.teamname.data
        vision = form.vision.data
        mission = form.mission.data
        members = form.members.data

        new_profile = Profile(teamname=teamname,vision=vision,mision=mission,members=members,user_id=current_user.id)
        new_profile.save_profile()
        flash('Profile has been created!', 'success')
        return redirect(url_for('main.home'))

    return render_template('profile/profile.html', profile_form = form)

@main.route('/user')
def profile():
    # usr = User.query.filter_by(username = uname).first()
    user= current_user

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)