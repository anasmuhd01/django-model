from django import forms
from office.models import *

class DeptForm(forms.ModelForm):
    class Meta:
        model=Department
        fields="__all__"

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"