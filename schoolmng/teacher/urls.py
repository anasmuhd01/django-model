from django.urls import path
from teacher.views import *

urlpatterns = [
    path('list',studentListView.as_view(),name="slist"),
    path('add',AddStudentView.as_view(),name="sadd"),
    path('edit<int:sid>',EditStudentView.as_view(),name='sedit'),
    path('delete<int:sid>',DeleteStudent.as_view(),name='sdelete'),
    path('viwworks',HomeworkListView.as_view(),name="viewworks"),
    path('addhwrk',AddhomeworkView.as_view(),name="addhworks"),
    path('edithwork/<int:hid>',EdithomeworkView.as_view(),name='edithw'),
    path('delethw/<int:hid>',DeleteHomewrkView.as_view(),name="delhw"),

]