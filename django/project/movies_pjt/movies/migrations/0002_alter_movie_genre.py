# Generated by Django 3.2.13 on 2022-10-07 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('코미디', '코미디'), ('공포', '공포'), ('로맨스', '로맨스')], max_length=30),
        ),
    ]
