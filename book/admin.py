from django.contrib import admin

# Register your models here.
#导入要注册的模型
from book.models import BookInfo
from book.models import PeopleInfo
#让超管管理我们的模型
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)