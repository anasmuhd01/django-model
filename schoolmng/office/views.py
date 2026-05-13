from django.shortcuts import render,redirect
from django.views import View
from office.forms import * 
from django.http import HttpResponse
# Create your views here.

class OfficeHomeView(View):
    def get(self,req):
        return render(req,'officehome.html')
    
class AdddeptView(View):
    def get(self,req):
        form = DeptForm()
        return render(req,"adddept.html",{'form':form})
    def post(self,req):
        form_data = DeptForm(data=req.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('officehome')
        
class DeptListView(View):
    def get(self,req):
        data = Department.objects.all()
        return render(req,"deptlist.html",{'data':data})
    
class DeleteDeptView(View):
    def get(self,req,**kwargs):
        id = kwargs.get('id')
        Department.objects.get(id=id).delete()
        return redirect("dptlistv")

class EditDeptView(View):

    def get(self,req,**kwargs):
        did = kwargs.get('id')
        dqso = Department.objects.get(id=did)
        form = DeptForm(instance=dqso)
        return render(req,"editdept.html",{'form':form})
    
    def post(self,req,**kwargs):
        id = kwargs.get('id')
        qso = Department.objects.get(id = id)
        form_data = DeptForm(data=req.POST,instance=qso)
    
        if form_data.is_valid():
            form_data.save()
            return redirect('dptlistv')

class AddTeacher(View):
    def get(self,req):
        form = TeacherForm()
        return render(req,"addteacher.html",{'form':form})
    
    def post(self,req):
        form_data = TeacherForm(data=req.POST,files=req.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect("listT")
    
class ListTeacher(View):
    def get(self,req):
        teacherqso = Teacher.objects.all()
        return render(req,"viewteacher.html",{'teacherdata':teacherqso})
    
class DeleteTeacherview(View):
    def get(self,req,**kwargs):
        id = kwargs.get('id')
        Teacher.objects.get(id=id).delete()
        return redirect('listT')
    


        
        