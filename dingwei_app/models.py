import json

from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.name



class Attention(models.Model):

    user_id = models.CharField(max_length=32)
    target_user_id = models.CharField(max_length=32)
    def __str__(self):
        return self.userId + '++'+self.targetUserId

class Location(models.Model):
    #用户id
    person = models.ForeignKey(Person,on_delete=models.CASCADE,)
    #时间
    time = models.CharField(max_length=30)
    #经度
    jing = models.CharField(max_length=30)
    #纬度
    wei = models.CharField(max_length=30)
    def __str__(self):
        return self.jing +""+ self.wei
