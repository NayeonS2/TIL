# Generated by Django 3.2.9 on 2022-11-04 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movies.Genre'),
        ),
    ]
