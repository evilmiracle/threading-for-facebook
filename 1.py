#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import threading
import time


class Mythreading(threading.Thread):

    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print "starting thread" + self.name
        threadslock.acquire()
        proxy = urllib2.ProxyHandler({"https": "127.0.0.1:1080"})
        opener = urllib2.build_opener(proxy, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        start = time.time()
        html = urllib2.urlopen('https://www.facebook.com')
        print html.read()
        end = time.time()
        print end - start
        threadslock.release()
        print "End thread" + self.name

threadslock = threading.Lock()
threads = []
def main():
    try:
        thread1 = Mythreading(1, "Thread-1", 1)
        thread2 = Mythreading(2, "Thread-2", 2)
        thread3 = Mythreading(3, "Thread-3", 3)

        thread1.start()
        thread2.start()
        thread3.start()

        threads.append(thread1)
        threads.append(thread2)
        threads.append(thread3)

        for i in threads:
            i.join()
        print 'Exiting Main THread'
    except:
        print 'Error Thread'


if __name__ == '__main__':
    main()
