"""Fetch data from lastfm"""
import os
import requests
import ratelimit

# lastfm dev details
LASTFM_API_URL = 'http://ws.audioscrobbler.com/2.0/'
LASTFM_API_KEY = os.environ['LASTFM_API_KEY']
LASTFM_SHARED_SECRET = os.environ['LASTFM_SHARED_SECRET']

@ratelimit.rate_limited()
def get(method, params=None):
    """Generic lastfm api request. Rate limited to 1/sec

    Args:
        method (str): lastfm method to call
        params (dict): query parameters to send to lastfm method

    Returns:
        dict - json from lastfm api
    """
    params = params or {} # safe defaulting
    params.update({
        'format': 'json',
        'method': method,
        'api_key': LASTFM_API_KEY
    })

    response = requests.get(LASTFM_API_URL, params=params)
    response.raise_for_status()

    return response.json()



# User-based requests
def get_user_info(user):
    """Get lastfm info for a given lastfm user

    Args:
        user (str): a lastfm user name

    Returns:
        dict - lastfm api user data
    """
    return get('user.getinfo', params={'user': user})


def get_user_friends(user):
    """Get lastfm friends for a given lastfm user

    Args:
        user (str): a lastfm user name

    Returns:
        dict - lastfm api friend data
    """
    return get('user.getfriends', params={'user': user})


def get_user_weekly_artist_chart(user):
    """Get lastfm weekly artist chart for a given lastfm user

    Args:
        user (str): a lastfm user name

    Returns:
        dict - lastmf api weekly artist chart data
    """
    return get('user.getweeklyartistchart', params={'user': user})
