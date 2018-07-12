# coding：utf-8
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from dingwei_app import models
from dingwei_app.models import Person, Location


def index(request):
    return HttpResponse(u'欢迎光临')
def home(request):
    return render(request,'home.html')
def persons(request):
    person_list = models.Person.objects.all()
    return render(request,"persons.html",{'person_list':person_list})
def locations(request):
    location_list = models.Location.objects.all()
    return render(request,"locations.html",{'location_list':location_list})
def add_person(request):
    response = {'status':True,'message':None}
    print(request.POST)
    try:
        n = request.POST.get('name')
        ph = request.POST.get('phone')
        Person.objects.create(name=n,phone=ph)
    except Exception as e:
        response['status'] = False
        response['message'] = '用户输入错误'

    return HttpResponse('OK')

def add_location(request):
    response = {'status':True,'message':None}
    print(request.POST)
    try:
        j = request.POST.get('jing')
        w = request.POST.get('wei')
        Location.objects.create(jing=j,wei=w)
    except Exception as e:
        response['status'] = False
        response['message'] = '用户输入错误'

    return HttpResponse('OK')