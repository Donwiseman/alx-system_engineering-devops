#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API to retrieve subreddit details."""
    headers = {
        "User-Agent": "ubuntu:alx.APIadavncedProject:v1.0 \
(by /u/don-wiseman-1903)"
    }
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    val = {
        "limit": 50,
        "count": 0
    }
    try:
        r = requests.get(api_url, params=val, headers=headers,
                         allow_redirects=False)
        r.raise_for_status()
        r_j = r.json()
        if r_j:
            return r_j['data']['subscribers']
        return 0
    except requests.exceptions.RequestException as e:
        return 0
    except ValueError as e:
        return 0
