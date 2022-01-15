from django.core.management.base import BaseCommand, CommandError
from spaceflight.models import Articles, Launches, Events
import requests

class Command(BaseCommand):
    help = 'Get all articles to populate DB'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        response = requests.get('https://api.spaceflightnewsapi.net/v3/articles/')
        if response.status_code == 200:
            response_json = response.json()
            for article in response_json:
                if article['launches'] != []:
                    article_launches = article['launches']
                    for launch in article_launches:
                        launches = Launches.objects.create(
                            provider= launch['provider']
                        )
                else:
                    launches = None 

                if article['events'] != []:
                    article_events = article['events']
                    for events in article_events:
                        events = Events.objects.create(
                            provider= events['provider']
                        )
                else:
                    events = None
                Articles.objects.create(
                    title=article['title'],
                    url=article['url'],
                    image_url=article['imageUrl'],
                    news_site=article['newsSite'],
                    summary=article['summary'],
                    featured=article['featured'],
                    launches=launches,
                    events=events,
                    published_at=article['publishedAt']
                )