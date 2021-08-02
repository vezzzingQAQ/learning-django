from django.shortcuts import render

from django.http import HttpResponse
#凡是浏览器访问的http 请求的 url 地址 是 /sales/orders/ , 
#就由 views.py 里面的函数 listorders 来处理， 返回一段字符串给浏览器
# Create your views here.
def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")