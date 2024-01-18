 
# Import necessary libraries
from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__)

# Define the routes
@app.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')

@app.route('/basics')
def basics():
    """Render the basics page."""
    return render_template('basics.html')

@app.route('/advanced')
def advanced():
    """Render the advanced page."""
    return render_template('advanced.html')

@app.route('/resources')
def resources():
    """Render the resources page."""
    return render_template('resources.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
