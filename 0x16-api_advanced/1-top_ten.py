#!/usr/bin/python3
""" Gets the top 10 current hot posts """
import requests
import json


def top_ten(subreddit):
    """ Returns the top 10 hot post a selected subreddit """
    url = 'https://www.reddit.com/'

    try:
        response = requests.get(
            headers={'user-agent': 'custom'},
            url="{}/r/{}/hot.json?limit=10".format(url, subreddit),
        )

        data = response.json()['data']
        for ite in data['children']:
            print(ite['data']['title'])

    except Exception:
        print(None)
