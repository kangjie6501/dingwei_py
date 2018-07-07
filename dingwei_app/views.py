# coding：utf-8
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from dingwei_app import models


def index(request):
    return HttpResponse(u'欢迎光临')
def home(request):
    return render(request,'home.html')
def persons(request):
    person_list = models.Person.objects.all()
    return render(request,"persons.html",{'person_list':person_list})