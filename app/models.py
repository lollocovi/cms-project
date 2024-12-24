# Import necessary modules from Flask and SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy to interact with the database
db = SQLAlchemy()

# Define the Word model to represent words in the database
class Word(db.Model):
    """
    Word model representing a word in the database. This class defines the
    structure of the table in the SQLite database.
    """
    
    # Define the table name and columns
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the word entry
    word = db.Column(db.String(255), nullable=False)  # The word itself (in the first language)
    translation = db.Column(db.String(255), nullable=True)  # The translation of the word (in the second language)
    example = db.Column(db.String(255), nullable=True)  # Example sentence using the word
    
    def __repr__(self):
        """
        String representation of the Word object. This is useful for debugging
        and viewing the word details in the Flask shell or logs.
        """
        return f"<Word {self.word}>"
