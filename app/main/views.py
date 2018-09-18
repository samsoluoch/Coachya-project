from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from flask_login import login_required, current_user
# from .. import db
from ..models import Team
# from app import login_manager
from .forms import TeamForm

@main.route('/')
def index():
    '''
    View page function that creates and returns the post titles on the index page
    '''

    form = TeamForm()

    if form.validate_on_submit():
        new_team = Team(actual_post=form.post.data, user_id=current_user.id)
        # new_team.save_post()
        # flash('Team has been created successfully')
        return redirect(url_for('.index'))
    # team = Team.query.all()
    title= 'moringa'
    return render_template('index.html',title = title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

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