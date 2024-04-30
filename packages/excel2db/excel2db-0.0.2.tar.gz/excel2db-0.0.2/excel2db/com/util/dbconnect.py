# -*- coding: utf-8 -*-
"""
数据库连接
在实例化类后，使用时应判断STATUS参数，若参数为0表示连接成功，可以调用
可以使用close方法关闭，也可以等待程序结束后自动关闭
"""
import threading, re

###sqlite
class sqliteCon:
    def __init__(self, dbname):
        """
        :param dbname: 数据库文件路径
        """
        import sqlite3
        self.odbc = sqlite3
        self.dbname = dbname
        self.STATUS = 1  ##判断连接状态，若为1，则未连接，否则已连接

        ###连接数据库
        try:
            self.connect = self.odbc.connect(dbname)
        except Exception:
            self.STATUS = 1
        else:
            self.STATUS = 0

        if not self.STATUS:
            self.cursor = self.connect.cursor()
            self.lock = threading.Lock()

    def close(self):
        if not self.STATUS:
            self.cursor.close()
            self.connect.close()
            self.STATUS = 1

    def acquire(self):
        if not self.STATUS:
            self.lock.acquire()

    def release(self):
        if not self.STATUS:
            self.lock.release()

    def __del__(self):
        if not self.STATUS:
            self.cursor.close()
            self.connect.close()

    def getname(self):
        return self.dbname

    def escape_string(self, st: str):
        return st.replace("'", "''")

class SqlData:
    def __init__(self, dataByRow, dataByCol, columns):
        self.columns = columns
        self.dataByRow = dataByRow
        self.dataByCol = dataByCol