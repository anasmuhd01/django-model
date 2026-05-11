from django import forms


class HomeworkForm(forms.Form):
    subject = forms.CharField()
    question = forms.CharField()
    submit_date = forms.DateField()