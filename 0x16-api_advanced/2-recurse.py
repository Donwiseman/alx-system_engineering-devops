#!/usr/bin/python3
""" queries the Reddit API and returns a list containing the titles\
of all hot articles for a given subreddit. """

import requests


def recurse(subreddit, hot_list=[], tag="", count=0):
    """Queries the Reddit API to retrieve list of subreddit titles."""
    headers = {
        "User-Agent": "ubuntu:alx.APIadavncedProject:v1.0 \
(by /u/don-wiseman-1903)"
    }
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if count == 0:
        val = {
                "limit": 100
        }
    else:
        val = {
                "after": tag,
                "limit": 100,
                "count": count,
        }
    try:
        r = requests.get(api_url, params=val, headers=headers,
                         allow_redirects=False)
        r.raise_for_status()
        r_j = r.json()
        if r_j:
            children = r_j.get('data').get('children')
            for index, data in enumerate(children):
                hot_list.append(data['data']['title'])
                seen = index
            count += seen
            tag = r_j.get('data').get('after')
            if (tag is not None):
                recurse(subreddit, hot_list, tag, count)
            return hot_list
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None
    except ValueError as e:
        return None


if __name__ == '__main__':
    mylist = []
    print(len(recurse('programming', mylist)))
    print(f"Titles in list is : {len(mylist)}")
