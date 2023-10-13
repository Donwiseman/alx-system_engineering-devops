#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the first 10 hot\
posts listed for a given subreddit.  """

import requests


def top_ten(subreddit):
    """Queries the Reddit API to retrieve subreddit title details."""
    headers = {
        "User-Agent": "ubuntu:alx.APIadavncedProject:v1.0 \
(by /u/don-wiseman-1903)"
    }
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    val = {
        "limit": 15,
        "count": 0
    }
    try:
        r = requests.get(api_url, params=val, headers=headers,
                         allow_redirects=False)
        r.raise_for_status()
        r_j = r.json()
        if r_j:
            children = r_j.get('data').get('children')
            for i in range(0, 10):
                print(children[i]['data']['title'])
    except requests.exceptions.RequestException as e:
        print('None')
    except ValueError as e:
        print('None')
