from django.shortcuts import render
from app.models import *
# Create your views here.
def home_view(request):
    context = {
        "products" : Product.objects.all(),
    }
    return render(request, 'home.html', context)
def about_view(request):
    context = {}
    return render(request, 'about.html', context)
def detail_view(request):
    context = {
        "product":Product.objects.get(id=id),
    }
    return render(request, 'detail.html', context)