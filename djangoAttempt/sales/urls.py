#新建的文件用于创建路由子表
from django.urls import path

from sales.views import listcustomers,listcustomersWithGUI1,listorders

urlpatterns = [
    path('orders/', listorders),
    #修改路由表， 加上对 sales/customers/ url请求的 路由
    path('customers/',listcustomers),
    path('customersGui/',listcustomersWithGUI1),
]