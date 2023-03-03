from config import POST_LIST
import json

def load_posts(posts):
    with open(posts, 'r', encoding='utf-8') as file:
        post_list = json.load(file)
    for post in post_list:
        post['content_smail'] =post['content'][:post['content'].find('.',)+1]
    return post_list


def find_id_post(id_post, file_post):
    data = load_posts(file_post)
    for post in data:
        if post['pk'] == id_post:
            return post
    else:
        return None
       






