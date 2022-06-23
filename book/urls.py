from django.urls import path
from book.views import index,shop,register,json,methon,response
from book.views import set_cookie,get_cookie,set_session,get_session,login
from book.views import LoginView

from django.urls import converters
from django.urls.converters import register_converter

#1、定义转换器
class MobileConverter:
    #数据验证的是 正则
    regex = "1[2-9]\d{9}"
    #验证没有问题的数据，给视图函数
    def to_python(self, value):
        return value

    # def to_url(self, value):
    #将匹配结果用于反向解析传递值使用（了解）
    #     return str(value)
#2、先注册转换器，才能在第三步中使用
# converter 转换器类
# type_name 转换器名字
register_converter(MobileConverter,'phone')

#urlpatterns 固定写法
urlpatterns = [
    #path,第一个路由地址，第二个视图函数名
    path('index/',index),
    #   转换器名字：变量名
    #   转换器会对变量数据进行验证 正则的验证


    path('<int:city_id>/<phone:mobile>/',shop),
    path('register',register),
    path('json',json),
    path('methon',methon),
    path('res',response),
    path('set_cookie/',set_cookie),
    path('get_cookie/',get_cookie),
    path('set_session/',set_session),
    path('get_session/',get_session),
    path('login/',login),
    #################类视图
    path('163login/',LoginView.as_view()),

]

