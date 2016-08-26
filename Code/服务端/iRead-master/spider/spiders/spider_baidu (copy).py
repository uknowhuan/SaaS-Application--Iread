#coding:utf-8
__author__ = 'jdd'

import urllib
import time
import sys
from bs4 import BeautifulSoup


class Time_service():
    #获取帖子的最新更新时间
    def get_last_time(self,turl,url):
        url = turl+url
        html_content =urllib.urlopen(url).read()
        soup = BeautifulSoup(html_content)
        print url
        print '0 ======================================='
        last_page_url = turl + soup.find('div',class_='pb_footer').find('ul',class_='l_posts_num').find_all('a')[-1]['href']
        print '1 *******************'
        print last_page_url
        html_content2 =urllib.urlopen(last_page_url).read()
        soup2 = BeautifulSoup(html_content2)
        print '2 *******************'
        datetime = soup2.find_all('div',class_='l_post l_post_bright ')[-1]['data-field']
        index = datetime.index('date')
        datetime =  datetime[index+7:index+23]
        print datetime
        print '3 *******************'
        #sys.exit()
        return datetime

class Down_Baidu_Forum():
    """mullti thread download"""
    def __init__(self, url, totime):
        #threading.Thread.__init__(self)
        self.url = url
        self.deadline = totime
        self.lasttime = 0

    def getNewTime(self):
        return self.lasttime

    #return the Next page url or False
    def start_load(self, p_url, reList, first, turl):
        f_url = self.url + p_url
        print 'downling from %s' % f_url

        #爬去网页
        html_content = 3
        while html_content > 0:
            html_content -= 1
            try:
                html_content =urllib.urlopen(f_url).read()
                break
            except Exception as e:
                print('Unable to download data [Time:%d][%s]' % (html_content, f_url))

        #判断是否爬去成功
        if isinstance(html_content, int):
            print('Unable to save data [%s]' % f_url)
            return False

        print 'downling successfully'

        #解析网页
        soup = BeautifulSoup(html_content)
        all_a = soup.find_all('a',class_='j_th_tit')
        post_urls = []
        for a in all_a:
            post_urls.append(a['href'])
        print '4 ======================================='
        topic_url = soup.find('a',class_='th_tit')['href'].replace(turl,'')
        post_urls.append(topic_url)
        #sys.exit()
        

        #获取next page url
        next_page = None
        nps = soup.find('div', class_="pager clearfix").find_all('a')

        next_page = soup.find('a', class_="next")['href']
        #print next_page
        print '5 ======================================='

        #获取每个帖子的url
        timestamp = 0
        for post_url in post_urls:
            try:
                time_service = Time_service()
                print '6 ======================================='
                rt = time_service.get_last_time(turl, post_url)
                print 'rt='+rt
                print '7 ======================================='

                if((first) and (timestamp == 0)):
                    timeArray = time.strptime(rt, "%Y-%m-%d %H:%M")
                    timestamp = int(time.mktime(timeArray))
                    self.lasttime = timestamp
                timeArray = time.strptime(rt, "%Y-%m-%d %H:%M")
                timestamp = int(time.mktime(timeArray))

                #判断截止时间   只获取得到第一个帖子时的镜像
                if(timestamp < self.lasttime):
                    #如果该帖的最新时间大于上次的截止时间
                    if(timestamp >= self.deadline):
                        reList.append(purl)
                    else:
                        return False
            except Exception as e:
                continue
        return next_page
        print 'analyze successfully'

#更新截止时间
def setDeadline(filename, toTime):
    tx_file = open(filename, 'w')
    tx_file.write(str(toTime))
    tx_file.close()

#获取截止时间
def getDeadline(filename):
    try:
        tx_file = open(filename, 'r')
        toTime = tx_file.readline()
        tx_file.close()
    except Exception as e:
        return 0
    return int(toTime.strip())

def write_list(tx_list, fn):
    """把列表内容写入文本"""
    tx_file = open(fn, 'a+')
    for tx in tx_list:
        tx_file.write(tx.strip()+'\n')
    tx_file.close()

def scanItemUrl(url, initDeadline = 1414640120):
    print 'start。。。'

    #the root url
    turl = 'http://tieba.baidu.com'

    #截止时间的存储目录文件
    dir = './data/'
    filename = dir+url[1:]

    # 获取的帖子URL列表
    urlList = []

    #获取更新时间
    deadline = getDeadline(filename)

    #初始化更新时间
    if deadline is 0:
        deadline = initDeadline
    print deadline

    #顺序读取帖子列表页，获取解析帖子URL直到截止时间
    downlist = Down_Baidu_Forum(turl, deadline)
    next_page = downlist.start_load(url, urlList, True, turl)

    print "NEXT Page:%s" % next_page
    if not isinstance(next_page, bool):
        while True:
            next_page = downlist.start_load(next_page, urlList, False, turl)
            print "NEXT:%s" % next_page
            if next_page is None:
                break
            if isinstance(next_page, bool):
                break
    if len(urlList) == 0:
        print 'THE LEN of urlList is 0'
        return False


    #去除帖子列表中的重复项，更新过快的原因
    urlList2 = {}.fromkeys(urlList).keys()

    #写入文件
    write_list(urlList2, './data/postList.txt') 

    print "LEN:", len(urlList2)

    for myurl in urlList2:
        print 'L:%s' % myurl
		
		#此处调用downPage-demo.py,当两个程序调试好后，在此处调用	
		#down_page_run(myurl)

	#更新截止时间
    setDeadline(filename, downlist.getNewTime())

    print 'download FINISH : %s' % url
    return True

def scanItemRun():
    #百度的版块URL
    section = 'http://news.baidu.com/ns?word='

    while True:
        try:
            if scanItemUrl(sec, 1414639980) is False:
                time.sleep(30)
            time.sleep(3)
        except Exception as e:
            print 'scanItemRunERROR ', e

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')

    scanItemRun()
