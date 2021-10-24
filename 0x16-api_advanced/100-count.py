#!/usr/bin/python3
""" Prints a count of given keywords from data taken fromm the reddit API """
import json
import requests


def count_words(subreddit, word_list, hot_list=[], after=""):
    """ Prints a count of given keywords from reddit API data"""
    url = 'https://www.reddit.com/'

    try:
        answer = requests.get(
            headers={'User-Agent': 'custom'},
            url="{}/r/{}/hot.json?after={}".format(url, subreddit, after),
            allow_redirects=False
        )

        if after is None:
            dict = {}
            for word in word_list:
                for hot in hot_list:
                    if word == hot:
                        if word not in dict:
                            dict[word] = 1
                        else:
                            dict[word] += 1
            for word in sorted(dict, key=dict.get, reverse=True):
                if dict[word]:
                    print('{}: {}'.format(word, dict[word]))
            return hot_list

        for ite in answer.json().get('data').get('children'):
            hot_list += ite.get('data').get('title').lower().split()

        after = answer.json().get('data').get('after')
        count_words(subreddit, word_list, hot_list, after)
        return hot_list

    except Exception:
        return None
