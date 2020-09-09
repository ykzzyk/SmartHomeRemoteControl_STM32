# """SmartHome URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.conf.urls import url
from django.contrib import admin
from django_web.views import index #导入views.py文件中的index函数
from django_web.views import lighton
from django_web.views import lightoff
from django_web.views import getdata
from django_web.views import upload

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^on', lighton),
    url(r'^off', lightoff),
    url(r'^getdata', getdata),
    url(r'^upload', upload),
    url(r'^', index), #在url中凡是以url开头的访问都使用index函数来处理该请求
]
