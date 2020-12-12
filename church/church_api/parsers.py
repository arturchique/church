from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
import requests
from .models import News
from django.core.exceptions import ObjectDoesNotExist


class NewsParser:
    def __init__(self):
        self.post = ""
        self.club_id = "-151364622"

    @staticmethod
    def get_photo(attachments):
        for item in attachments:
            if item['type'] == 'photo':
                return item['photo']['photo_1280']
        return False

    @staticmethod
    def load_concrete_post(post):
        params = {
            "posts": post,
            "access_token": "982caca3b4f963c83d035a92221bc87f79ee708b90e64b4b045ddef97ed9e5b4dbd621cc9c7a1b253c90e",
            "v": "5.52"
        }
        data = requests.get(url="https://api.vk.com/method/wall.getById", params=params).json()['response'][0]

        title = data['text'].split('\n')[0]
        text = "\n".join(data['text'].split('\n')[1:])
        date_time = datetime.fromtimestamp(data['date'])
        image = NewsParser.get_photo(data['attachments']) or None

        print(title)
        print(text)
        print(date_time)
        print(image)
        try:
            return News.objects.get(text=text)
        except ObjectDoesNotExist:
            news_obj = News(title=title, text=text, time=date_time, image=image)
            news_obj.save()
            return news_obj

    @staticmethod
    def load_last_post():
        params = {
            'owner_id': '-151364622',
            "access_token": "982caca3b4f963c83d035a92221bc87f79ee708b90e64b4b045ddef97ed9e5b4dbd621cc9c7a1b253c90e",
            "v": "5.52"
        }
        data = requests.get(url="https://api.vk.com/method/wall.get", params=params).json()

        if data['response']['items'][1]['date'] > data['response']['items'][0]['date']:
            last_post_id = data['response']['items'][1]['id']
        else:
            last_post_id = data['response']['items'][0]['id']

        post = f"-151364622_{last_post_id}"
        return NewsParser.load_concrete_post(post)


# NewsParser.load_last_post()