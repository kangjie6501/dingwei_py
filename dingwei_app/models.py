from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=32)
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

# class Location(models.Model):
#     jing = models.CharField(max_length=30)
#     wei = models.CharField(max_length=30)
#     date = models.CharField(max_length=30)
#     id = models.CharField(max_length=32)
#
#     def __str__(self):
#         return self.id
