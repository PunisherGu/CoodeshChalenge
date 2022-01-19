from celery import shared_task, task
from celery.utils.log import get_task_logger
import requests


from spaceflight.models import Articles, Events, Launches


@task(name='articles') 
def get_new_articles():
    newest_article = Articles.objects.first()
    path = f'https://api.spaceflightnewsapi.net/v3/articles/?_sort=id&id_gt={newest_article.ref_original_id}&_limit=100000'
    print(path)
    response = requests.get(path)
    count = 0
    if response.status_code == 200:
        response_json = response.json()
        for article in response_json:
            count = count + 1
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