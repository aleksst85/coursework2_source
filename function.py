from config import POST_LIST, COMENT_LIST
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
    

def find_post_coment(id_post, file_comment):
    answer_list=[]
    with open(file_comment, 'r', encoding='utf-8') as file:
        comment_list = json.load(file)
    for coment in comment_list:
        if coment['post_id'] == id_post:
            answer_list.append(coment)
    return answer_list


def find_name_post(name, file_post):
    data = load_posts(file_post)
    poster_list=[]
    for post in data:
        if post['poster_name'] == name:
            poster_list.append(post)
    return poster_list


def search_for_posts(query, file_post): 
    data = load_posts(file_post) 
    post_searhc_list=[]  
    for post in data:   
        if query.lower() in post['content'].lower():
            if len(post_searhc_list)<11:
                post_searhc_list.append(post)
            else:
                break
    return post_searhc_list








