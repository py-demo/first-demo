# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, ForeignKey, MetaData, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.sql import text

import uuid

eis = dict()


class UserObject:
    def __init__(self):
        connstr = eis["connectionstring"]

        self.engine = create_engine(connstr)

        self.dbo = self.engine.connect()

        self.metadata = MetaData()

        # 表对象

        self.metadata.create_all(self.engine)

        pass

    def create(self,name, desc):
        pass

    def delete(self, tid):
        pass

    def edit(self, tid, name, desc):
        pass

    def select4id(self, tid):
        pass

    def select4name(self, name):
        pass

    def select4all(self):
        pass
