from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says here is the about page.")

# Create your views here.
