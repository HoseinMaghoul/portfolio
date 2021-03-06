from django.db import models
from datetime import datetime

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_3  = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    is_published = models.BooleanField(default=True)
    project_date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return f'{self.title} | {self.description[:30]}'
