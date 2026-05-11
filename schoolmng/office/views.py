from django.shortcuts import render
from django.views import View

# Create your views here.

class OfficeHomeView(View):
    def get(self,req):
        return render(req,'officehome.html')