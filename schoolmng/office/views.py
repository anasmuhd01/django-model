from django.shortcuts import render,redirect
from django.views import View
from office.forms import * 

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
    def get(self,req):
        form = DeptForm()
        return render(req,"editdept.html",{'form':form})