from django.db import models

# Create your models here.

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    
class Book(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=250)
    description = models.TextField(default=0)
    price = models.IntegerField(default=0)
    genre = models.CharField(max_length=100)
    autor = models.CharField(max_length=35)
    year = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)