#!/usr/bin/python3
"""Subs Module"""

import requests
import json
import sys


def number_of_subscribers(subreddit):
    """Function queries Reddit API

    Returns:
        number of subscribers to a given subreddit
    """
    url = "https://reddit.com/r/{}".format(subreddit)
    headers = {'User-agent': 'test'}
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        url = "https://reddit.com/r/{}/about.json".format(subreddit)
        subscribers = requests.get(url, headers=headers)
        if subscribers.json() is None:
            return (0)
        if subscribers.json().get('data') is None:
            return (0)
        data = subscribers.json().get('data').get('subscribers')
        if data:
            return (data)
    else:
        return (0)
