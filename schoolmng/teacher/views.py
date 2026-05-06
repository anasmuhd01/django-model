from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class homeView(View):
    def get(self,req):
        return render(req,'home.html')
    

class studentListView(View):
    def get(self,req):
        return render(req,"studentlist.html")
    
class AddStudentView(View):
    def get(self,req):
        return render(req,"addstudent.html")
    def post(self,req):
        name=req.POST.get('name')
        age=req.POST.get('age')
        batch=req.POST.get('batch')
        place=req.POST.get('place')
        return HttpResponse(f"{name} {age} {batch} {place}")
    
class EditStudentView(View):
    def get(self,req):
        return render(req,"editstudent.html")
    
    def post(self,req):
        name=req.POST.get('name')
        age=req.POST.get('age')
        batch=req.POST.get('batch')
        place=req.POST.get('place')
        return HttpResponse(f"{name} {age} {batch} {place}")
        