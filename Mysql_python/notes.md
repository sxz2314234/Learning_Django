<!--
 * @Author: git config sxz2314234.name && git config 3218635958@qq.com
 * @Date: 2025-05-17 12:44:52
 * @LastEditors: git config sxz2314234.name && git config 3218635958@qq.com
 * @LastEditTime: 2025-05-17 19:23:15
 * @FilePath: \Learning_Django\Mysql_python\notes.md
 * @Description: 
 * 
 * Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
-->
# 1.忘记密码
```
默认情况下,启动Mysql时，需要用户输入账户名、密码。
修改Mysql设置，重新启动Mysql（无账号）：
    mysql -u root -p
    重新设置密码
    退出

再重新修改Mysql配置文件，重新启动Mysql（需要账号的模式）
    mysql -u root -p
    新密码
```

# 2.数据库管理（文件夹）
- 查看已有的数据库（文件夹）
```
show databases;
```

- 创建数据库（文件夹）
```
create database 数据库名字 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```
- 删除数据库
```
drop database 数据库名字;
```
- 进入数据库（文件夹）
```
use 数据库名字
```
- 查看数据库（文件夹）中所有的数据表（文件）
```
show tabales;
```
# 数据表的管理（文件）
- 创建表（文件）
```
create table 表名称（
    列名称 类型，
    列名称 类型，
    列名称 类型
)default charset=utf8;
```
**例子：**
```
note:所创建的表的元素分别是：id,name,age
create table tb1(id int,name varchar(16),age int)default charset=uft8;

【标准】
create table tb1(
    id int primary key(主键),  -- 不允许为空且唯一，同时可以使用auto_increment实现自增
    name varchar(16) not null, -- 不允许为空
    age int default 3 -- 默认值为3
)default charset=uft8;
```
- 删除表
```
delete table 表名；
```

- 展示表的性质
```
desc 表名
```
- 插入数据
```
insert into tb2(salary,age) value(10000,18);

<!-- 批量插入 -->
insert into tb2(salary,age) value(20000,19),(30000,31),(40000,41);
```
- 查看表中数据
```
select * from tb2;
```

## 常用的数据类型
- tinyint
    ```
    大小为1个字节
    默认为有符号的，
    如果要无符号则为：tinyint unsigned
    ```
- int
    ```
    大小为4字节；
    其他同上
    bigint 大小更大.
    ```
- float
- double
- decimal
    ```
    准确的小数值
    decimal(数字的总个数，小数点后几位)
    数字总个数最大为65，小数点后最多30位（四舍五入）
    ```
## 存储字符串
- char(m)
    ```
    定长字符串,m最大为255
    表示固定存储长度
    优点：查询速度快
    ```
- varchar(m)
    ```
    动态字符串,与编码有关
    真实的数据有多大就按多大存储
    优点：节省存储空间
    ```
- text
    ```
    text数据类型用于保存变长的大字符串，可以最多到65535（2**16-1）个字符。
    一般情况下，长文本会用text类型。例如：文章，新闻等。
    ```
- mediumtext
- longtext
- datatime(时间，精确到时分秒)
- date(时间：年月日)

## 练习：用户表
```
create table tb3(
    id int not null auto_increment primary key,
    name varchar(64) not null,
    password varchar(64) not null,
    email varchar(64) not null,
    age tinyint,
    salary decimal(10,2),
    ctime datetime
)default charset=utf8;
```

# 数据行操作
## 1.新增数据
```
insert into 表名(列名，列名) values(值，值),(值,值);
```

## 2.删除数据
```
delete from 表名; // 表示删除整张表
delete from 表名 where 条件; // 删除满足条件的
(and or 与或 )

或者：
drop table 表名;
```

## 3.修改数据
```
update 表名 set 列=值；
update 表名 set 列=值 where 条件;

例：update tb3 set age=age+10 where id>5;
```

## 4.查询数据
```
select * from 表名; // 查询表中所有数据
select 列名 from 表名;
select 列名 from 表名 where 条件;
```


