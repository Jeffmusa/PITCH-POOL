from flask import render_template
from . import main
from .forms import PitchForm
# from ..models import Pitch



#views
@main.route('/')
def index():
    '''
    View root page function that returns index page and its data
    '''
    title = 'PITCH PERFECT'

    return render_template('index.html', title = title )   

@main.route('/pitch', methods = ['GET','POST'])
def new_pitch():
    # form = PitchForm()
    

    # if form.validate_on_submit():
    #     pitch = form.pitch.data
    #     pitch = Pitch(pitch)
    #     pitch.save_pitch()
    #     return redirect(url_for('movie',id = movie.id ))

    
    return render_template('pitch.html')    
