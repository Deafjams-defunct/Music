"""Fetch data from lastfm"""
import os
import requests

# lastfm dev details
LASTFM_API_URL = 'http://ws.audioscrobbler.com/2.0/'
LASTFM_API_KEY = os.environ['LASTFM_API_KEY']
LASTFM_SHARED_SECRET = os.environ['LASTFM_SHARED_SECRET']

def get(method, params=None):
    """Generic lastfm api request

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

    return requests.get(LASTFM_API_URL, params=params).json()


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
