from django.forms.models import ModelForm
from .models import Student, Presence
from django import forms

class StudentForm(ModelForm):

  class Meta:
    # la ref du ModEle
    model = Student

    # liste des champs A Editer
    fields  = [
      "first_name",
      "last_name",
      "birth_date",
      "email",
      "phone",
      "comments",
      "cursus",
    ]
    widgets = {
        'birth_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }


class particularcallForm(ModelForm):

  class Meta:
    # la ref du ModEle
    model = Presence

    # liste des champs A Editer
    fields  = [
      "todayDate",
      "isMissing",
      "reason",
      "Student"
    ]

    widgets = {
        'todayDate': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }