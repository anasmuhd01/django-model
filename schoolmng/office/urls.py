from django.urls import path
from office.views import *
urlpatterns=[
    path('',OfficeHomeView.as_view(),name="officehome"),
    path('test',AdddeptView.as_view(),name="adddept"),
    path('deptlist',DeptListView.as_view(),name="dptlistv"),
    path('dltdpt/<int:id>',DeleteDeptView.as_view(),name="dltdptview"),
    path('editdept',EditDeptView.as_view(),name="editdept"),
]