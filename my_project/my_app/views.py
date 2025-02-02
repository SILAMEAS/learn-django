from django.shortcuts import render,HttpResponse
from . import models

# Create your views here.

def home(request):
    return render(request=request,template_name='home.html')

def items(request):
    products = models.Item.objects.all()
    return render(request=request,template_name='products.html',context={'products':products})
    
