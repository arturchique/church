from datetime import datetime
import requests
from .models import News, PraySchedule
from django.core.exceptions import ObjectDoesNotExist
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


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
            "access_token": "fbe7c6ebfbe7c6ebfbe7c6eb23fb929815ffbe7fbe7c6eba428a43eb1564d2456216979",
            "v": "5.52"
        }
        data = requests.get(url="https://api.vk.com/method/wall.getById", params=params).json()['response'][0]

        title = data['text'].split('\n')[0]
        text = "\n".join(data['text'].split('\n')[1:])
        date_time = datetime.fromtimestamp(data['date'])
        image = NewsParser.get_photo(data['attachments']) or None

        # try:
        #     return News.objects.get(text=text)
        # except:
        news_obj = News(title=title, text=text, time=date_time, image=image)
        news_obj.save()
        return news_obj

    @staticmethod
    def load_last_post():
        params = {
            'owner_id': '-151364622',
            "access_token": "fbe7c6ebfbe7c6ebfbe7c6eb23fb929815ffbe7fbe7c6eba428a43eb1564d2456216979",
            "v": "5.52"
        }
        data = requests.get(url="https://api.vk.com/method/wall.get", params=params).json()

        if data['response']['items'][1]['date'] > data['response']['items'][0]['date']:
            last_post_id = data['response']['items'][1]['id']
        else:
            last_post_id = data['response']['items'][0]['id']

        post = f"-151364622_{last_post_id}"
        return NewsParser.load_concrete_post(post)


class ScheduleParser:
    """ Use GoogleAPI credentials to create parser """
    def __init__(self, creds):
        self.creds = creds

    def parse_schedule(self):
        spreadsheet_id = "1OrOS3T7Zxk8r93nZ3nmq5seBRmQobWJ-vfgLEaB4utk"

        credentials = ServiceAccountCredentials.from_json_keyfile_dict(
            self.creds,
            ["https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive"]
        )
        http_auth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build("sheets", "v4", http=http_auth)

        values = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range="B1:R3",
            majorDimension="COLUMNS"
        ).execute()
        return values

    def load_schedules(self):
        data = self.parse_schedule()['values']
        try:
            PraySchedule.objects.all().delete()
            for day in data:
                new_day = PraySchedule(date=day[0],
                                       day_name=day[1],
                                       schedule=day[2])
                new_day.save()

        except:
            raise KeyError
