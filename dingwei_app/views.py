# coding：utf-8
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from dingwei_app import models
from dingwei_app.models import Person, Location
from dss.Serializer import serializer


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

def response_as_json(data, foreign_penetrate=False):
    jsonString = serializer(data=data, output_type="json", foreign=foreign_penetrate)
    response = HttpResponse(
            # json.dumps(dataa, cls=MyEncoder),
            jsonString,
            content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def login(request):
    response = {'status':True,'message':None}
    print(request.GET)
    try:
        j = request.GET.get('phone')
        w = request.GET.get('password')
        p = Person.objects.filter(phone__exact=j).filter(passWord__exact=w)
        if p.len == 0 :
            '''找不到用户'''

        else:
            '''找到用户'''


    except Exception as e:
        response['status'] = False
        response['message'] = '用户输入错误'

    return HttpResponse(j+w)

