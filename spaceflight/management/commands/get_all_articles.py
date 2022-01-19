from django.core.management.base import BaseCommand, CommandError
import requests

from spaceflight.models import Articles, Launches, Events


class Command(BaseCommand):
    help = 'Get all articles to populate DB'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        newest_article = Articles.objects.first()
        get_count_articles = requests.get('https://api.spaceflightnewsapi.net/v3/articles/count')
        count_articles = get_count_articles.json()
        path = f'https://api.spaceflightnewsapi.net/v3/articles/?_sort=id&id_gt={newest_article.ref_original_id}&_limit=100000'
        print("######################### Starting ################")
        response = requests.get(path)
        count = 0
        if response.status_code == 200:
            response_json = response.json()
            print(f'Total articles - {count_articles}')
            for article in response_json:
                count = count + 1
                print(f'Article {count} de {count_articles}')
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
                    published_at=article['publishedAt'],
                    ref_original_id=article['id']
                )