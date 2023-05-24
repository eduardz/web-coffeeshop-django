from django.shortcuts import render
# import http response
from django.http import HttpResponse
from .models import Coffee 

# adauga template home.html
def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'home.html', {'coffee': coffee})
    #return HttpResponse('<h1> Cafenea Home </h1>')
