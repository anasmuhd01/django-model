from django.shortcuts import render
from django.views import View

# Create your views here.

class homeView(View):
    def get(self,req):
        return render(req,'home.html')