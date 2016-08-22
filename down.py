import re
import requests
import time
import random
import sys

def get_down_links(page_num,keyword):
    url = 'https://github.com/search?l=PHP&p={p}&q={k}&ref=searchresults&type=Repositories'.format(p=page_num,k=keyword)
    #print url
    res = requests.get(url)
    m = re.findall(r'repo-list-name">.*?href="(.*?)">',res.content,re.S)
    return m

if __name__ == '__main__':
    print 'Usage: python down.py KEYWORD PAGE_START PAGE_END'
    keyword = sys.argv[1]
    page_start = int(sys.argv[2])
    page_end = int(sys.argv[3])
    print 'Searching {k} from {s} to {e}'.format(k=keyword,s=page_start,e=page_end)
    for page_num in range(page_start,page_end+1):
        print 'PAGE '+str(page_num)
        m = get_down_links(page_num,keyword)
        for repo in m:
            print "https://github.com"+repo+"/archive/master.zip"
        time.sleep(random.random()*8)
