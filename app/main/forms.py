from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.fields.core import DateField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('pitch tittle',validators=[Required()])
    author = StringField("author",validators=[Required()])
    content = TextAreaField('pitch', validators=[Required()])
    date_posted = DateField("Date posted",validators=[Required()])
    
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')
