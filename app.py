from flask import Flask, render_template, send_from_directory, request
from config import POST_LIST, COMENT_LIST
from function import load_posts, find_id_post, find_post_coment, find_name_post, search_for_posts
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
    return render_template('user-feed.html', name=name, posts=posts)



@app.route('/user-feed', methods=["POST"])
def bokmark_insert():
    post_id = request.values.get('post_id')
    print(post_id)
    return '<script>document.location.href = document.referrer</script>'


@app.route('/search', methods=["POST"])
def search_posts():
    text_search = request.values.get('search_post_text')
    data_search = search_for_posts(text_search, POST_LIST)
    len_posts=len(data_search)
    return render_template('search.html', len_posts=len_posts, data_search=data_search )



@app.route("/img/<path:path>")
def static_dir(path):
    return send_from_directory("img", path)


app.run(debug=True)