from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the hello index.")



def greet(request, name):
    return render(request, 'hello/greet.html',{"name": name.capitalize()})
