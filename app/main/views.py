from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm
from flask_login import login_required
from .. import auth
from ..models import User
from .forms import UpdateProfile
from .. import db



#views
@main.route('/')
def index():
    '''
    View root page function that returns index page and its data
    '''
    title = 'PITCH PERFECT'

    return render_template('index.html', title = title )   

@main.route('/pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    # form = PitchForm()
    

    # if form.validate_on_submit():
    #     pitch = form.pitch.data
    #     pitch = Pitch(pitch)
    #     pitch.save_pitch()
    #     return redirect(url_for('movie',id = movie.id ))

    
    return render_template('pitch.html') 


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