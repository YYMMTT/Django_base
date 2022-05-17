from django.db import models

# Create your models here.
"""
model中的类需要继承models.Model 
字段定义  字段名=model.类型(选项) 当charfield选项必填

模型有自带的ID，主键
"""

#创建书籍 模型类
class BookInfo(models.Model):

    name=models.CharField(max_length=10) #数据库最大长度

   #在admin中显示书籍的名字
    def __str__(self):
        return self.name


#创建人物模型类
class PeopleInfo(models.Model):

    name=models.CharField(max_length=1)
    gender=models.BooleanField()
    #外键约束 属于哪本书
    book=models.ForeignKey('BookInfo',on_delete=models.CASCADE)
