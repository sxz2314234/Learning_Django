from django.db import models

# Create your models here.
class Department(models.Model):
    """部门表"""
    name = models.CharField(verbose_name="标题",max_length=32)
    
class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名",max_length=16)
    password = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    salary=models.DecimalField(verbose_name="薪水",max_digits=10,decimal_places=2)
    create_time=models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
    
    # 无约束
    # depart_id=models.BigIntegerField(verbose_name="部门id")
    # 1.有约束
    #  - to,与那张表关联
    #  - to_field,与那张表的哪个列关联
    # 2.django自动
    #  - 写的depart
    #  - 生成数据列：depart_id
    # 3.部门表被删除
    # - 3.1级联删除
    # - 3.2置空
    # depart=models.ForeignKey(to="Department",to_field="id",null=true,blank=true,on_delete=models.SET_NULL)
    depart=models.ForeignKey(verbose_name="部门",to="Department",to_field="id",on_delete=models.CASCADE)
    gender=models.SmallIntegerField(verbose_name="性别",choices=((1,"男"),(2,"女")),default=1)