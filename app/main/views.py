from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitches,Comments,User
from .forms import PitchForm,CommentForm,UpdateProfile
from .. import db
from flask_login import login_required

@main.route("/")
def index():
    title="Home"
    return render_template("index.html",title=title)

@main.route('/pitches', methods = ['GET','POST'])
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        content = form.content.data

        new_pitch = Pitches(title,author,content)

        new_pitch.save_pitches()
        

    pitchess = Pitches.get_pitches()

    title = "pitches"
    return render_template('pitches.html',title = title, pitch_form=form,pitchess=pitchess)

@main.route('/comments', methods = ['GET','POST'])
@login_required
def new_comment():
    form = CommentForm()

    if form.validate_on_submit():
        comment= form.comment.data
        author=form.author.data

        new_comment = Comments(comment,author)

        new_comment.save_comment()

    commentss = Comments.get_comments()

    title = "comments"
    return render_template('comments.html',title = title, comment_form=form,commentss=commentss)

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


