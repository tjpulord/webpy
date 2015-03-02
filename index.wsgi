# -*- coding: utf-8 -*-
import os
 
import tempfile
import cStringIO
 
def TemporaryFile(mode='w+b', bufsize=-1, suffix="", prefix='', dir=None):
    return cStringIO.StringIO()
tempfile.TemporaryFile = TemporaryFile

import md5
import sae
import web

from setting import *


class content():
    def __init__(self, **args):
        self.title = args.get('title', 'default')
        self.error_msg = args.get('error_msg', None)
        self.dish_list=args.get('dish_list', [])
        self.menu_sort_list=args.get('menu_sort_list', [])

    def set_title(self, title):
        self.title = title

class Index:
    def GET(self):
        if session.login == 100:
            return web.seeother('/admin')
        a = web.input(cid=1)
        cid = int(a.get('cid', 1))
        param=content()
        param.set_title('first page')
        if cid == 1:
            param.dish_list = [r for r in db.select(menu_table)]
        else:
            param.dish_list = [r for r in db.select(menu_table) if r.category_id&cid]
        param.menu_sort_list = [r for r in db.select(menu_sort_table)]
        return render.hello_c(param)


class Admin:
    def GET(self):
        if not session.login:
            return web.seeother('/login')
        if session.login != 100:
            return web.seeother('/')
        a = web.input(cid=1)
        cid = int(a.get('cid', 1))
        param = content(title='Admin')
        if cid == 1:
            param.dish_list = [r for r in db.select(menu_table)]
        else:
            param.dish_list = [r for r in db.select(menu_table) if r.category_id&cid]
        param.menu_sort_list = [r for r in db.select(menu_sort_table)]
        return render.admin(param)

class Logout:
    def GET(self):
        session.kill()
        return web.seeother('/')

class Login():
    def GET(self):
        param = content()
        param.set_title('登录')
        return render.login(param)

    def POST(self):
        a = web.input()
        #print a.keys()
        param = content(title="重新登录")
        if not a.username:
            param.error_msg = 'User name is empty!'
            return render.login(param)
        try:
            user = db.select('user', where='user="%s"'% a.username)[0]
        except Exception, e:
            param.error_msg = 'database error: %s' % e
            return render.login(param)

        if  md5.new(a.password).hexdigest()[-10:] == user.passwd:
            param.dish_list = [r for r in db.select(menu_table)]
            session.login = 1
            if user.nick_name:
                session.username = user.nick_name
            else:
                session.username = a.username
            if user.user == 'root':
                session.login = 100
                return web.seeother('/admin')
            return web.seeother("/")
            #return render.order_page()
        else:
            param.error_msg = "User name or password is wrong."
            return render.login(param)


class Upload():
    def GET(self):
        if session.login != 100:
            return web.seeother('/login')
        return render.upload(None, None)
    def POST(self):
        if session.login != 100:
            return web.seeother('/login')
        a = web.input(image={})
        #print int(a.price), a.maketime, type(a.image)
        if not a.dishname:
            return render.upload('upload error', 'dish name should not be empty!')
        elif not a.price:
            return render.upload('upload error', 'dish price should not be empty!')
        elif not a.maketime:
            a.maketime=0
        # upload the image file
        try:
            filepath = a.image.filename.replace('\\','/')
            fn = filepath.split('/')[-1]
            suffix=fn.split('.')[-1]
            if suffix.lower() not in ('jpg', 'jpeg', 'gif', 'png'):
                raise ValueError, 'The upload file is not correct image'
            #print filepath, fn, image_path
            fout = open('%s/%s' % (image_path, fn), 'wb')
            fout.write(a.image.file.read())
            fout.flush()
            fout.close()
        except Exception,e:
            return render.upload('upload error', 'upload image failed: %s' % e)
        # compute the category value
        cid = 1
        for k in a.keys():
            if k.startswith('category_'):
                cid |= int(a[k])
        try:
            db.insert(menu_table, dish_name=a.dishname, price=int(a.price), \
                   make_time=int(a.maketime), image=fn, category_id=cid)
        except Exception, e:
            return render.upload('upload error', 'database error: %s' % e)
        return render.upload('upload', 'succeed')


class Delete:
    def GET(self, args):
        if session.login != 100:
            return web.seeother('/login')
        # TODO:
        # Add one caution before deleting data from database.
        try:
            db.delete(menu_table, where="nid=%d" % int(args))
        except Exception, e:
            raise e

        referer = web.ctx.env.get('HTTP_REFERER', '/')
        return web.seeother(referer)

class Edit:
    def GET(self, args):
        if session.login != 100:
            return web.seeother('/login')
        if args:
            dish = db.select(menu_table, where='nid=%d' % int(args))
        else:
            dish = db.select(menu_table)

        param=content()
        param.set_title('edit')
        param.dish_list = [r for r in dish]
        param.menu_sort_list = [(r.category, r.category_id) for r in db.select(menu_sort_table)]
        return render.edit(param)

    def POST(self, args):
        param = content(title='Edit - error')
        try:
            args=int(args)
            if args <= 0:
                raise
        except:
            param.error_msg = '%s is not correct' % args
            return render.edit(param)

        a=web.input()
        int_list = ['price', 'make_time']
        vars = {}
        category_id = 0
        for ks in a.keys():
            if ks in int_list:
                vars[ks] = int(a[ks])
            elif ks.startswith('category_'):
                category_id |= int(a[ks])
            elif a[ks]:
                vars[ks] = a[ks]
        vars['category_id'] = category_id
        try:
            db.update(menu_table, where='nid=%d'%args, **vars)
        except Exception, e:
            param.error_msg = 'database error: %s' % e
            return render.edit(param)
        return web.seeother("/admin")


class Regist:
    def GET(self):
        param = content()
        param.set_title('注册')
        return render.regist(param)

    def POST(self):
        param = content()
        param.set_title('Regist')
        a = web.input()
        if not a.username or not a.password:
            param.error_msg = '用户名或密码不能为空'
            return render.regist(param)
        elif a.password != a.repassword:
            param.error_msg = '两次输入秘密不一致'
            return render.regist(param)
        else:
            user = db.select(user_table, where='user="%s"' % a.username)
            if user:
                param.error_msg = '注册用户名已存在，请重新注册！'
                return render.regist(param)
        try:
            pwd = md5.new(a.password).hexdigest()[-10:]
            db.insert(user_table, user=a.username, passwd=pwd, nick_name=a.nickname)
        except Exception, e:
            param.error_msg = 'Database error:%s' % e
            return render.regist(param)
        param.set_title('login')
        param.error_msg = '注册成功，请登录'
        return render.login(param)


class Add:
    def GET(self, nid):
        nid = int(nid)
        if session.login:
            if not session.get('order_dict'):
                session.order_dict = {}
                session.order_dict[nid] = 1
            else:
                if nid not in session.order_dict:
                    session.order_dict[nid] = 1
                else:
                    session.order_dict[nid] += 1
        else:
            return web.seeother('/login')

        referer = web.ctx.env.get('HTTP_REFERER', '/')
        return web.seeother(referer)

class Minus:
    def GET(self, nid):
        nid = int(nid)
        if not session.login:
            return web.seeother('/login')
        if session.order_dict[nid] <= 1:
            del session.order_dict[nid]
        else:
            session.order_dict[nid] -= 1

        referer = web.ctx.env.get('HTTP_REFERER', '/')
        return web.seeother(referer)


class Shopping:
    def GET(self):
        param = content(title='购物清单')
        if not session.login:
            return web.seeother('/login')
        if not session.get('order_dict'):
            param.error_msg = '没有点餐，请返回点餐'
            return render.shopping(param)
        #print 'shopping order_dict:',session.order_dict
        total = 0
        for k in session.order_dict:
            menu = db.select(menu_table, where="nid=%d" % k)[0]
            param.dish_list.append(menu)
            total += menu.price * session.order_dict[k]
        session.total_price = total
        return render.shopping(param)


class Order:
    def GET(self):
        param = content(title='我的订单')
        if not session.login:
            return web.seeother('/login')
        return render.order(param)


app = web.application(urls, globals())

#use session in debug model
if web.config.get('_session') is None:
    session = web.session.Session(app, sqlstore,
              initializer={'login': None, 'order_dict':{}})
    web.config._session = session
else:
    session = web.config._session
def session_hook():
    web.ctx.session = session
app.add_processor(web.loadhook(session_hook))

render = web.template.render(templates_root, base='base', globals={'context': session})

application = sae.create_wsgi_app(app.wsgifunc())

web.config.debug = True