from django.db import models

# Create your models here.

class Result(models.Model):
    image = models.ImageField(blank=True)
    answer = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')
    use_model = models.CharField(null=True, max_length=50)

class AiModel(models.Model):
    model_name = models.CharField(max_length=20)
    version = models.CharField(max_length=100)
    ai_file = models.FileField(upload_to='model/')
    is_selected = models.BooleanField(default=False) 
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.model_name