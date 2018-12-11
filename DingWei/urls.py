"""DingWei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dingwei_app import views as learn_views

urlpatterns = [
 #   path('admin/', admin.site.urls),
  #  path('',learn_views.index,),
   # path('admin/',admin.site.urls),
    path('',learn_views.home,name='home'),
    path('login/', learn_views.login),
    path('register/', learn_views.register),
    path('persons/',learn_views.persons),
  #  path('add_person',learn_views.add_person),
    path('locations/',learn_views.locations),
    path('addLocation/',learn_views.add_location),
    #clearLocationByUserId/
    path('clearLocationByUserId/', learn_views.clear_location),
    path('getLocationByUserId/',learn_views.get_location_by_user_id),
    path('addAttention/',learn_views.add_attention),
    path('getAttentions/',learn_views.get_attentions),
    path('d/', learn_views.file_down),
]
