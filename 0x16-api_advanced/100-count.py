#!/usr/bin/python3
""" Prints a count of given keywords from data taken fromm the reddit API """
import json
import pprint
import re
import requests

def printer(word_list, hot_list):
    """ Prints our results"""
    total = {}
    for word in word_list:
        total[word] = 0

    for title in hot_list:
        for word in word_list:
            total[word] = total[word] +\
             len(re.findall(r'(?:^| ){}(?:$| )'.format(word), title, re.I))

    total = {k: v for k, v in total.items() if v > 0}
    words = sorted(list(total.keys()))
    for word in sorted(words,
                       reverse=True, key=lambda k: total[k]):
        print("{}: {}".format(word, total[word]))


def count_words(subreddit, word_list, hot_list=[], after=None):
    """ Prints a count of given keywords from reddit API data"""
    url = 'https://www.reddit.com/'
    params = {'limit': 100}

    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return printer(word_list, hot_list)

    answer = requests.get(
            headers={'User-Agent': 'custom'},
            url="{}/r/{}/hot.json".format(url, subreddit),
            allow_redirects=False,
            params=params
    )

    if answer.status_code != 200:
        return None

    data = answer.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]

    return count_words(subreddit, word_list, hot_list, after)
