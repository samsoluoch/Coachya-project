from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from flask_login import login_required, current_user
from .. import db
from ..models import Coach
from app import login_manager
# from .forms import PostForm,CommentsForm

@main.route('/',methods=['GET','POST'])
def index():
    '''
    View page function that creates and returns the post titles on the index page
    '''
    # form = PostForm()

    # if form.validate_on_submit():
    #     new_post = Post(actual_post=form.post.data,category=form.category.data, user_id=current_user.id)
    #     new_post.save_post()
    #     flash('Post has been created successfully')
    #     return redirect(url_for('.index'))
    # post = Post.query.all()
    #
    # General = Post.query.filter_by(category='General')
    title=title

    return render_template('index.html',title = 'new_post',form=form)