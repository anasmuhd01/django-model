from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from teacher.models import *
from teacher.forms import *

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
    
#homeworks

class HomeworkListView(View):
    def get(self,req):
        data =HomeWork.objects.all()
        return render(req,"homeworklist.html",{'data':data})
    
class AddhomeworkView(View):
    def get(self,req):

        form = HomeworkForm()
        
        return render(req,"addhomeworks.html",{'form':form,})
    
    def post(self,req):
        # subject = req.POST.get('subject')
        # question = req.POST.get('question')
        # date = req.POST.get('submit_date')
        form_data = HomeworkForm(data=req.POST)
        if form_data.is_valid():
            
            subject = form_data.cleaned_data('subject')
            question = form_data.cleaned_data('question')
            date = form_data.cleaned_data('submit_date')
        
            HomeWork.objects.create(subject=subject,question=question,submit_date=date)
            return redirect('viewworks')
        return  HttpResponse('Form validation failed')
    
# class EdithomeworkView(View):
#     def get(self,req):
#         return render(req,"edithomework.html")



