from django.db import models

# Create your models here.

class WordCount(models.Model):
    words = models.TextField()