#新建的文件用于创建路由子表
from django.urls import path

from . import views

urlpatterns = [
    path('orders/', views.listorders),
]