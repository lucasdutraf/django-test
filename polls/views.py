from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("Hi there, u r at the polls index")