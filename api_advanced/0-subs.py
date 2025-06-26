#!/usr/bin/python3

"""
Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:sub.count:v1.0 (by /u/yourusername)"
    }
    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=10
        )
        if response.status_code != 200:
            return 0
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except Exception:
        return
