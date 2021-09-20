from flask import render_template
from . import main
from ..models import Pitches,Comments
from .forms import PitchForm,CommentForm

# from flask_login import login_required

@main.route("/")
# @login_required
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
        date_posted = form.date_posted.data
        new_pitch = Pitches(title,author,content,date_posted,)
        new_pitch.save_pitch()


    title = "pitches"
    return render_template('pitches.html',title = title, pitch_form=form)

@main.route('/comments', methods = ['GET','POST'])
def new_comment():
    form = CommentForm()

    if form.validate_on_submit():
        comment= form.comment.data
        new_comment = Comments(comment)
        new_comment.save_pitch()

    title = "comments"
    return render_template('comments.html',title = title, comment_form=form)

