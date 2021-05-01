from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField(max_length=2048)


    #To Represent data of book
    def __str__(self):
        return self.title
    