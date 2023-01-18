import json


def load_posts_in_json_file():
    with open('posts.json', encoding='utf-8') as file:
        return json.load(file)


def search_posts(search_key):
    posts = load_posts_in_json_file()
    result_url = []
    result_post = []
    for post in posts:
        if search_key in post["content"].lower():
            result_url.append(post["pic"])
            result_post.append(post["content"])
    return result_url, result_post


print(search_posts('утро'))