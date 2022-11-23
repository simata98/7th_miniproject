from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Result(models.Model):
    image = models.ImageField(blank=True)
    answer = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')

class AiModel(models.Model):
    model_name = models.CharField(max_length=30, null=True)
    file_upload = models.FileField(upload_to='upload_model/', blank=True)
    uploader = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    create_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'[{self.pk}] {self.model_name} :: {self.uploader}'