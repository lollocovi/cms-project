# Importing necessary modules from Flask and models
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Word, db

# Creating a Blueprint for 'routes', which groups related views together
bp = Blueprint('routes', __name__)

# Route to display the words and allow searching through them
@bp.route('/index', methods=['GET'])
def index():
    # Get the search query from the URL parameters (default to an empty string if not provided)
    search = request.args.get('search', '')
    
    # Query the 'Word' model to filter words containing the search term (case-insensitive)
    # Paginate the results to display 10 words per page
    words = Word.query.filter(Word.word.contains(search)).paginate(per_page=10)
    
    # Render the 'index.html' template and pass the 'words' object for display
    return render_template('index.html', words=words)

# Route to handle editing a word based on its ID
@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # Retrieve the word by its ID from the 'Word' model
    word = Word.query.get(id)
    
    # If the form is submitted (POST request), update the word with new data
    if request.method == 'POST':
        # Update the word's properties from the form data
        word.word = request.form['word']
        word.translation = request.form['translation']
        word.example = request.form['example']
        
        # Commit the changes to the database
        db.session.commit()
        
        # Redirect the user to the 'index' route after the update is complete
        return redirect(url_for('routes.index'))
    
    # If it's a GET request, render the 'edit.html' template with the word's details
    return render_template('edit.html', word=word)
