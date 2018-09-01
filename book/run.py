import pymysql

pymysql.install_as_MySQLdb()

from flask_script import Manager  # 可以将flask项目用命令行的方式进行数据库的更新和其他的一些操作，比如说启动服务器
from flask_migrate import Migrate, MigrateCommand  # 导入migrate相关的模块,数据库迁移相关模块

from config.app import app

from models.db import db
from models.model import *  # 从models导入数据库模型（数据库要创建的表）

migrate = Migrate(app, db)  # 将数据库和app关联起来

import viewsmodel.views

db.init_app(app)  # db和app
# 让flaskapp支持命令行工作
manager = Manager(app)

# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)


# db.create_all()


# 自定义命令 python 文件 runserver
@manager.command
def runserver():
    app.run(debug=True, host='127.0.0.1', port=8888, threaded=True)  # 此处 threaded=True 为多线程启动


if __name__ == '__main__':
    manager.run()

# 运行相关的命令
# 初始化: python manage.py db init

# 创建迁移脚本: python manage.py db migrate

# 更新数据库: python hello.py db upgrade
# 第一次迁移实际上相当于调用db.create_all()，但在后续迁移中，upgrade命令对表实施更新操作但不影响表中的内容。


# 用脚本管理数据库和model的引入
# 1、导入from flask_script 、flask_migrate
# 2、migrate = Migrate(app,db) 关联数据库和应用
# 3、manager = Manager(app) #让flaskapp支持命令行工作
# 4、manager.add_command('db',MigrateCommand）将数据库迁移的命令导入到manager
# 5、用脚本管理起来 manager.run()
