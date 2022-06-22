from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def create_book(request):
    return HttpResponse('create')

