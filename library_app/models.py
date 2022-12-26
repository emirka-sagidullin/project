from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Books(models.Model):
    title =  models.CharField(max_length=255)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    image =models.FileField(upload_to='img/')
    Authors = models.TextField()
    date = models.CharField(max_length=50)