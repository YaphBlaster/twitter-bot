try:
    import unzip_requirements
except ImportError:
    pass

import twitter
import os


def post_update(event, context):
    try:
        CONSUMER_KEY = os.environ['CONSUMER_KEY']
        CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
        ACCESS_TOKEN_KEY = os.environ['ACCESS_TOKEN_KEY']
        ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
        api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN_KEY,
                      access_token_secret=ACCESS_TOKEN_SECRET)

        image_link = event['body']['imageLink']
        status = api.PostUpdate("Created using http://www.prequelmemes.com/ #prequelmemes #starwars", media=image_link)

        response = {
            'statusCode': 200,
            'body': status.text
        }

    except Exception as e:
        response = {
            "statusCode": 500,
            "body": e
        }

    return response

if __name__ == "__main__":
    print(post_update({"imageLink":"https://i.imgur.com/UfuuHKx.jpg"}, ''))