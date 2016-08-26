# coding=utf-8
"""
Created on 2014-12-19

@author: guan
"""
import core.db as db
import json
import hashlib

def login(env,params):
    result = {}
    try:
        conn=db.DB()
        email=params['email'][0]
        pwd=params['pwd'][0]
        sql = "select userid,nickname,pwd from user where email=%s"
        data = conn.read(sql,(email))
        temp={}
        if pwd==data[0]['pwd']:
            temp['login']='success'
            temp['session_id']=data[0]['userid']
            temp['nickname']=data[0]['nickname']
        else:
            temp['login']='fail'
            temp['session_id']=""
            temp['nickname']=""
        result['data']=temp
        result['ret']=0
        result['msg']='ok'
        json_result=json.dumps(result)
        conn.close()
        return json_result
    except Exception, e:
        print e
        result['ret']=1
        result['msg']=str(e)
        json_result=json.dumps(result)
        return json_result
