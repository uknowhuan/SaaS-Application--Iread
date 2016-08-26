# coding=utf-8
'''
Created on 2014-12-19

@author: guan
'''
import core.db as db
import json
import random
import time
import uuid

def register(env,params):
    result = {}
    temp={}
    try:
        conn = db.DB()
        userid = str(uuid.uuid1())
        nickname = params['nickname'][0]
        email = params['email'][0]
        pwd = params['pwd'][0]
        create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        update_time = create_time

        sql0 = "select * from user where email=%s"
        data0 = conn.read(sql0,(email))
        if (len(data0)==0):
            sql = "insert into user(userid,nickname,email,pwd,create_time,update_time) values(%s,%s,%s,%s,%s,%s)"
            data = conn.write(sql,(userid,nickname,email,pwd,create_time,update_time))
            if data==1:
                result['msg']='success'
                result['ret']=0
            else:
                result['ret']=1
                result['msg']='sql error'
        else:
            result['msg']='email is existed'
            result['ret']=1
        result['data']=temp
        json_result = json.dumps(result)
        conn.close()
        return json_result
    except Exception, e:
        print e
        result['ret']=1
        result['msg']=str(e)
        json_result=json.dumps(result)
        return json_result
