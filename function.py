
import json

def load_posts(posts):
    with open(posts, 'r', encoding='utf-8') as file:
        post_list = json.load(file)
    for post in post_list:
        post['content_smail'] =post['content'][:post['content'].find('.',)+1]
    return post_list

