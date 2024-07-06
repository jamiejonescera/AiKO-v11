from flask import Blueprint, render_template, request
from .ai_based_ruling import compute_scores

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/assessment', methods=['GET', 'POST'])
def assessment():
    if request.method == 'POST':
        answers = request.form
        slideshows = compute_scores(answers)
        return render_template('result.html', slideshows=slideshows)
    
    return render_template('assessment.html')
