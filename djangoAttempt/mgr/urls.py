#新建的文件用于创建路由子表
from django.urls import path

from mgr import customer

urlpatterns = [
    path('customers',customer.dispatcher),
]