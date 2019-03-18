# 这是启动和管理项目的操作代码
from app import create_app,db
# 通过Manager()管理项目并增加数据迁移命令
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate


