'''
Author: git config sxz2314234.name && git config 3218635958@qq.com
Date: 2025-05-16 20:01:47
LastEditors: git config sxz2314234.name && git config 3218635958@qq.com
LastEditTime: 2025-05-16 22:14:19
FilePath: \Learning_Django\mysite\app01\views.py
Description: 

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''
from django.shortcuts import render,HttpResponse

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