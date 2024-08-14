#!/usr/bin/python3
"""This script queries the Reddit API"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """function returns a title list of all hot posts"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-User-Agent"}
    payload = requests.get(url, allow_redirects=False,
                           headers=headers,
                           params={"after": after})
    if payload.status_code == 200:
        for item in payload.json()['data']['children']:
            hot_list.append(item['data']['title'])
        after = payload.json()['data']['after']
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
