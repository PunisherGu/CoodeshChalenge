# Generated by Django 3.2.11 on 2022-01-15 19:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUUIDModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('myuuidmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='spaceflight.myuuidmodel')),
                ('provider', models.CharField(max_length=150)),
            ],
            bases=('spaceflight.myuuidmodel',),
        ),
        migrations.CreateModel(
            name='Launches',
            fields=[
                ('myuuidmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='spaceflight.myuuidmodel')),
                ('provider', models.CharField(max_length=150)),
            ],
            bases=('spaceflight.myuuidmodel',),
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=350)),
                ('url', models.URLField(max_length=250)),
                ('image_url', models.URLField(max_length=250)),
                ('news_site', models.CharField(max_length=60)),
                ('summary', models.TextField()),
                ('published_at', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('events', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spaceflight.events')),
                ('launches', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spaceflight.launches')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]