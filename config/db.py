# coding:utf-8
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

engine = create_engine("mysql+pymysql://root:root@localhost:3306/py_db", echo=True)

db = engine.connect()
metadata = MetaData(engine)

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(20)),
             Column('fullname', String(40)),
             )
address = Table('address', metadata,
                Column('id', Integer, primary_key=True),
                Column('user_id', None, ForeignKey('user.id')),
                Column('email', String(128), nullable=False)
                )
metadata.create_all()

create = db.execute("insert into user() VALUE('%s','%s','%s')") % ('','saturn','saturn.eich')

select = db.execute('select * from user')
for row in select:
    print(row)