from django.db import models
import uuid


class MyUUIDModel(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Launches(MyUUIDModel):
    provider = models.CharField(
        max_length=150
    )

    def __str__(self):
        return self.provider


class Events(MyUUIDModel):
    provider = models.CharField(
        max_length=150
    )

    def __str__(self):
        return self.provider


class Articles(models.Model):
    featured = models.BooleanField(default=False)
    title = models.CharField(
        max_length=350
    )
    url = models.URLField(
        max_length=250
    )
    image_url = models.URLField(
        max_length=250
    )
    news_site = models.CharField(
        max_length=60
    )
    summary = models.TextField()
    published_at = models.CharField(
        max_length=40
    )
    launches = models.ForeignKey(
        Launches,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    events = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']