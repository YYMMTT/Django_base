from django.shortcuts import render

# Create your views here.

"""
视图函数就是Python函数

视图函数参数必须是request，必须有返回值
"""
from django.http import HttpRequest
from django.http import HttpResponse
def index(request):
    # return HttpResponse('ok')
    #render request, template_name, context=None,
    # 三个参数，第一个request，第二个模板名字，第三

    #模拟查询数据库
    content={
        'name':'马上端午了啊啊啊啊啊'
    }
    return render(request,'book/index.html',content)