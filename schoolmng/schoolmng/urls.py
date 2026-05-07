"""
URL configuration for schoolmng project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from teacher.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homeView.as_view()),
    path('list',studentListView.as_view(),name="slist"),
    path('add',AddStudentView.as_view(),name="sadd"),
    path('edit<int:sid>',EditStudentView.as_view(),name='sedit'),
    path('delete<int:sid>',DeleteStudent.as_view(),name='sdelete')
]
