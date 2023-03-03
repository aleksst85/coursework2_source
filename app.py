from flask import Flask, render_template, send_from_directory
from config import POST_LIST
from function import load_posts
app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def start():
    posts = load_posts(POST_LIST)
    print(posts)
    return render_template('index.html', posts=posts)


@app.route("/img/<path:path>")
def static_dir(path):
    return send_from_directory("img", path)


app.run(debug=True)