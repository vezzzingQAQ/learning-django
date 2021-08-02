from django.db import models

# Create your models here.
class Customer(models.Model):
    #2021.8.2.12.19
    # 客户名称
    name=models.CharField(max_length=200)

    # 联系电话
    phonenumber = models.CharField(max_length=200)

    # 地址
    address = models.CharField(max_length=200)

    #官方文档
    #https://docs.djangoproject.com/en/2.0/ref/models/fields/#model-field-types
    #
    #修改了Models.py 里面的库表的定义，都需要再次运行 python manage.py makemigrations common 和 python manage.py migrate 命令，使数据库同步该修改结果
    