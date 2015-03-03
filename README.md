# webpy
一、 运行环境:

  1. python 环境：
    使用的python版本为Python 2.7.9，下载地址：https://www.python.org/downloads/release/python-279/

  2. webpy 安装：
    安装web.py, 下载地址：http://webpy.org/static/web.py-0.37.tar.gz
    解压之后运行安装命令：python setup.py install （python 设置windows环境变量，或是从python的安装目录下运行，例：C:\Python27\python.exe）

    安装完在python shell下测试:
    >>> import web
    没有报错表示安装成功。

  3. mysql 安装：
    mysql 官网下载：http://dev.mysql.com/downloads/installer/
    安装时记住mysql的用户名及密码，以方便命令下登录
    a. mysql服务的启动: net stop mysql 停止：net start mysql
    b. 登陆mysql
      语法如下： mysql -u 用户名 -p 用户密码
      键入命令mysql -u root -p， 回车后提示你输入密码，输入123456，然后回车即可进入到mysql中了，mysql的提示符是：mysql>
      c. 导入数据库
      选择数据库： mysql>use webdb;
      导入数据（注意sql文件的路径）： mysql>source init.sql;

  4. 安装python支持mysql的模块MySQLdb:
    下载地址：http://sourceforge.net/projects/mysql-python/
    >>> import MySQLdb
    没有报错表示安装成功

二、运行程序

  1. windows下运行：
  运行命令（使用webpy内置服务）：c:\Python27\python.exe index.py

