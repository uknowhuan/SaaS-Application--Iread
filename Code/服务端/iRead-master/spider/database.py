# coding=utf-8
'''
Created on 2014-12-19

@author: guan
'''
import core.db as db
import time

def get_all_key_word():
    data = None
    try:
        conn=db.DB()
        sql = "select * from key_word"
        data = conn.read(sql)
        return data
    except Exception, e:
        print e
        return data


def add_content(kw_id,url,title,summary,update_time):
    print 'add new content'
    try:
        conn=db.DB()
        create_time = time.strftime('%Y-%m-%d %H:%M:%S')

        sql = "insert into content(url,title,summary,create_time,update_time) values(%s,%s,%s,%s,%s)"
        data = conn.write(sql,(url,title,summary,create_time,update_time))
        if data==1:
            sql1 = "select max(id) from content"
            data1 = conn.read(sql1) 
            content_id = data1[0]['max(id)']

            sql2 = "insert into key_word_content(key_word_id,content_id) values(%s,%s)"
            data2 = conn.write(sql2,(kw_id,content_id))
            if data2==1:
                print 'success'
            else:
                print 'error'
        else:
            print 'error'
    except Exception, e:
        print e
 
    
