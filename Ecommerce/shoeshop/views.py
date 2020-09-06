from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'shoeshop/index.html')

def another(request, name):
    context = {
        'name': name.capitalize()
    }
    return render(request, 'shoeshop/another.html', context= context)