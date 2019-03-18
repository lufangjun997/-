# 这是启动和管理项目的操作代码
from app import create_app,db
# 通过Manager()管理项目并增加数据迁移命令
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
# 导入所有实体类方便使用db指令做迁移
from app import models

# 调用create_app得到一个app实例
app = create_app()
# 创建Manager的实例对象, 用于托管app
manager = Manager(app)
# 创建Migrate对象, 用于关联管理的app和db
migrate = Migrate(app,db)
# 再通过Manager的对象增加db迁移指令
manager.add_command('db',MigrateCommand)
if __name__ == "__main__":
    # 使用Manager实例启动程序
    manager.run()