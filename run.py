# Import the create_app function from the app package to initialize the Flask app
from app import create_app

# Create the Flask application instance using the create_app function
app = create_app()

# Run the application with debug mode enabled, which is useful for development
if __name__ == "__main__":
    app.run(debug=True)
