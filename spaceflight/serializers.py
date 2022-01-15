from rest_framework import serializers
from spaceflight.models import Articles, Launches


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Articles
        fields= '__all__'


class LaunchesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Launches
        fields= '__all__'