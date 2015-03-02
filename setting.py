import web
import os
#import sae

app_root = os.path.dirname(__file__)
image_path = os.path.join(app_root, 'static/img/dish')
templates_root = os.path.join(app_root, 'templates').replace('\\','/')

urls = (
    '/', 'Index',
    '/admin', 'Admin',
    '/login',          'Login',
    '/logout',         'Logout',
    '/upload',         'Upload',
    '/edit/(.+)',      'Edit',
    '/delete/(.+)',    'Delete',
    '/regist',         'Regist',
    '/addmenu/(.+)',   'Add',
    '/minusmenu/(.+)', 'Minus',
    '/shopping',       'Shopping',
    '/order',          'Order',
)

menu_table='menu'
user_table='user'
menu_sort_table='menu_sort'
#db = web.database(dbn='mysql', db = sae.const.MYSQL_DB, host = sae.const.MYSQL_HOST, port = int(sae.const.MYSQL_PORT), user = sae.const.MYSQL_USER, pw = sae.const.MYSQL_PASS)
db = web.database(dbn='mysql', db='webdb', host='localhost', port=3306, user='root', pw='123456')

store=web.session.DiskStore('session')
sqlstore=web.session.DBStore(db, 'sessions')
