from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from teacher.models import *

# Create your views here.

class homeView(View):
    def get(self,req):
        return render(req,'home.html')
    

class studentListView(View):
    def get(self,req):
        qso = StudentList.objects.all()
        return render(req,"studentlist.html",{'studentlist':qso})
    
class AddStudentView(View):
    def get(self,req):
        return render(req,"addstudent.html")
    def post(self,req):
        name=req.POST.get('name')
        age=req.POST.get('age')
        batch=req.POST.get('batch')
        place=req.POST.get('place')

        StudentList.objects.create(name=name,age=age,batch=batch,place=place)
        return redirect("slist")
    
class EditStudentView(View):
    def get(self,req,*args,**kwargs):
        sid=kwargs.get('sid')
        # edit_data will return the queryset <>
        edit_data= StudentList.objects.get(id=sid)
        # for i in edit_data:
        #     print(i.name)
        return render(req,"editstudent.html",{'data':edit_data})
    
    def post(self,req,*args,**kwargs):
        
        name=req.POST.get('name')
        age=req.POST.get('age')
        batch=req.POST.get('batch')
        place=req.POST.get('place')
        stud_obj  = StudentList.objects.get(id=kwargs.get("sid")   )
        stud_obj.name=name
        stud_obj.age=age
        stud_obj.batch=batch
        stud_obj.place=place
        stud_obj.save()
        return redirect('slist')
        
class DeleteStudent(View):
    def get(self,req,*args,**kwargs):
        del_val=kwargs.get('sid')
        StudentList.objects.get(id=del_val).delete()
        return redirect("slist")
        