from flask import Flask, render_template, send_from_directory
from config import POST_LIST
from function import load_posts, find_id_post
app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def start():
    posts = load_posts(POST_LIST)
    
    return render_template('index.html', posts=posts)



@app.route("/post/<int:id_post>")
def post(id_post):
    post = find_id_post(id_post, POST_LIST)
    if post!=None:
        return render_template('post.html', post=post)
    else:
        return '<h1>Пост не найден</h1>'









@app.route("/img/<path:path>")
def static_dir(path):
    return send_from_directory("img", path)


app.run(debug=True)