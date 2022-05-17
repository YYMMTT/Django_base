from django.shortcuts import render

# Create your views here.

"""
视图函数就是Python函数

视图函数参数必须是request，必须有返回值
"""
from django.http import HttpRequest
from django.http import HttpResponse
def index(request):
    return HttpResponse('ok')