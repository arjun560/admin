from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'welcome.html')
# Create your views here.

def new(request):
    return HttpResponse('the page is newate')
