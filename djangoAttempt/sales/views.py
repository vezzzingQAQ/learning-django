from django.shortcuts import render

from django.http import HttpResponse

#导入数据库
from common.models import Customer
#凡是浏览器访问的http 请求的 url 地址 是 /sales/orders/ , 
#就由 views.py 里面的函数 listorders 来处理， 返回一段字符串给浏览器
# Create your views here.
def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")

#实现一个功能：浏览器访问 sales/customers/ ，我们的服务端就返回系统中所有的客户记录给浏览器

#Django 中 对数据库表的操作， 应该都通过 Model对象 实现对数据的读写，而不是通过SQL语句。
#比如，这里我们要获取 customer 表 所有记录， 该表是和我们前面定义的 Customer 类管理的。
def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Customer.objects.values()

    # 定义返回字符串
    retStr = ''
    for customer in  qs:
        #字典提取
        for name,value in customer.items():
            retStr += f'{name} : {value} | '
        retStr += '<br>'

    return HttpResponse(retStr)