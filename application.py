from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_aws():
    return "Hello, Azure Web Apps!"
