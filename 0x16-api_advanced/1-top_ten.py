#!/usr/bin/python3
"""This script queries the Reddit API"""

import requests


def top_ten(subreddit):
    """function returns the title of top ten hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 10}
    headers = {"User-Agent": "My-User-Agent"}
    payload = requests.get(url, allow_redirects=False,
                           headers=headers,
                           params=params)
    if payload.status_code == 200:
        for item in payload.json()['data']['children']:
            print(item['data']['title'])
    else:
        print(None)
