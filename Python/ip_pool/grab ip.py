import requests
from bs4 import BeautifulSoup
import os
import time
import re
#模拟登陆
header = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.8;baidu Transcoder) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729)','Referer':'https://baidu.com'}#
kuaidaili_url='https://www.kuaidaili.com/free/'
xicidaili_api='http://api.xicidaili.com/free2016.txt'

#req = urllib2.Request(url=xicidaili_url,headers=headers)
#res = urllib2.urlopen(req).read()
#print(main_page.text)
ip_list=[]
port_list=[]
for i in range(1,200):
 xicidaili_url='http://www.xicidaili.com/wt/'+ str(i)
 main_page = requests.get(xicidaili_url, headers = header)
 bsObj = BeautifulSoup(main_page.text,'html.parser')
 for xxx in bsObj.findAll("tr",{"class":"odd"}):
   ip=xxx.td.next_sibling.next_sibling.get_text().strip()
   ip_list.append(ip)
 for yyy in bsObj.findAll("tr",{"class":"odd"}):
   port=yyy.td.next_sibling.next_sibling.next_sibling.next_sibling.get_text().strip()
   port_list.append(port)
 ip_total=[list(item)for item in zip(ip_list,port_list)]
 f = open('D:\python\ZhaoHeng\\ip pool'+".txt", 'a')
 for li in ip_total:
  ip = li[0]+':'+li[1]+ '\n'
 #print(ip)
  f.write(ip)
 f.close()
 time.sleep(2)
