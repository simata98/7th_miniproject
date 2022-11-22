from django.db import models

class Result(models.Model):
    image = models.ImageField(blank=True)
    answer = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')

class Image(models.Model):
    image = models.ImageField(blank=True)
    answer = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')

class AiModel(models.Model):
    path = models.CharField(max_length=512)
    version = models.CharField(max_length=10)
    file_name = models.CharField(max_length=10)
    pub_date = models.DateTimeField(verbose_name='date published')