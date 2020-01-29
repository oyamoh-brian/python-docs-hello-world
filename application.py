from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <center><h1>This is a Flask App on Azure</h1></center>
    
    """
