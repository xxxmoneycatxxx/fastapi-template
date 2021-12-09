from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time

# 实例化 声明性类定义 - 构造基类
Base = declarative_base()  # 声明一个数据库映射（生成一个ORM基类）


class Mail(Base):  # 定义Mail子类, 继承Base类
    """Mail表字段、关系 ORM设置"""
    __tablename__ = "mail"  # 指定本类映射到mail表
    id = Column(Integer, primary_key=True)  # id 整数、主键 整数主键默认自动增长
    update_time = Column(String(16))  # 信息更新时间 16位字符串
    status = Column(String(20))  # 邮件状态 20位字符串
    send_date = Column(String(10))   # 寄出日期 10位字符串
    received_date = Column(String(10))  # 送达日期 10位字符串
    room = Column(String(20))  # 所属庭室 20位字符串
    area = Column(String(20))  # 行政区划 20位字符串
    year = Column(String(20))  # 案件年度 20位字符串
    num = Column(String(20))  # 案件号 20位字符串
    to = Column(String(20))  # 寄送对象
    nu = Column(String(13))  # 邮件编码
    item = Column(String(64))  # 寄送内容
    detail = Column(String(9999))  # 投递详情
    is_follow = Column(Integer)  # 是否关注


class Initialize:  # 封装 MailDB数据表 初始化、创建、删除操作 工具类
    """MailDB数据表初始化、创建、删除操作"""
    from GlobalSetting import db_path
    from sqlalchemy import create_engine

    def __init__(self):
        self.engine = self.create_engine('sqlite:///%s?check_same_thread=False' % self.db_path, echo=False, )

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
