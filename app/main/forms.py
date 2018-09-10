from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class PitchForm(FlaskForm):

    post = StringField('Your name',validators=[Required()])

    body = TextAreaField('Pitch')

    category = StringField('Your category',validators=[Required()])
   
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    comment = StringField('Your comment',validators=[Required()])

    
    
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')