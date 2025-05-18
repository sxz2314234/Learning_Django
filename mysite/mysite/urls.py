"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from app01 import views
urlpatterns = [
    # path("admin/", admin.site.urls),
    
    # www.xxx.com/index -> 函数
    path('index/',views.index),
    path('user/list/',views.user_list),
    path('tpl/',views.tpl),
    path('news/',views.news),
    path('something/',views.something),
    
    # test: User login
    path('login/',views.login),

    # test: connect database
    path('orm/',views.orm),
    
    #test:user list
    path('users/list/',views.users_list),
    
    #test:user add
    path('user/add/',views.user_add),
    
    #test:user delete
    path('user/delete/',views.user_delete),
]
