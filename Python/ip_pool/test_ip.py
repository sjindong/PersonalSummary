import requests
from bs4 import BeautifulSoup
import socket
import urllib

socket.setdefaulttimeout(3)
#模拟登陆
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24','Referer':'https://www.baidu.com/'}
file=open('D:\python\ZhaoHeng\\ip pool.txt',"r")
lines=file.readlines()
proxys = []
for i in range(0,len(lines)):
    proxy_host ='http://'+ lines[i].replace("\n","")
    #proxy_host2 = +lines[i]
    proxy_temp = {"http":proxy_host}
    proxys.append(proxy_temp)
url = "http://ip.chinaz.com/getip.aspx"
# 将可用ip写入valid_ip.txt
for proxy in proxys:
    try:
        res = requests.get(url,proxies=proxy,headers=header)
        valid_ip = proxy['http'][7:]
        ouf = open("D:\python\ZhaoHeng\\valid_ip.txt", "a+")
        print('valid_ip:' + valid_ip)
        ouf.write(valid_ip+'\n')
        ouf.close()
    except Exception as e:
        print(proxy)
        print(e)
        continue

