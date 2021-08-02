"""djangoattempt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#创建url路由
from sales.views import listorders
urlpatterns = [
    path('admin/', admin.site.urls),
    #添加如下的路由记录
    #前端过来的请求 url地址 是 /sales/orders/ , 就由 views.py 里面的函数 listorders 来处理
    path('sales/orders/', listorders),
]
