"""Load lastfm api data into neo4j"""
import py2neo

GRAPH = py2neo.Graph('bolt://neo4j:neo4j@localhost:7687')

def load_user_info(user):
    """Stores a lastfm user in neo4j

    Args:
        user (dict): neo4j friendly user data
    """
    if not GRAPH.find_one('User', property_key='name', property_value=user['name']):
        user_node = py2neo.Node('User', **user)
        GRAPH.create(user_node)


def load_user_friend(user, friend):
    """Stores a lastfm user's friend in neo4j

    Args:
        user (str): lastfm username
        friend (str): lastfm username
    """
    user_node = GRAPH.find_one('User', property_key='name', property_value=user)
    friend_node = GRAPH.find_one('User', property_key='name', property_value=friend)
    relationship = GRAPH.match_one(
        start_node=user_node,
        rel_type='FRIENDS',
        end_node=friend_node,
        bidirectional=True
    )

    if relationship is None:
        relationship = py2neo.Relationship(user_node, 'FRIENDS', friend_node)
        GRAPH.create(relationship)


def load_user_friends(user, friends):
    """Convenience method for loading many lastfm friends

    Args:
        user (str): lastfm username
        friends (list): list of lastfm user dicts
    """
    for friend in friends:
        load_user_info(friend)
        load_user_friend(user, friend['name'])
