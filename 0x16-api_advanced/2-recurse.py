#!/usr/bin/python3
""" Gets the top 10 current hot posts, recursively """
import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Returns the top 10 hot post a selected subreddit, recursively """
    url = 'https://www.reddit.com/'

    try:
        if after is None:
            return

        answer = requests.get(
            headers={'user-agent': 'custom'},
            url="{}/r/{}/hot.json".format(url, subreddit),
            params={'after': after}
        )

        data = answer.json()['data']
        after = data['after']

        for ite in data['children']:
            hot_list.append(ite['data']['title'])
        recurse(subreddit, hot_list, after)
        return hot_list

    except Exception:
        return None
