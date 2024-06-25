#!/usr/bin/python3
"""Top Ten Module"""

import requests
import json
import sys


def top_ten(subreddit):
    """Function queries Reddit API

    Returns:
        number of subscribers to a given subreddit
    """
    url = "https://reddit.com/r/{}".format(subreddit)
    headers = {'User-agent': 'test'}
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        url = "https://reddit.com/r/{}/hot.json?limit=10".format(subreddit)
        hot_posts = requests.get(url, headers=headers)
        if hot_posts.json() is None:
            print(None)
            return
        elif hot_posts.json().get("data") is None:
            print(None)
            return
        list_hot_posts = list(hot_posts.json().get("data").get("children"))
        if list_hot_posts is None:
            print(None)
            return
        for post in list_hot_posts:
            print(post.get("data").get("title"))
    else:
        print(None)
