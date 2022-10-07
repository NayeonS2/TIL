from django.db import models
from django.conf import settings

GENRE_CHOICES = (
    ('comedy','코미디'),
    ('horror','공포'),
    ('romance','로맨스'),
)




# Create your models here.
class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title

