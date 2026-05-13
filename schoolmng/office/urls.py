from django.urls import path
from office.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',OfficeHomeView.as_view(),name="officehome"),
    path('test',AdddeptView.as_view(),name="adddept"),
    path('deptlist',DeptListView.as_view(),name="dptlistv"),
    path('dltdpt/<int:id>',DeleteDeptView.as_view(),name="dltdptview"),
    path('editdept/<int:id>',EditDeptView.as_view(),name="editdept"),
    path('addteacher',AddTeacher.as_view(),name="addteachr"),
    path('listteacher',ListTeacher.as_view(),name="listT"),
    path('deleteteacher/<int:id>',DeleteTeacherview.as_view(),name='deleteT'),
    path('editteacher',,name="editT"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)