from sqlalchemy import Column, Integer, VARCHAR, DateTime
from sqlalchemy.databases import mysql
from sqlalchemy.ext.declarative import declarative_base
import time

# 实例化 声明性类定义 - 构造基类
Base = declarative_base()  # 声明一个数据库映射（生成一个ORM基类）


class Documents(Base):  # 定义Documents子类, 继承Base类
    """Documents表字段、关系 ORM设置"""
    __tablename__ = "documents"  # 指定本类映射到documents表

    uuid = Column(VARCHAR(), primary_key=True, nullable=False)
    create_time = Column(DateTime(), nullable=False)
    update_time = Column(DateTime(), nullable=False)
    permission_level = Column(Integer(), nullable=False)
    content = Column(mysql.MSMediumText, nullable=True)
    type = Column(VARCHAR(), nullable=False)
    click_amount = Column(Integer(), nullable=False)


class Initialize:  # 封装 MailDB数据表 初始化、创建、删除操作 工具类
    """MailDB数据表初始化、创建、删除操作"""
    from sqlalchemy import create_engine

    def __init__(self):
        self.engine = self.create_engine('mysql+pymysql://root:@localhost:3306/project_name', echo="utf-8" )

    def create(self):
        """生成/初始化数据表"""
        print("开始进行生成/初始化数据表操作...")
        Base.metadata.create_all(self.engine, checkfirst=True)  # （若该表不存在时）创建所有继承自Base的表
        print("生成/初始化数据库成功！")

    def drop_all(self):
        """删除数据表"""
        print("开始进行删除数据表操作...")
        # 删除数据表
        Base.metadata.drop_all(self.engine)  # （若该表存在时）删除所有继承自Base的表
        print("删除数据库成功！")

    def initialize(self):
        """初始化数据表（先删后建）"""
        self.drop_all()
        self.create()


# 新增
class Create:
    pass


# 检索
class Retrieve:
    pass


# 更新
class Update:
    pass


# 删除
class Delete:
    pass


if __name__ == '__main__':
    Initialize.initialize()
