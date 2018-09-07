from flask import render_template
from . import main



#views
@main.route('/')
def index():
    '''
    View root page function that returns index page and its data
    '''
    title = 'PITCH PERFECT'

    return render_template('index.html', title = title )   
