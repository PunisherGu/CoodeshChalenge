from asyncio import events
from django.urls import reverse
from faker import Faker
from rest_framework.test import APITestCase
from rest_framework import status

from spaceflight.models import Articles
from spaceflight.serializers import ArticlesSerializer


class ArticlesTestCase(APITestCase):

    def setUp(self):
        fake = Faker()
        self.list_url = reverse('articles-list')
        self.article = Articles(
            title='Coodesh satellite in orbit',
            featured=True,
            url=fake.url(),
            image_url=fake.image_url(),
            news_site='Coodesh',
            summary=fake.paragraph(nb_sentences=2),
            published_at="2022-01-14T12:00:37.000Z",
            launches=None,
            events=None,

        )
        self.serializer = ArticlesSerializer(instance=self.article)

    
    def test_get_home_should_return_200(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_verify_serializer_data(self):
        data = self.serializer.data
        self.assertEqual(data['title'], self.article.title)
        self.assertEqual(data['featured'], self.article.featured)
        self.assertEqual(data['url'], self.article.url)
        self.assertEqual(data['image_url'], self.article.image_url)
        self.assertEqual(data['news_site'], self.article.news_site)
        self.assertEqual(data['summary'], self.article.summary)
        self.assertEqual(data['published_at'], self.article.published_at)

    def test_create_new_article(self):
        fake = Faker()
        data={
            'title': 'Coodesh Roks',
            'featured':True,
            'url':fake.url(),
            'image_url':fake.image_url(),
            'news_site':'Coodesh',
            'summary':fake.paragraph(nb_sentences=2),
            'published_at':"2022-01-14T12:00:37.000Z",
        }
        response = self.client.post(path=self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Articles.objects.count(), 1)

    def test_get_article_by_id(self):
        fake = Faker()
        article = Articles.objects.create(
            title='Coodesh satellite in orbit',
            featured=True,
            url=fake.url(),
            image_url=fake.image_url(),
            news_site='Coodesh',
            summary=fake.paragraph(nb_sentences=2),
            published_at="2022-01-14T12:00:37.000Z",
            launches=None,
            events=None,  
        )
        url = reverse('articles-detail', kwargs={'pk': article.id})
        response = self.client.get(url)
        self.assertEqual(response.json()['id'], article.id)
        self.assertEqual(response.json()['title'], article.title)

    def test_delete_article_by_id(self):
        fake = Faker()
        article = Articles.objects.create(
            title='Coodesh satellite in orbit',
            featured=True,
            url=fake.url(),
            image_url=fake.image_url(),
            news_site='Coodesh',
            summary=fake.paragraph(nb_sentences=2),
            published_at="2022-01-14T12:00:37.000Z",
            launches=None,
            events=None,  
        )
        self.assertEqual(Articles.objects.count(), 1)
        url = reverse('articles-detail', kwargs={'pk': article.id})
        self.client.delete(url)
        self.assertEqual(Articles.objects.count(), 0)


    def test_update_article_with_put(self):
        fake = Faker()
        article = Articles.objects.create(
            title='Coodesh satellite in orbit',
            featured=True,
            url=fake.url(),
            image_url=fake.image_url(),
            news_site='Coodesh',
            summary=fake.paragraph(nb_sentences=2),
            published_at="2022-01-14T12:00:37.000Z",
            launches=None,
            events=None,  
        )

        new_title='We Roks'
        new_url=fake.url()
        new_image_url=fake.image_url()
        new_news_site='Django Docs'
        new_summary=fake.paragraph(nb_sentences=2)
        new_published_at="2022-02-14T12:00:37.000Z"

        put_data={
            'title':new_title,
            'url':new_url,
            'image_url':new_image_url,
            'news_site':new_news_site,
            'summary':new_summary,
            'published_at':new_published_at,
        }
        url = reverse('articles-detail', kwargs={'pk': article.id})
        self.client.put(url, data=put_data)
        article = Articles.objects.get(id=article.id)
        self.assertEqual(article.title, new_title)
        self.assertEqual(article.url, new_url)
        self.assertEqual(article.image_url, new_image_url)
        self.assertEqual(article.news_site, new_news_site)
        self.assertEqual(article.summary, new_summary)
        self.assertEqual(article.published_at, new_published_at)