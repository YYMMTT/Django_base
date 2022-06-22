from django.db import models

# Create your models here.
"""
model中的类需要继承models.Model 
字段定义  字段名=model.类型(选项) 当charfield选项必填
        1、字段名不要用python 和 mysql关键字
        2、不要使用连续的下划线（后面查询有用到__)
        3、ID会主动生成
类型      1、mysql的类型
选项      1、是否有默认值，是否唯一，是否为null
         2、CharField 必须设置max_length
         3、verbose_name 主要是admin站点使用
         
修改表的名字 默认：子应用名_类名 都是小写

            

模型有自带的ID，主键
"""

#创建书籍 模型类
class BookInfo(models.Model):

    name=models.CharField(max_length=10) #数据库最大长度
    pub_date=models.DateField(null=True)
    readcount=models.IntegerField(default=0)
    commentcount=models.IntegerField(default=0)
    is_delete=models.BooleanField(default=False)

    class Meta:
        db_table='bookinfo' #修改表的名字
        verbose_name='书籍管理' #admin站点名字使用

   #在admin中显示书籍的名字
    def __str__(self):
        return self.name


#创建人物模型类
class PeopleInfo(models.Model):
    #定义一个有序字典
    GENDER_CHOICE=(
        (1,'male'),
        (2,'female'),
    )
    name=models.CharField(max_length=10,unique=True)
    gender=models.SmallIntegerField(choices=GENDER_CHOICE,default=1)
    description=models.CharField(max_length=100,null=True)
    is_delete=models.BooleanField(default=False)

    # 在1对多，在1的地方有(关联模型类名小写_set)peopleinfo_set 隐藏的字段
    # peopleinfo_set

    #外键约束 属于哪本书
    #系统会自动为外键添加_id

    #外键的级联操作
    #主表 从表
    #1 对 多
    #主表删除，从表怎么办？
    #Set null 从表该咋办咋办
    #级联删除
    #抛出异常，不让删除
    book=models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    # book=BookInfo

    class Meta:
        db_table='peopleinfo'

    def __str__(self):
        return self.name
