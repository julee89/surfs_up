from flask import Flask

app = Flask(__name__)

# Create first route
@app.route('/')
def hello_world():
    return 'Hello world'