"""Takes lastfm data and stores it in neo4j"""
import extract
import transform
import load

def main():
    """extract and load data"""
    user = extract.get_user_info('deafjams')
    user = transform.transform_user_info(user)
    load.load_user_info(user)


    friends = extract.get_user_friends('deafjams')
    friends = transform.transform_user_friends(friends)
    load.load_user_friends('Deafjams', friends)

if __name__ == '__main__':
    main()
