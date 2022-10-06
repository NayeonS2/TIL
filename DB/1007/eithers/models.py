from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Either(models.Model):
    title = models.CharField(max_length=30)
    issue_a = models.CharField(max_length=30)
    issue_b = models.CharField(max_length=30)

    def __str__(self):
        return self.title

PICK_CHOICES = (
    ('BLUE', 'BLUE'),
    ('RED', 'RED'),
)

class Comment(models.Model):
    either = models.ForeignKey(Either, on_delete=models.CASCADE)
    pick = models.CharField(max_length=10, choices=PICK_CHOICES)
    content = models.TextField()

    def __str__(self):
        return self.content
