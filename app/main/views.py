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

    return render_template('index.html', title = title )   

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

    prodo=Pitch.query.filter_by(category="product").all()

   
    return render_template('product.html', prodo = prodo )

@main.route('/interview', methods = ['GET','POST'])

def interview():

    inter=Pitch.query.filter_by(category="interview")
   
    return render_template('interview.html')    



@main.route('/promotion', methods = ['GET','POST'])

def promotion():

    promo=Pitch.query.filter_by(category="promotion").all()
   
    return render_template('promotion.html', promo=promo)

@main.route('/pitch', methods = ['GET','POST'])

def pitch():

    pitches=Pitch.query.all()
   
    return render_template('pitch.html',pitches=pitches)
    

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