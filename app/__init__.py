# Import necessary modules and functions
from flask import Flask
from .routes import bp as routes_bp  # Import the routes blueprint
from .models import db  # Import the database instance
import requests  # For loading initial data from the URL
from .models import Word, db  # Import the Word model and db instance

def create_app():
    """
    Create and configure the Flask application.
    
    This function initializes the Flask app, sets up the database configuration,
    registers the routes blueprint, and creates the necessary tables in the database.
    """
    
    # Initialize the Flask app
    app = Flask(__name__)

    # Configure the SQLite database URI and disable modification tracking
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the database with the app
    db.init_app(app)
    
    # Register the blueprint for handling routes
    app.register_blueprint(routes_bp)
    
    # Create all the database tables
    with app.app_context():
        db.create_all()
    
    return app

def load_initial_data():
    """
    Load initial data from a remote JSON file and populate the database.
    
    This function fetches data from a provided URL, processes it, and saves the
    data into the local SQLite database.
    """
    # URL to the JSON file with the words data
    url = "https://pecto-content-f2egcwgbcvbkbye6.z03.azurefd.net/language-data/language-data/russian-finnish/cards/curated_platform_cards/sm1_new_kap1.json"
    
    # Fetch the JSON data from the URL
    response = requests.get(url)
    
    # Parse the JSON response
    data = response.json()
    
    # Loop through each entry in the fetched data and add it to the database
    for entry in data:
        # Check if 'wordFirstLang' exists, and use it as the word
        word = entry.get('wordFirstLang', '')  # Default to an empty string if the key doesn't exist
        translation = entry.get('wordSecondLang', '')  # Default to an empty string
        example = entry.get('sentenceFirstLang', '')  # Default to an empty string
        
        # Create a new Word object with the fetched data
        new_word = Word(word=word, translation=translation, example=example)
        
        # Add the new word to the session
        db.session.add(new_word)
    
    # Commit the session to save changes to the database
    db.session.commit()
