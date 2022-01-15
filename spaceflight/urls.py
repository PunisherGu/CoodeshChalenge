from django.urls import path, include
from rest_framework import routers

from spaceflight.views import HomeView, ArticlesView


router = routers.DefaultRouter()
router.register('articles', ArticlesView, basename='articles')

urlpatterns = [
   path('', HomeView.as_view(), name='home'),
   path('', include(router.urls)),
]
