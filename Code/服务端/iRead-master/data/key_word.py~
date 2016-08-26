# coding=utf-8
"""
Created on 2014-12-19

@author: guan

"""
import core.db as db
import json
import time

def key_word_list(env,params):
    result = {}
    try:
        conn=db.DB()
        userid = params['session_id'][0]

        sql = "select key_word.* from key_word,user,user_key_word where user.id=user_key_word.user_id and key_word.id=user_key_word.key_word_id and user.userid=%s"
        data = conn.read(sql,(userid))
        for i in range(len(data)):
            data[i]['create_time']=str(data[i]['create_time'])
            data[i]['update_time']=str(data[i]['update_time'])
        result['data']=data
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


def key_word_add(env,params):
    result = {}
    temp={}
    try:
        conn=db.DB()
        userid = params['session_id'][0]
        kw = params['kw'][0]
        kw_type = params['type'][0]
        create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        update_time = create_time
        
        sql0 = "select id from user where user.userid=%s"
        data0 = conn.read(sql0,(userid))
        user_id = data0[0]['id']

        sql = "select * from key_word where key_word.kw=%s"
        data = conn.read(sql,(kw))
        if(len(data)==0):
            print 'data = 0'
            sql1 = "insert into key_word(kw,type,create_time,update_time) values(%s,%s,%s,%s)"
            data1 = conn.write(sql1,(kw,kw_type,create_time,update_time))
            if data1==1:
                sql2 = "select max(id) from key_word"
                data2 = conn.read(sql2) 
                key_word_id = data2[0]['max(id)']
                print key_word_id
        else:
            key_word_id=data[0]['id']

        sql4 = "select * from user_key_word where user_key_word.user_id=%s and user_key_word.key_word_id=%s"
        data4 = conn.read(sql4,(user_id,key_word_id))

        if(len(data4)==0):
            sql3 = "insert into user_key_word(user_id,key_word_id) values(%s,%s)"
            data3 = conn.write(sql3,(user_id,key_word_id))
            if data3==1:
                result['msg']='ok'
                result['ret']=0
                temp['id']=key_word_id
            else:
                result['msg']='fail'
                result['ret']=1
                temp['id']=''
        else:
            result['msg']='key word is existed'
            result['ret']=0
            temp['id']=key_word_id
        result['data']=temp
        
        json_result=json.dumps(result)
        conn.close()
        return json_result
    except Exception, e:
        print e
        result['ret']=1
        result['msg']=str(e)
        json_result=json.dumps(result)
        return json_result


def key_word_delete(env,params):
    result = {}
    temp={}
    try:
        conn=db.DB()
        userid = params['session_id'][0]
        key_word_id = params['id'][0]

        sql0 = "select id from user where user.userid=%s"
        data0 = conn.read(sql0,(userid))
        user_id = data0[0]['id']
        
        sql1 = "delete from user_key_word where user_id=%s and key_word_id=%s"
        data1 = conn.write(sql1,(user_id,key_word_id))
        if data1==1:
            result['msg']='ok'
            result['ret']=0
        else:
            result['msg']='fail'
            result['ret']=1

        result['data']=temp
        
        json_result=json.dumps(result)
        conn.close()
        return json_result
    except Exception, e:
        print e
        result['ret']=1
        result['msg']=str(e)
        json_result=json.dumps(result)
        return json_result


def key_word_update(env,params):
    result = {}
    temp={}
    try:
        conn=db.DB()
        userid = params['session_id'][0]
        key_word_id = params['id'][0]
        kw = params['kw'][0]
        kw_type = params['type'][0]
        update_time = time.strftime('%Y-%m-%d %H:%M:%S')
     
        sql = "update key_word set kw=%s,type=%s,update_time=%s where id=%s"
        data = conn.write(sql,(kw,kw_type,update_time,key_word_id))
        if data==1:
            result['msg']='ok'
            result['ret']=0
        else:
            result['msg']='fail' 
            result['ret']=1

        result['data']=temp
        
        json_result=json.dumps(result)
        conn.close()
        return json_result
    except Exception, e:
        print e
        result['ret']=1
        result['msg']=str(e)
        json_result=json.dumps(result)
        return json_result
