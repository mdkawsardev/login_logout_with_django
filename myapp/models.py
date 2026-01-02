from django.db import models

# Create your models here.
class myusers(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    def __str__(self):
        return self.name
class Books(models.Model):
    books = models.CharField(max_length=200)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    