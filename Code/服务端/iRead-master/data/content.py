# coding=utf-8
"""
Created on 2014-12-19

@author: guan
"""
import core.db as db
import json

def get_list(env,params):
    result = {}
    temp={}
    try:
        conn=db.DB()
        userid = params['session_id'][0]
        start_time = params['start_time'][0]
        end_time = params['end_time'][0]
        start_num = int(params['start_num'][0])
        num = int(params['num'][0])
        
        sql = "select c.* from content c where c.id in (select kwc.content_id from key_word_content kwc where kwc.key_word_id in(select ukw.key_word_id from user_key_word ukw where ukw.user_id = (select u.id from user u where u.userid = %s))) and c.update_time < %s limit %s,%s"

        data = conn.read(sql,(userid,start_time,start_num,num))
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
