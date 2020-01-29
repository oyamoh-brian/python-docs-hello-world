from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <center><h1>This is an Azure Flask Web App on Azure</h1></center>
    
    """
