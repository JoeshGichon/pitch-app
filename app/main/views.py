from flask import render_template
from . import main
from ..models import Pitches,Comments
from .forms import PitchForm,CommentForm
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

