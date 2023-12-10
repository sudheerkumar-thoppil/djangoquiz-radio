from django.shortcuts import render
from .import views
from .models import Exam

def home(request):
    exam=Exam.objects.all()
    return render(request,'index.html',{"exam":exam})

