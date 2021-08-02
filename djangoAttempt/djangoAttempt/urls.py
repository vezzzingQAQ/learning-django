"""djangoAttempt URL Configuration

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
# 别忘了导入 listorders 函数
# from sales.views import listorders
# 导入一个include函数
from django.urls import path, include
# 添加路由记录
urlpatterns = [
    path('admin/', admin.site.urls),
    # 添加如下的路由记录
    # path('sales/orders/', listorders),

    # 凡是 url 以 sales/  开头的，
    # 都根据 sales.urls 里面的 子路由表进行路由
    path('sales/', include('sales.urls')),
    path('/api/mgr/',include('.mgr.urls')),
]
