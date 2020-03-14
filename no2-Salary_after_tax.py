#coding:utf-8

import math
#计算所得税公式
def income_tax_function(i):
	'''
	速算扣除数法:
	0     - 3.6w    3% 0
	3.6w  - 14.4w  10% 2520
	14.4w - 30w    20% 16920
	30w   - 42w    25% 31920
	42w   - 66w    30% 52920
	66w   - 96w    35% 85920
	96w   -        45% 181920
	'''
	if i <=36000 and i> 0 :
		return i*0.03
	if i>36000 and i <=144000:
		return i*0.1 - 2520
	if i>144000 and i<=300000:
		return i*0.2 -16920
	if i>300000 and i<= 420000:
		return i*0.25 - 31920
	if i>420000 and i <= 660000:
		return i*0.3-52920
	if i>660000 and i <= 960000:
		return i*0.35 - 85920
	if i>96000:
		return i*0.45 - 18920
'''
计算五险一金
计算扣除%8养老保险,0.2%失业保险, 0%生育,0%工伤,2%医保,12%公积金,企业年金1%
税基简单以b来计算
'''
def tax_52(b):

	tax_52_outcome = float(b)*(0.08+0.002+0.02+0.12+0.01) #五险二金
	return tax_52_outcome
#计算年度个人所得税
def income_tax_year(b):
	#先扣除五险二金
	income_gross = float(b)-tax_52(b)

	#个税 先减去 5k*12=6w 基本
	income_pure = income_gross - 60000
	if income_pure<= 0:
		return 0

	#减去每月专项附加税(不计入)
	#超出部分专项扣除
	else: 
		income_tax = income_tax_function(income_pure)
		return income_tax

def main():
		a = raw_input("month or year: ")
		if a == 'year':
			b = raw_input("input year salary:")
			if str(b).isdigit():
				tax_5x2j = tax_52(b)
				income_gross_year = income_tax_year(b)
				salary_after_tax = float(b) - tax_5x2j - income_gross_year
				print("扣除五险二金 %.2f 元,扣除个人所得税 %.2f 元, 税后收入为 %.2f 元" %(tax_5x2j,income_gross_year,salary_after_tax))
		if a == 'month':
			b = raw_input("input month salary: ")
			if str(b).isdigit():
				# c = caculate_month(b)
				print("暂不支持,请输入年税前收入")

if __name__ == '__main__':
	main()