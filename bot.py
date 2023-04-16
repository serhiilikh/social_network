import json
import random

import requests


base_url = f"http://0.0.0.0:8000/"
headers = {"Content-Type": "application/json"}

post_ids = []

with open("bot_config.json", "r") as fp:
    config = json.load(fp)
number_of_users = config["number_of_users"]
max_posts_per_user = config["max_posts_per_user"]
max_likes_per_user = config["max_likes_per_user"]

for user_number in range(number_of_users):
    r = requests.post(
        base_url + "users/",
        data=json.dumps(
            {
                "email": f"{user_number}@example.com",
                "username": f"user{user_number}",
                "password": "ABCdef1@",
            }
        ),
        headers=headers,
    )
    resp = requests.post(
        base_url + "auth/jwt/create/",
        data=json.dumps({"username": f"user{user_number}", "password": "ABCdef1@"}),
        headers=headers,
    )
    print(resp.json())
    token = resp.json()["access"]
    for post_number in range(random.randint(1, max_posts_per_user)):
        resp = requests.post(
            base_url + "posts/",
            data=json.dumps({"title": f"post {post_number}", "text": "string"}),
            headers=headers | {"Authorization": f"Bearer {token}"},
        )
        post_id = resp.json()["id"]
        post_ids.append(post_id)
        print(f"user {user_number} added new post, post id {post_id}")
    for _ in range(random.randint(1, max_likes_per_user)):
        post_to_upvote = random.choice(post_ids)
        print(f"user {user_number} likes post {post_to_upvote}")
        requests.post(
            base_url + f"posts/{post_to_upvote}/upvote/",
            headers=headers | {"Authorization": f"Bearer {token}"},
        )
