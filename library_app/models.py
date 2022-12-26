from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)

class Books(models.Model):
    title =  models.CharField(max_length=255)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    description = models.TextField()
    image =models.ImageField(upload_to='images')
    Authors = models.TextField()