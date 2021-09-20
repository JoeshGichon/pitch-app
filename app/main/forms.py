from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('pitch tittle',validators=[Required()])
    author = StringField("author",validators=[Required()])
    content = TextAreaField('pitch', validators=[Required()])
    
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    author = StringField("author",validators=[Required()])
    submit = SubmitField('Submit')
