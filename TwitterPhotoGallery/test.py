from TwitterAPI import TwitterAPI

consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_secret_secret = ''

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_secret_secret)
def test():
    r = api.request('search/tweets', {'q':'#GoogleUdacityScholars', 'filter': 'hashtags'})
    #r = api.request('search/tweets', {'q':'#summer', 'filter': 'images'})
    
    photo = []
    for item in r:
        keys_in_entities = item.get('entities')
        keys_in_media = keys_in_entities.get('media')
        if type(keys_in_media) == list:
            val = keys_in_media[0].get('media_url')
            print(val)
            photo.append(val)
    return photo
