from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])

    review = TextAreaField('Comment pitch')
    submit = SubmitField('Submit')