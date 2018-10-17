import smtplib

# 实例化SMTP()
smtp = smtplib.SMTP() 

# connect(host,port):
# host:指定连接的邮箱服务器。常用邮箱的smtp服务器地址如下：新浪邮箱：smtp.sina.com,新浪VIP：smtp.vip.sina.com,搜狐邮箱：smtp.sohu.com，126邮箱：smtp.126.com,139邮箱：smtp.139.com,163网易邮箱：smtp.163.com。
# port：指定连接服务器的端口号，默认为25.
smtp.connect('smtp.163.com,25') 

#登陆邮箱账号密码
smtp.login(username, password) 

# sendmail(from_addr,to_addrs,msg,...):
# from_addr:邮件发送者地址
# to_addrs:邮件接收者地址。字符串列表['接收地址1','接收地址2','接收地址3',...]或'接收地址'
# msg：发送消息：邮件内容。一般是msg.as_string():as_string()是将msg(MIMEText对象或者MIMEMultipart对象)变为str。
smtp.sendmail(sender, receiver, msg.as_string()) 


# quit():用于结束SMTP会话。
smtp.quit()