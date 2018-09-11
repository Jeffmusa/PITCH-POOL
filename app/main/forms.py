from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import Required


class PitchForm(FlaskForm):

    post = StringField('Your name',validators=[Required()])

    body = TextAreaField('Pitch')

    category = RadioField('Pick Category',
                          choices=[('product', 'product'),
                                ('interview', 'interview'),
                                   ('promotion', 'promotion')],
                          validators=[Required()])
   
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):

    comment = StringField('Your comment',validators=[Required()])

    
    
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')