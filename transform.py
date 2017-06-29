"""Transform lastfm api data into neo4j friendly data"""

def transform_user_info(user):
    """Converts lastfm api user data into neo4j friendly user data

    Args:
        user (dict): lastfm api user data

    Returns:
        dict - neo4j friendly user data
    """
    if 'user' in user:
        user = user['user']

    user['image'] = [element['#text'] for element in user['image']]
    user['registered'] = user['registered']['unixtime']
    user['playcount'] = int(user['playcount'])
    user['playlists'] = int(user['playlists'])
    user['registered'] = int(user['registered'])

    return user


def transform_user_friends(friends):
    """Converts lastfm api friends data into neo4j friendly friends data

    Args:
        friends (dict): lastfm api friends data

    Returns:
        dict - neo4j friendly friends data
    """
    friends = friends['friends']['user']
    return [transform_user_info(friend) for friend in friends]
