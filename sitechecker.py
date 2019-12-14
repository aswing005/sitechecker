import urllib.request
import time
#a=input()
while(True):
    try:
        #a=urllib.request.urlopen("url ").getcode()
        a=(urllib.request.urlopen("url").getcode())
        #print(a)
        if(a==200):
            print('site is up')
        time.sleep(90)
    except:
        print('site is down')
        time.sleep(90)
        continue
