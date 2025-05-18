'''
Author: git config sxz2314234.name && git config 3218635958@qq.com
Date: 2025-05-16 20:01:47
LastEditors: git config sxz2314234.name && git config 3218635958@qq.com
LastEditTime: 2025-05-17 09:41:34
FilePath: \Learning_Django\mysite\app01\views.py
Description: 

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def user_list(request):
    # 1. 去app01目录下的templates目录下找（根据app的注册顺序，逐一去他们的templates目录下找）
    return render(request,'user_list.html')

def tpl(request):
    name="sxz"
    roles=["admin","user","CEO"]
    user_info={
        "name":"sxz",
        "age":18,
        "salary":10000,
    }
    
    return render(request,'tpl.html',{"n1":name,"n2":roles,"n3":user_info})

def news(request):
    import requests
    import json
    
    data_list = requests.get("http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2021/11/news").json()
    return render(request,'news.html',{"news_list":data_list})

def something(request):
# request是一个对象，封装了用户通过浏览器发送过来的所有数据
    
    # 1. 获取请求方式 Get/Post
    print(request.method)
    
    # 2. 在URL上传递值 /something/?n1=123&n2=456
    print(request.GET) # <QueryDict: {'n1': ['123'], 'n2': ['456']}>
    
    # 3.通过请求体中传递数据
    print(request.POST) 
    
    # 4. [响应]HttpResponse("Hello World")，内容字符串返回给请求者。
    # return HttpResponse("Hello World")

    # 5. [响应]读取HTML的内容 + 渲染（替换）-> 字符串，返回给用户浏览器
    # return render(request,'something.html',{"title":"Hello World"})
    
    # 6.[响应]让浏览器重定向其他页面
    return redirect('http://www.baidu.com')

def login(request):
    # 1. 获取请求方式
    if request.method == "GET":
        return render(request,'login.html')
    else:
        # 2. 获取用户名和密码
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # 3. 验证用户名和密码
        if username == "sxz" and password == "123":
            return redirect("http://www.baidu.com")
        else:
            return render(request,'login.html',{"err_msg":"用户名或密码错误"})


from app01.models import Department,UserInfo
def orm(request):
    # ###### 1.新建数据 ######
    Department.objects.create(title="市场部")
    UserInfo.objects.create(name="sxz",password="123456",age=18)
    """
    # ###### 2.删除数据 ######
    UserInfo.objects.filter(name="sxz").delete()
    Department.objects.filter(title="市场部").delete()
    
    # ###### 3.获取数据 ######
    data_list = [对象,对象,对象]  为QuerySet对象
    data_list = UserInfo.objects.all() # 获取所有对象
    for obj in data_list:
        print(obj.name,obj.password,obj.age)
    
    row_obj = UserInfo.objects.filter(id=1).first() # 获取单个对象
    print(row_obj.name,row_obj.password,row_obj.age)
    
    # ###### 4.更新数据 ######
    UserInfo.objects.filter(id=1).update(name="sxz",password="123456",age=18)
    """
    return HttpResponse("ok")

def users_list(request):
    # 1. 获取所有用户
    data_list = UserInfo.objects.all()
    
    # 2. 渲染数据
    return render(request,'users_list.html',{"users":data_list})

def user_add(request):
    # 1. 获取请求方式
    if request.method == "GET":
        return render(request,'user_add.html')
    else:
        # 2. 获取用户名和密码
        username = request.POST.get("user")
        password = request.POST.get("password")
        age = request.POST.get("age")
        
        # 3. 新建用户
        UserInfo.objects.create(name=username,password=password,age=age)
        
        # 4. 重定向到用户列表页面
        return redirect("/users/list/")
    
def user_delete(request):
    uid=request.GET.get("uid")
    UserInfo.objects.filter(id=uid).delete()
    
    return redirect("/users/list/")