from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField(max_length=2048)


    #To Represent data of post
    def __str__(self):
        return self.title
    