import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class QSBK():
    def __init__(self):
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    def get_code(self,index=1):
        self.url="http://www.qiushibaike.com/8hr/page/"
        request=urllib2.Request(self.url+str(index),headers=self.header)
        code=urllib2.urlopen(request).read()
        return code
        
    def get_essence(self,index=1):
        code=self.get_code(index)
        find_essence=re.compile('<h2>(.*?)</h2>.*?<div.*?>\s*(.*?)<!.*?>',re.S)
        essence=find_essence.findall(code)
        for i in essence:
            print i[0].encode('gbk')+'\n'
            print i[1].encode('gbk')
            print '-'*50
        return essence
        
        
        
t=QSBK()
t.get_essence()