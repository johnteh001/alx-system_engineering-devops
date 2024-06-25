#!/usr/bin/python3
"""Top Ten Module"""

import requests
import json
import sys


def recurse(subreddit, hot_list=[], count=0, aft=None):
    """Function queries Reddit API

    Returns:
        number of subscribers to a given subreddit
    """
    headers = {'User-agent': 'test'}
    if count > 1 and aft is None:
        return (hot_list)
    if aft is None:
        url = "https://reddit.com/r/{}".format(subreddit)
        req = requests.get(url, headers=headers)
        if req.status_code == 200:
            url = "https://reddit.com/r/{}/hot.json?limit=100".format(
                    subreddit)
            hot_posts = requests.get(url, headers=headers)
            if hot_posts.json() is None:
                return None
            elif hot_posts.json().get("data") is None:
                return None
            list_hot_posts = hot_posts.json().get("data").get("children")
            if list_hot_posts is None or len(list_hot_posts) == 0:
                return None
            for post in list_hot_posts:
                hot_list.append(post.get("data").get("title"))
            aft = hot_posts.json().get("data").get("after")
            recurse(subreddit, hot_list, count + 1, aft)
        else:
            return None
    else:
        url = "https://reddit.com/r/{}/hot.json?after={}&limit=100".format(
            subreddit, aft)
        after_hot = requests.get(url, headers=headers)
        list_after_hot = after_hot.json().get("data").get("children")
        for post in list_after_hot:
            hot_list.append(post.get("data").get("title"))
        aft = after_hot.json().get("data").get("after")
        recurse(subreddit, hot_list, count + 1, aft)
    return (hot_list)
