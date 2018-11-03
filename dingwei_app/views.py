# coding：utf-8
from django.core import serializers
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# from dss.Serializer import serializer
import json
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
'''def add_person(request):
    response = {'status':True,'message':None}
    print(request.POST)
    try:
        n = request.POST.get('name')
        ph = request.POST.get('phone')
        password = request.POST.get('password')
        Person.objects.create(name=n,phone=ph)
    except Exception as e:
        response['status'] = False
        response['message'] = '用户输入错误'

    return HttpResponse('OK')'''

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

'''def response_as_json(data):
#    jsonString = serializer(data=data, output_type="json", foreign=foreign_penetrate)
    jsonString = json.dumps(data)
    response = HttpResponse(
            # json.dumps(dataa, cls=MyEncoder),
            jsonString,
            content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response'''
'''class Employee (object):

  empCount = 0

 

  def __init__(self, name, salary) :

    self.name  = name

    self.salary = salary

    Employee.empCount += 1'''
class ResponceData():

    def __init__(self,code,msg,data):
        self.code = code
        self.msg = msg
        self.data = data


def register(request):
    ph = request.POST.get('phone')
    password = request.POST.get('password')
    person = Person(phone=ph,password=password)
#    Person.objects.create(phone=ph, passWord=password)
    person.save()
    data = ResponceData(code=200,msg="成功",data=person)

  #  data.data = person
    jsonString = json.dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    print(jsonString)
    return HttpResponse(jsonString, content_type="application/json")




def login(request):
    try:
        j = request.GET.get('phone')
        w = request.GET.get('password')
        p = Person.objects.filter(phone__exact=j).filter(password__exact=w)

        if len(p) == 0 :
            '''找不到用户'''
            data = ResponceData(code=200, msg="成功", data=None)
            print(data)
            jsonString = json.dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        else:
            '''找到用户'''
            data = ResponceData(code=200, msg="成功",data=p[0])
            jsonString = json.dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=4)


    except IOError  as e:
        data = ResponceData(code=500, msg="error", data=None)
        print(data)
        jsonString = json.dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    print(jsonString)
    return HttpResponse(jsonString, content_type="application/json")

