from datetime import datetime
from sqlalchemy import create_engine  # 创建连接引擎
from sqlalchemy import Column  # 生成列
from sqlalchemy import Integer, DateTime, String, ForeignKey, Boolean, and_, or_ # 定义列类型
from sqlalchemy.ext.declarative import declarative_base  # 基类
from sqlalchemy.orm import relationship, sessionmaker  # 表示关系
from api.db import db_pwd, db_user, ip_port, ip_address

address_engine = 'mysql+pymysql://' + db_user + ':' + db_pwd + '@' + ip_address + ':' + ip_port + '/conceal_web'

engine = create_engine(address_engine, echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    password = Column(String(20))
    email = Column(String(100))

    def __repr__(self):
        return '<User {} : {}>'.format(self.id, self.name)


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    password = Column(String(20))
    description = Column(String(100))
    posts = relationship('Post', back_populates="category")

    def __repr__(self):
        return '<Category {} : {}>'.format(self.id, self.name)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    author = Column(String(50))
    source = Column(String(100))
    source_url = Column(String(100))
    topic_img = Column(String(100))
    summary = Column(String(100))
    body = Column(String(1000), nullable=False)
    tags = Column(String(100))
    hits = Column(Integer, default=0)
    visible = Column(Boolean, default=True)
    featured = Column(Boolean, default=False)
    recommended = Column(Boolean, default=False)
    chosen = Column(Boolean, default=False)
    created_time = Column(DateTime, default=datetime.now)
    category = relationship('Category', back_populates="posts")

    def __repr__(self):
        return '<Post {} : {}>'.format(self.id, self.title)


if __name__ == '__main__':

    Base.metadata.create_all(engine)
    # 建表
    user = User()
    user.name = "Tom"
    user.password = "123456"
    user.email = "tom@@cod.cn"
    session.add(user)
    session.commit()
    # 插值
    '''
    基本查询
    '''
    session.query(Post).all()
    # 查询所有信息
    for d in session.query(Post).all():
        # 每个Post都列出来放在每一个类的实例中
        print(d)
        # 直接调用了repr函数
        print('<Post {} : {}>'.format(d.id, d.title))
    # 查询所有id 和 title
    for d in session.query(Post.title).all():
        print(d)
    # 查询所有title
    for d in session.query(Post.title, Post.title).all():
        print(d)
        print(d.title)
    # return tuple or namedtuple
    for d in session.query(Post.title.label('哈哈')).all():
        print(d.哈哈)
    # 给列取别名
    for d in session.query(Post).order_by(Post.id)[:10]:
        print(d)
    # 正序
    for d in session.query(Post).order_by('post_id desc')[:10]:
        print(d)
    # 倒序

    for d in session.query(Post).filter(Post.id == '123'):
        print(d)
    SQL = "select * from Post WHERE id = '123'"
    # 查询 id 为 123

    for d in session.query(Post).filter(Post.id != '123'):
        print(d)
    SQL = "select * from Post WHERE id != '123'"
    # 不等于

    for d in session.query(Post).filter(Post.id.like('%2%')):
        print(d)
    SQL = "select * from Post WHERE id LIKE '123%'"
    SQL = "select * from Post WHERE id LIKE '123'"
    # 模糊查询

    SQL = "select * from Post WHERE id in('123','123')"
    # 包含
    SQL = "select * from Post WHERE id NOT in('123','123')"
    # 不包含
    for d in session.query(Post).filter(Post.name.in_(['123', '321'])):
        print(d)
    # 包含
    for d in session.query(Post).filter(~Post.name.in_(['123', '321'])):
        print(d)
    # 不包含

    SQL = "select * from Post WHERE name = '123' and id = '123'"
    for d in session.query(Post).filter(Post.name == "123",Post.id == "332"):
        print(d)
    for d in session.query(Post).filter(Post.id == "332").filter(Post.name == "123"):
        print(d)
    for d in session.query(Post).filter(and_(Post.id == "123", Post.name == "123")):
        print(d)
    # 与
    SQL = "select * from Post WHERE name = '123' OR id = '123'"
    for d in session.query(Post).filter(or_(Post.id == "123", Post.name == "123")):
        print(d)
    query = session.query(Post).filter(Post.id == 1)
    query.first()
    query.one() # 如果有两条就报错
    query.one_or_none()
    # 统计**人有多少条
    SQL = "select count(*) from Post WHERE name = '123'"
    query.scalar()