from django.shortcuts import render

from django.http import HttpResponse
#导入数据库
from common.models import Customer
#导入引擎
from django.template import engines
#*****************************************************************
# 先定义好HTML模板
html_template ='''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>id</th>
        <th>姓名</th>
        <th>电话号码</th>
        <th>地址</th>
        </tr>

        {% for customer in customers %}
            <tr>

            {% for name, value in customer.items %}            
                <td>{{ value }}</td>            
            {% endfor %}
            
            </tr>
        {% endfor %}
                
        </table>
    </body>
</html>
'''

django_engine = engines['django']
template = django_engine.from_string(html_template)
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

def listcustomersWithGUI1(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    # 检查url中是否有参数phonenumber
    ph =  request.GET.get('phonenumber',None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phonenumber=ph)

    # 传入渲染模板需要的参数
    rendered = template.render({'customers':qs})

    return HttpResponse(rendered)