# coding=utf-8
'''
Created on 2014-12-19

@author: guan
'''
import core.db as db
import database
import spiders.spider_baidu as baidu
import sys

def hunt():
    print '*****************************'
    print 'spider is hunting...'
    print '*****************************'
    data = database.get_all_key_word()
    if not data is None:
        for i in range(len(data)):
            baidu.scan_by_kw(data[i]['id'], data[i]['kw'])
