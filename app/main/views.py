from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm
from flask_login import login_required, current_user
from .. import auth
from ..models import User,Pitch
from .forms import UpdateProfile
from .. import db,photos



#views
@main.route('/')
def index():
    '''
    View root page function that returns index page and its data
    '''
    title = 'PITCH PERFECT'

    index=Pitch.query.all()

    return render_template('index.html', title = title, index = index )   

@main.route('/new_pitch', methods = ['GET','POST'])
@login_required
def new_pitch():   
    form = PitchForm() 
    if form.validate_on_submit():
        pitch = Pitch(post=form.post.data,body=form.body.data,category=form.category.data)
        pitch.save_pitch()
        return redirect(url_for('main.pitch'))
    return render_template('new_pitch.html',form=form) 

@main.route('/product', methods = ['GET','POST'])

def product():

    product_pitches=Pitch.query.filter_by(category="product")

    

    return render_template('product.html', product_pitches = product_pitches )

@main.route('/interview', methods = ['GET','POST'])

def interview():

    interview_pitches=Pitch.query.filter_by(category="interview")
   
    return render_template('interview.html', interview_pitches = interview_pitches)    



@main.route('/promotion', methods = ['GET','POST'])

def promotion():

    promotion_pitches=Pitch.query.filter_by(category="promotion")
   
    return render_template('promotion.html', promotion_pitches = promotion_pitches)

@main.route('/pitch', methods = ['GET','POST'])

def pitch():

    pitches_interview=Pitch.query.filter_by(category="pitch")
   
    return render_template('pitch.html',pitches_interview=pitches_interview)
    

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



@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))