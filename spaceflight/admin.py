from django.contrib import admin

from spaceflight.models import Articles, Events, Launches

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'url', 'published_at']
