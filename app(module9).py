# Import dependacies
from flask import Flask

# Define New Flask app instance
app = Flask(__name__)

# Create Flask Route
@app.route('/')

# Create new function
def hello_world():
    return 'Hello World'