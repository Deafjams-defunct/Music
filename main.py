"""Takes lastfm data and stores it in neo4j"""
import extract
import transform
import load

def crawl_friends(user, ignore=None):
    """Recursively crawl lastfm friends

    Args:
        user (str): lastfm user to crawl for friends
    """
    ignore = ignore or [] # safe default

    user = extract.get_user_info(user)
    user = transform.transform_user_info(user)
    load.load_user_info(user)
    ignore.append(user['name'])

    friends = extract.get_user_friends(user['name'])
    friends = transform.transform_user_friends(friends)
    load.load_friendships(user['name'], friends)

    for friend in friends:
        if friend['name'] not in ignore:
            crawl_friends(friend['name'], ignore)


def fetch_my_friends():
    """Fetch my profile and my lastfm friends, load into database"""
    user = extract.get_user_info('deafjams')
    user = transform.transform_user_info(user)
    load.load_user_info(user)

    friends = extract.get_user_friends('deafjams')
    friends = transform.transform_user_friends(friends)
    load.load_user_friends('Deafjams', friends)


def main():
    """extract and load data"""
    crawl_friends('deafjams')


if __name__ == '__main__':
    main()
