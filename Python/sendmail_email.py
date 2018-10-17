from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText    
from email.mime.image import MIMEImage

# 学习路径 ：https://www.cnblogs.com/yufeihlf/p/5726619.html

# Message
# +- MIMEBase
#    +- MIMEMultipart
#    +- MIMENonMultipart
#       +- MIMEMessage
#       +- MIMEText
#       +- MIMEImage

#添加普通文本
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com"    
text_plain = MIMEText(text,'plain', 'utf-8')  

#添加超文本
html = """
<html>  
  <body>  
    <p> 
       Here is the <a href="http://www.baidu.com">link</a> you wanted.
    </p> 
  </body>  
</html>  
"""    
text_html = MIMEText(html,'html', 'utf-8')

#添加附件
sendfile=open(r'D:\pythontest\1111.txt','rb').read()
text_att = MIMEText(sendfile, 'base64', 'utf-8')    
text_att["Content-Type"] = 'application/octet-stream'    
text_att["Content-Disposition"] = 'attachment; filename="显示的名字.txt"' 

#添加图片
sendimagefile=open(r'D:\pythontest\testimage.png','rb').read()
image = MIMEImage(sendimagefile)
image.add_header('Content-ID','<image1>')

#设置邮件类型 
# multpart说明
# 常见的multipart类型有三种：multipart/alternative, multipart/related和multipart/mixed。
# 邮件类型为"multipart/alternative"的邮件包括纯文本正文（text/plain）和超文本正文（text/html）。
# 邮件类型为"multipart/related"的邮件正文中包括图片，声音等内嵌资源。
# 邮件类型为"multipart/mixed"的邮件包含附件。向上兼容，如果一个邮件有纯文本正文，超文本正文，内嵌资源，附件，则选择mixed类型
msg = MIMEMultipart('mixed')

# 必须把Subject，From，To，Date添加到MIMEText对象或者MIMEMultipart对象中，邮件中才会显示主题，发件人，收件人，时间（若无时间，就默认一般为当前时间，该值一般不设置）
msg = MIMEMultipart('mixed') 
msg['Subject'] = 'Python email test'
msg['From'] = 'XXX@163.com <XXX@163.com>'
msg['To'] = 'XXX@126.com'
msg['Date']='2012-3-16'
