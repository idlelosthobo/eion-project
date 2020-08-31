from django.core.management.base import BaseCommand, CommandError
from app.news import models
import requests


class Command(BaseCommand):
    help = 'Get news information from news list'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        nyt_api_key = 'fVcqRCgZMed4C2m8GaQeNKH79PlAQSER'

        url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

        querystring = {
            "begin_date": "20200101",
            "end_date": "20200131",
            "q": "Taylor Swift",
            'page': 0,
            "api-key": nyt_api_key,
        }

        json = requests.request("GET", url, params=querystring).json()
        for article in json['response']['docs']:
            self.stdout.write(self.style.SUCCESS(str(article['headline']['main'])))
