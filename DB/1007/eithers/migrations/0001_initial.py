# Generated by Django 3.2 on 2022-10-06 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Either',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('issue_a', models.CharField(max_length=30)),
                ('issue_b', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick', models.CharField(choices=[('BLUE', 'BLUE'), ('RED', 'RED')], max_length=10)),
                ('content', models.TextField()),
                ('either', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eithers.either')),
            ],
        ),
    ]
