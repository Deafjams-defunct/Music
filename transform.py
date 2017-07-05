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


def transform_artist(artist):
    """Converts lastfm api artist data into neo4j friendly user data

    Args:
        artist (dict): lastfm api artist data

    Returns:
        dict - neo4j friendly artist data
    """
    artist.pop('@attr', None)

    return artist


def transform_user_weekly_artist_chart(chart):
    """Converts lastfm api weekly artist chart data into neo4j friendly
    weekly artist chart data

    Args:
        chart (dict): lastfm api weekly artist chart

    Returns:
        list - neo4j friendly artist data
    """
    chart = chart['weeklyartistchart']
    artists = []

    for artist in chart['artists']:
        artists.append(transform_artist(artist))

    return artists
