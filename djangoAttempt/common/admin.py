from django.contrib import admin

from .models import Customer
# 将创建的表格加入管理员视图
# Register your models here.
admin.site.register(Customer)

