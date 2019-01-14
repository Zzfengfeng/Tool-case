# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 12:51:56 2019

@author: Zz疯疯
"""

import calendar 
import datetime 
import sys 
  
def getcal(y, m): 
	# 从周日开始 
	cal = calendar.Calendar(6) 
	if not isinstance(y, int): y = int(y) 
	if not isinstance(m, int): m = int(m) 
	if m == 1: # 1月份 
		py = y - 1; pm = 12; 
		ny = y; nm = 2
	elif m == 12: # 12月份 
		py = y; pm = 11
		ny = y + 1; nm = 1
	else: 
		py = y; pm = m - 1
		ny = y; nm = m + 1
	pcal = cal.monthdayscalendar(py, pm) # 上一月 
	ncal = cal.monthdayscalendar(ny, nm) # 下一月 
	ccal = cal.monthdayscalendar(y, m)  # 当前 
	w1 = ccal.pop(0) # 取第一周 
	w2 = ccal.pop() # 取最后一周 
	wp = pcal.pop() # 上个月的最后一周 
	wn = ncal.pop(0) # 下个月的第一周 
	#r1 = [datetime.date(y, m ,w1[i]) or wp[i] for i in range(7)] 
	r1 = [w1[i] and datetime.date(y, m, w1[i]) or datetime.date(py, pm, wp[i]) for i in range(7)] 
	r2 = [w2[i] and datetime.date(y, m, w2[i]) or datetime.date(ny, nm, wn[i]) for i in range(7)] 
 # 转datetime 
	result = [] 
	result.append(r1) # 第一周 
	for c in ccal:  # 其他周 
		result.append([datetime.date(y,m,i) for i in c]) 
		result.append(r2) # 最后一周 
	return result 
  
if __name__ == '__main__': 
	for w in getcal(sys.argv[1], sys.argv[2]): 
		for d in w: 
			print d, 
		print "=="
