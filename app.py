from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, send_from_directory
import os


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("app.html", client_id=os.environ["CLIENT_ID"])


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == '__main__':
    app.run()
    