from django.urls import path
from book.views import index,shop

#urlpatterns 固定写法
urlpatterns = [
    #path,第一个路由地址，第二个视图函数名
    path('index/',index),
    path('<city_id>/<shop_id>',shop)

]