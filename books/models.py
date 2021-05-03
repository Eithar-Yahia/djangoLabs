from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CopyRight(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Metric(models.Model):
    reads = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.reads

class Book(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField(max_length=2048)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True, related_name="books")
    categories = models.ManyToManyField(Category)
    metrics = models.OneToOneField(Metric, on_delete=models.CASCADE, null=True, blank=True)
    copyright = models.ForeignKey(CopyRight, null=True, blank=True, on_delete=models.CASCADE)
    


    #To Represent data of book
    def __str__(self):
        return self.title
    