from flask import Flask, render_template, send_from_directory
from config import POST_LIST
app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def start():
    return render_template('index.html')


@app.route("/img/<path:path>")
def static_dir(path):
    return send_from_directory("img", path)


app.run(debug=True)