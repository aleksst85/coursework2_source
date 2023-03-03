from config import POST_LIST
import json

def load_posts(posts):
    with open(posts, 'r', encoding='utf-8') as file:
        post_list = json.load(file)
    return post_list


print(load_posts(POST_LIST))