#!/usr/bin/env python26
#-*- coding:utf-8 -*-
import MySQLdb


create_dish_sql = """create table if not exists menu(
                      nid int(10) not null primary key auto_increment,
                      dish_name varchar(50) not null,
                      price int not null,
                      category_id int(10),
                      make_time int,
                      image varchar(50),
                      comment text)
"""
create_user_sql = """create table if not exists user(
                          uid int(5) not null primary key auto_increment,
                          user varchar(20) not null,
                          passwd varchar(10) not null,
                          nick_name varchar(20),
                          extend text)
"""

create_menu_sorts_sql="""create table if not exists menu_sort(
                         uid int(5) not null primary key auto_increment,
                         category varchar(20) not null,
                         category_id int(10) not null,
                         info text)
"""


def initDB():
    conn = MySQLdb.connect(host='localhost',user='root',passwd='123456')
    cursor = conn.cursor()
    cursor.execute("create database if not exists webdb")

    conn.select_db('webdb')
    cursor.execute(create_dish_sql)
    cursor.execute(create_user_sql)
    cursor.execute(create_menu_sorts_sql)
    #cursor.execute("create table if not exists comment(nid int(10) not null primary key auto_increment,cid int(10) not null,datetime datetime,name varchar(20)  default '??',mail varchar(20) default '??', comment text )")
    #cursor.execute("insert into user(user, passwd) values('custom1', password('123456'))")
    #cursor.execute("insert into menu(dish_name, price, make_time, image)values('salsa', 15, 10, 'salsa.jpg')")
    cursor.close()
    conn.close()

def insert_data_into_menu_sort():
    conn = MySQLdb.connect(host='localhost',user='root',passwd='123456', db='webdb')
    cursor = conn.cursor()

    cate_list = [("全部", 1),
                 ("快餐", 2),
                 ("中餐", 4),
                 ("西餐", 8),
                 ("料理", 16),
                 ("糕点", 32),
                 ("汤类", 64),
                 ("面食", 128),
                 ("饮品", 1024)
    ]
    #sql_str = 'insert into menu_sort(category, category_id) values ("%s", %d)'
    sql_str = 'update table menu_sort set category="%s" where category=%d'
    for item in cate_list:
        cursor.execute(sql_str % (item[0], item[1]))
