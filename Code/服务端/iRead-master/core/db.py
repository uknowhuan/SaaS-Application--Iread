# coding=utf-8
#import MySQLdb
import MySQLdb.cursors
from settings import DATABASE

class DB():
    def __init__(self):
        """
        初始化连接
        """
        try:
            self.conn = MySQLdb.connect(
                host=DATABASE['HOST'],
                user=DATABASE['USER'],
                passwd=DATABASE['PWD'],
                db=DATABASE['DB'],
                cursorclass=MySQLdb.cursors.DictCursor,
                init_command='set names utf8'
            )
        except Exception, e:
            #print 'Connection Exception:', e
            raise e

    def read(self, sql, params=None, isencode=False):
        """
        查询数据
        @sql:sql语句
        @params:参数,元组类型
        """
        try:
            if isencode and params:
                array = list(params)
                for i in range(len(array)):
                    if type(array[i]) == unicode:
                        array[i] = array[i].encode('utf-8')
                params = tuple(array)
                #print sql
            #print params
            cur = self.conn.cursor()
            count = cur.execute(sql, params)
            data = cur.fetchall()
            cur.close()
            return data
        except Exception, e:
            raise e

    def write(self, sql, params=None, isencode=True, isdata=False):
        """
        写数据库
        @sql:sql语句
        @isencode:是否对参数进行utf-8编码
        @isdata:是否返回数据，否:返回受影响行数
        """
        try:
            if isencode and params:
                array = list(params)
                for i in range(len(array)):
                    if type(array[i]) == unicode:
                        array[i] = array[i].encode('utf-8')
                params = tuple(array)
            cur = self.conn.cursor()
            count = cur.execute(sql, params)
            cur.execute("set autocommit = 1")
            data = cur.fetchall()
            cur.close()
            if isdata:
                return data
            else:
                return count
        except Exception, e:
            self.conn.rollback()
            self.conn.close()
            print 'write Exception:', e
            return {}
            #return geterrMsg(304, e)


    def close(self):
        """
        关闭数据库连接
        """
        try:
            self.conn.close()
        except Exception, e:
            #print 'close connection Exception:', e
            raise e
            return {}
            #return geterrMsg(301, e)
