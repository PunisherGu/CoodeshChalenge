from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from spaceflight.models import Articles
from spaceflight.serializers import ArticlesSerializer


class HomeView(generics.GenericAPIView):
    def get(self, request):
        return Response(
           {'Success': "Back-end Challenge 2021 🏅 - Space Flight News"}, 
           status=status.HTTP_200_OK
        )


class ArticlesView(viewsets.ModelViewSet):
    serializer_class = ArticlesSerializer

    def get_queryset(self):
        return Articles.objects.all()