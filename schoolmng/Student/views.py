from django.shortcuts import render
from django.views import View

# Create your views here.

class StudentHomeView(View):
    def get(self,req):
        return render(req,"home.html")
    
class ListWorkView(View):
    def get(self,req):
        return render(req,"listworks.html")
