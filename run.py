from app import create_app

# Create the Flask application instance by calling the create_app function from the app package
app = create_app()

# This part will run the Flask application when this script is executed directly
if __name__ == "__main__":
    # Run the Flask app with debugging enabled and on a specific port (5001 in this case)
    app.run(debug=True, host='127.0.0.1', port=5001)
