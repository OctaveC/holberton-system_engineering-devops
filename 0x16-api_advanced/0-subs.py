#!/usr/bin/python3
""" Queries the subscribers to a certain Subreddit """
import json
import requests


def number_of_subscribers(subreddit):
    """ Returns a the number of a subs a sub has """
    url = 'https://www.reddit.com/'

    try:
        response = requests.get(
            headers={'user-agent': 'custom'},
            url="{}/r/{}/about.json".format(url, subreddit),
        )
        data = response.json()['data']
        return data['subscribers']

    except Exception:
        return False
