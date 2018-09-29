#!/usr/bin/env python
#coding=utf-8
year = int(input('please input the total years: '))
money = float(input('please input the money(RMB) invest per week: '))
rate = float(input('please input the rate invest per year: '))

def calculateRates(y,m,r):
	total = 0
	amount = 0
	alltotal = 0
	for index in range(y):
		total = (total + 365/7*m)*r
		amount = amount + 365/7*m
		alltotal = 365/7*m*(index+1)*(r**(index+1))
		needrate = alltotal/total*r
		actualrate = (total/amount)**(1.0/(index+1))
		print('第%d年总额：%.1f, 复利总额：%.1f, 总投入：%.1f, 复利：%.4f, 一次投入复利：%.4f, 换算为一次投入利率：%.4f, 换一次投入需要利率：%.4f' 
			% (index+1,
				total,
				alltotal,
				amount,
				total/amount,
				r**(index+1),
				actualrate,
				needrate))
	print('利率为：%.4f' % (alltotal/amount)**(1.0/(year)))

calculateRates(year,money,rate)