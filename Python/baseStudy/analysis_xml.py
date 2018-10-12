#!/usr/bin/env python3    #linux使用，window忽略
# -*- coding: utf-8 -*-

from pyquery import PyQuery as pq
with open('E:/1.txt', 'r',encoding='utf-8') as f:
	data = f.read()
	d = pq(data)
	#获取正文内容
	body1 =d('body')
	#获取标题，有多个，这里需要 书名
	body2 =body1('.hanghang-za-title').eq(0).text()
	print(body2)
	
	#获取书籍简介
	body2 =body1('.hanghang-shu-content-font').text()
	s = body2.split()
	n=0
	print(s )
	# for s.len():


	# while n<3:
	# 	s2=s1.split('：')
	# 	print(s2 )
	# 	print("\n")
	# 	n++
	

	#获取下载地址，此处是百度云盘的
	body3=body1('.hanghang-shu-content-btn')
	body4=body3('a').attr('href')
	print(body4)
