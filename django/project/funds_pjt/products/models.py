from random import choices
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.forms import IntegerField
# Create your models here.

RISK_CHOICES = (
    ('낮은위험','낮은위험'),
    ('보통위험','보통위험'),
    ('다소높은위험','다소높은위험'),
    ('높은위험','높은위험'),
    ('매우높은위험','매우높은위험'),
)

COMPANY_CHOICES = (
    ('한화자산운용','한화자산운용'),
    ('엔에이치아문디자산운용','엔에이치아문디자산운용'),
    ('멀티에셋자산운용','멀티에셋자산운용'),
    ('삼성자산운용','삼성자산운용'),
    ('한국투자신탁운용','한국투자신탁운용'),
    ('키움투자자산운용','키움투자자산운용'),
    ('미래에셋자산운용','미래에셋자산운용'),
    ('아이비케이자산운용','아이비케이자산운용'),
    ('마이다스에셋자산운용','마이다스에셋자산운용'),
    ('신한자산운용','신한자산운용'),
    ('한국투자밸류자산운용','한국투자밸류자산운용'),
    ('유리자산운용','유리자산운용'),
    ('알파자산운용','알파자산운용'),
    ('피델리티자산운용','피델리티자산운용'),
    ('교보악사자산운용','교보악사자산운용'),
    ('케이비자산운용','케이비자산운용'),
    ('에셋플러스자산운용','에셋플러스자산운용'),
)

PERIOD_CHOICES = (
    ('6개월','6개월'),
    ('1년','1년'),
    ('3년','3년'),
)


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    risk = models.CharField(max_length=10, choices=RISK_CHOICES)
    company = models.CharField(max_length=20, choices=COMPANY_CHOICES)
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES)
    money = models.IntegerField()
