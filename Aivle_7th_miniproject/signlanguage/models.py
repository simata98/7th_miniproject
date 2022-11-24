from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Result(models.Model):
    image = models.ImageField(blank=True)
    answer = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')
    use_model = models.CharField(null=True, max_length=50)

class AiModel(models.Model):
    model_name = models.CharField(max_length=30, null=True)
    version = models.CharField(max_length=100)
    file_upload = models.FileField(upload_to='upload_model/', blank=True)
    is_selected = models.BooleanField(default=False)
    uploader = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    create_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'[{self.pk}] {self.model_name} :: {self.uploader}'
    
