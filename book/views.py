from django.shortcuts import render
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

def shop(request,city_id,shop_id):

    print(city_id,shop_id)
    #如何获取查询字符串
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
    return HttpResponse('杨姐的小饭店SHOP')


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