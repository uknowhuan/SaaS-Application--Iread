# coding:utf-8
'''
Created on 2014-12-19

@author: guan
'''
import urllib
import sys
import time,datetime
from bs4 import BeautifulSoup
import spider.database as database

def scan_by_kw(kw_id, kw):
    url = 'http://news.baidu.com/ns?word='+kw
    start_load(kw_id,url)


def start_load(kw_id,url):
    print 'downloading from '+url
    
    html_content = 3
    while html_content > 0:
        html_content -= 1
        try:
            html_content =urllib.urlopen(url).read()
            break
        except Exception as e:
            print('Unable to download data [Time:%d][%s]' % (html_content, url))

    if isinstance(html_content, int):
        print('Unable to save data [%s]' % url)
        return False

    print 'downling successfully'

    soup = BeautifulSoup(html_content)
    posts = []
    posts = soup.find_all('li', class_='result')

    d1 = datetime.datetime.now()
    d2 = d1-datetime.timedelta(hours=1)

    current_time = d1.strftime('%Y-%m-%d %H:%M:%S')
    last_time = d2.strftime('%Y-%m-%d %H:%M:%S')

    for post in posts:
        post_url = post.find_all('a')[0]['href']
        author = post.find_all('p', class_='c-author')[0].text
        date_time = author[-17:]+':00'
        date_time = time.strptime(date_time,'%Y-%m-%d %H:%M:%S')
        date_time = time.strftime('%Y-%m-%d %H:%M:%S',date_time)
        #print date_time
        #print last_time
        if date_time>last_time:
            title = post.find_all('a')[0].text
            summary = post.find_all('div')[0].text[len(author):-16]
            database.add_content(kw_id,post_url,title,summary,date_time)
        else:
            #print 'continue'
            continue
