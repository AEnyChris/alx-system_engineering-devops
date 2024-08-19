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

def count(split_title, word):
    count = 0
    for title in split_title:
        for token in title:
            if token == word:
                count += 1
    return count

def count_words(subreddit, word_list):
    word_list = [word.lower() for word in word_list]
    dup_words = list(set([w for w in word_list if word_list.count(w) > 1]))
    new_word_list = list(set(word_list))
    hot_list = recurse(subreddit)
    if hot_list:
        split_title = [t.lower().split() for t in hot_list]
        result = {}
        for word in sorted(new_word_list):
            word_count = count(split_title, word)
            if word_count != 0:
                if word not in dup_words:
                    result[word] = word_count
                else:
                    print(word_list.count(word))
                    result[word] = word_count * word_list.count(word)

        output = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
        for k, v in output.items():
            print(f"{k}: {v}")
