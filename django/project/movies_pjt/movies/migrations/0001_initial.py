# Generated by Django 3.2.13 on 2022-10-07 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('audience', models.IntegerField()),
                ('release_date', models.DateTimeField()),
                ('genre', models.CharField(max_length=30)),
                ('score', models.FloatField()),
                ('poster_url', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
