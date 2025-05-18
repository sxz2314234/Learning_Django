from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name=models.CharField(max_length=64)
    password=models.CharField(max_length=64)
    age=models.IntegerField()

"""
上述创建类相当于创建表：
create table app01_userinfo(
    id bigint auto_increment primary key,
    name varchar(64),
    password varchar(64），
    age int,
)
"""

class Department(models.Model):
    title=models.CharField(max_length=16)

# 新建数据：insert into app01department(title)values("销售部")
# Department.objects.create(title="销售部")
