#!/usr/bin/python3
"""
This script queries the Reddit API
and returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    try:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        payload = requests.get(url, allow_redirects=False)
        if payload.status_code != 200:
            return 0
        subs = payload.json()['data']['subscribers']
        return subs
    except Exception as e:
        return 0

