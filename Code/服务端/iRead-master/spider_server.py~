#coding:utf-8
'''
Created on 2014-12-19

@author: guan
'''
from apscheduler.schedulers.background import BackgroundScheduler
import spider.spider as spider
import time

def test():
    print 'test'


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(spider.hunt, 'interval', seconds=60*60)
    #scheduler.add_job(test, 'interval', seconds=6)
    scheduler.start()

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown() 
