from django.shortcuts import render, redirect
from django.views import View

from book.models import PeopleInfo,BookInfo

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
    #在这里实现 增删改查
    #运行，数据库增加一条记录
    book=BookInfo.objects.create(
        name='abc123',
        pub_date='2000-1-1',
        readcount=10
    )


    content={
        'name':'马上端午了啊啊啊啊啊'
    }
    return render(request,'book/index.html',content)

def shop(request,city_id,mobile):
    # import re
    # if not re.match('\d{5}',mobile):
    #     return HttpResponse('没有商品')

    # 获取路由路径的参数
    print(city_id,mobile)
    # 如何获取查询字符串
    query_params = request.GET
    # order=query_params.get('order')
    # order=query_params['order']
    print(query_params)
    # <QueryDict: {'order': ['readcount']}>
    #QueryDict 具有字典特性
    #还具有 一键多值
    # < QueryDict: {'order': ['readcount', 'commentcount'], 'page': ['1']} >
    order=query_params.getlist('order')
    print(order)
    return HttpResponse('杨姐的小饭店SHOPaaaaa')

def register(request):
    #form表单传参 获取body数据
    body=request.POST
    print(body)


    #<QueryDict: {'user': ['ymt'], 'password': ['123456']}>
    return HttpResponse('ok')


def json(request):
    #json传参 通过body获取请求传递的json数据
    body=request.body
    # print(body) #b'{\n    "name":"ymt",\n    "age":10\n}'

    body_str = body.decode()  # b转换为字符串
    print(body_str)
    #类似json类型的字符串  转换为字典（好获取数据）
    import json
    body_dict=json.loads(body_str)
    print(body_dict)

    return HttpResponse('json')


def methon(request):
    methon=request.method
    print(methon)
    header=request.META  #返回的是个字典类型
    print(header['SERVER_NAME'])
    return HttpResponse('methon')


def response(request):
    #添加响应头
    # response=HttpResponse('res',status=200)
    # response['name']='ymt'
    from django.http import HttpResponse,JsonResponse
    # response=JsonResponse()
    #JSON字符串 --->dict  loads()
    #dict --->JSON字符串  dumps()
    info={
        'name':'ymt',
        'address':'shunyi'
    }
    girl_friends=[
        {
            'name': 'ymt',
            'address': 'shunyi'
        },
        {
            'name': 'xl',
            'address': 'shengzhen'
        }
    ]

    #data 是返回的数据，返回的一般是字典
    # response = JsonResponse(data=info)
    """
    safe=True 表示data是字典数据
    JsonResponse 可以把字典转换为json数据(传的字典，可以转换为json）
    
    现在传递的是非字典，出现问题自己负责 safe=False
    """
    # response = JsonResponse(data=girl_friends,safe=False)
    # girl_friends=json.dumps(girl_friends)
    # response = JsonResponse(data=girl_friends)
    # import json
    # data = json.dumps(girl_friends)
    # print(type(data))
    # return HttpResponse(data)
    return redirect('http://www.itcast.cn')

#####################cookie和session##################
"""
第一次请求，携带 查询字符串
http://127.0.0.1:8000/set_cookie/?name=ymt&password=123  
服务器接受到请求之后，获取name,服务器设置cookie信息，cookie信息包括 name
浏览器接受到服务器到响应之后，应该把cookie保存起来

第二次及其之后到访问，http://127.0.0.1:8000这个域名网站，都会携带cookie，服务器就可以读取cookie信息，来判断用户身份
"""

def set_cookie(request):
    #1、获取查询字符串传递的name
    username=request.GET.get('name')
    password=request.GET.get('password')
    # print(username)
    #2.设置cookie 是通过respond对象的set_cookie（）方法实现的
    response = HttpResponse()
    # key,value="",
    response.set_cookie('name',username,max_age=60*60)
    response.set_cookie('password',password)
    #删除cookie
    # response.delete_cookie('name')
    return  response

def get_cookie(request):
    #获取cookie
    # cookie=request.COOKIES
    # print(cookie['name'])
    name=request.COOKIES.get('name')
    password=request.COOKIES.get('password')
    return HttpResponse(name)


def set_session(request):
    # session是保存在服务器端
    #session 需要依赖于 cookie
    """"
    第一次请求，携带 查询字符串
http://127.0.0.1:8000/set_session/?name=itcast  在服务端设置服务session信息，同时服务器会返回一个sessionid的cookie信息
浏览器接受的信息后，会把cookie信息保存起来

    第二次以其后面每次访问，都会带上信sessionid信息，验证没有问题会读取相关数据，实现业务逻辑
    """
    #1、获取请求的参数 模拟获取用户信息
    name=request.GET.get('name')
    #2、假设从数据库查询用户到了用户信息 设置session
    user_id=1
    request.session['user_id']=user_id
    request.session['name']=name
    #clear删除值，key不删除
    # request.session.clear()
    #falush key和value都删除
    # request.session.flush()
    #设置session有效期 先有session
    # request.session.set_expiry(None)

    return  HttpResponse('set_session')


def get_session(request):
    user_id=request.session.get('user_id')
    name=request.session.get('name')
    content=f'{user_id},{name}'
    return HttpResponse(content)

def login(request):
    #登录页面是get,但是登录接口是post，想在视图函数满足两种请求，可以用类视图
    if request.method == 'GET':
        return HttpResponse('get逻辑')
    else:
        return HttpResponse('post逻辑')

#####################类视图##################
"""
1、class 类视图名(View)
2、类视图里面的函数名，以http请求方法的小写名 命名
"""

class LoginView(View):
    def get(self,request):
        return HttpResponse('GET GET GET')
    def post(self,request):
        return HttpResponse('POST POST POST')


#####################查询数据##################


#####################增加数据##################
# from book.models import BookInfo
# #方式一
# book=BookInfo(
#     name='测试运维',
#     pub_date='2000-1-1',
#     readcount=100
# )
# #要调用save()方法才可保存到数据库中
# book.save()
#
#
# #方式二
# #objcts 相当于一个代理  实现增删改查
# BookInfo.objects.create(
#     name='测试开发入门',
#     pub_date='2020-1-1',
#     readcount=1000
# )
#
#
# #####################修改数据##################
# #方式一
# book=BookInfo.objects.get(id=6)
# book.name='哈哈哈书籍'
# #要调用save()方法才可保存到数据库中
# book.save()
# #方式二
# BookInfo.objects.filter(id=6).update(name='测试开发入门',commentcount=666)
#
#
# #####################删除数据##################
# # 方式一
# book=BookInfo.objects.get(id=6).delete()
# #方式二
# book=BookInfo.objects.filter(id=5).delete()
#
# #####################查询数据##################
# #get 查询单一结果，如果不存在 会抛出DoesNotExist:异常
# try:
#     BookInfo.objects.get(id=5)
# except BookInfo.DoesNotExist:
#     print('查询结果不存在')
#
# #all 查询多个结果
# BookInfo.objects.all()
#
# #count 查询结果数量
# BookInfo.objects.count()
# BookInfo.objects.all().count()
#
# #####################过滤数据##################
# #相当于mysql中的where
# #filter  过滤出多个结果集
# #exclude 排除符合条件剩下的结果
# #get 过滤单一结果
#
# #模型类名.objects.filter(属性名__运算符=值）id=1   获取n个结果
# #模型类名.objects.exclude(属性名__运算符=值）   获取n个结果
# #模型类名.objects.get(属性名__运算符=值）   获取1个结果  或者 异常
#
#
# #查询编号为1的图书
# book=BookInfo.objects.get(id=1)  #简写
# book=BookInfo.objects.get(id__exact=1) #完整形式
# book=BookInfo.objects.filter(pk=1)  #primary key 主键
#
# # 查询书名包含'湖'的图书
# BookInfo.objects.filter(name__contains='湖')
# # 查询书名为空的图书
# BookInfo.objects.filter(name__isnull=True)
# # 查询编号为1或3或5的图书
# BookInfo.objects.filter(id__in=[1,3,5])
# # 查询编号大于3的图书
# #  大于 gt  great
# #  大于等于 gte  equal
# #
# #  小于 lt
# #  小于等于 lte
# BookInfo.objects.filter(id__gt=3)
# #查询编号不等于3的图书
# BookInfo.objects.exclude(id=3)
# # 查询1980年发表的图书
# BookInfo.objects.filter(pub_date__year='1980')
# # 查询1990年1月1日发表的图书
# BookInfo.objects.filter(pub_date__gt='1990-1-1')
# #######################################
#
# from django.db.models import F
# #使用： 2个属性的比较
# #语法形式  以filter为例 模型类名.objects.filters(属性名__运算符=F('第二个属性名')
# #查询阅读量大于等于评论量的图书
# BookInfo.objects.filter(readcount__gte=F('commentcount'))
#
# #######################################
# #并且查询
# #查询阅读量大于20，并且编号小于3
# BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
# BookInfo.objects.filter(readcount__gt=20,id__lt=3)
# from django.db.models import Q
# #或者语法  模型类名.objects.filter(Q(属性名__运算符=值）|Q(属性名__运算符=值)|...)
# #并且语法  模型类名.objects.filter(Q(属性名__运算符=值）&Q(属性名__运算符=值)|...)
# #not 非 语法  模型类名.objects.filter(～Q(属性名__运算符=值）)
#
# BookInfo.objects.filter(Q(readcount__gt=20)&Q(id__lt=3))
#
# #查询编号不等于3的图书
# BookInfo.objects.exclude(id=3)
# BookInfo.objects.filter(~Q(id=3))
#
# ###############聚合函数##################
# from  django.db.models import Sum,Max,Min,Avg,Count
# #模型类名.objects.aggregate(Xxx('字段名'))
# BookInfo.objects.aggregate(Sum('readcount'))
# ###############排序##################
# BookInfo.objects.all().order_by('readcount')
#
# #查询书籍为1的所有人物信息
# book=BookInfo.objects.get(id=1)
# book.peopleinfo_set.all()  #在1对多，在1的地方有(关联模型类名小写_set)peopleinfo_set 隐藏的字段
#
# #查询人物为1的书籍信息
# from book.models import PeopleInfo
# people=PeopleInfo.objects.get(id=1)
# people.book.name
# ###############关联过滤查询##################
# #查询1的数据，条件为n
# #模型类名.objects(关联模型类名小写__字段名__运算符=值）
#
# #查询图书，要求图书人物为'郭靖'
# BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
# BookInfo.objects.filter(peopleinfo__name='郭靖')
# #查询图书，要求图书人物的描述包含'八'
# BookInfo.objects.filter(peopleinfo__description__contains='八')
#
# #查询书名为'天龙八部'的所有人物
# PeopleInfo.objects.filter(book__name__exact='天龙八部')
# PeopleInfo.objects.filter(book__name='天龙八部')
# # 查询图书阅读量大于30的所有人物
# PeopleInfo.objects.filter(book__commentcount__gt=30)