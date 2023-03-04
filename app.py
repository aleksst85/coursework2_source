from flask import Flask, render_template, send_from_directory
from config import POST_LIST, COMENT_LIST
from function import load_posts, find_id_post, find_post_coment, find_name_post
app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def start():
    posts = load_posts(POST_LIST)
    
    return render_template('index.html', posts=posts)



@app.route("/post/<int:id_post>")
def post(id_post):
    post = find_id_post(id_post, POST_LIST)
    comment = find_post_coment(id_post, COMENT_LIST)
    len_comment =f"Всего коментариев {len(comment)}"
    if post!=None:
        return render_template('post.html', post=post, comments=comment, len_comment = len_comment)
    else:
        return '<h1>Пост не найден</h1>'


@app.route('/user-feed/<string:name>')
def name_post(name):
    posts = find_name_post(name, POST_LIST)
    return render_template('user-feed.html', name=name)









@app.route("/img/<path:path>")
def static_dir(path):
    return send_from_directory("img", path)


app.run(debug=True)