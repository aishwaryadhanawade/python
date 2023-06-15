# d = {1: 'A', 2: 'B'}
#
# for i in d.values():
#     print(i)
#
# print(d.values())
# import datetime
#
# # from dateutil import parser
#
# close_date = '2099/12/12 '
# open_date = '01-01-2000'
# format_date = '%Y/%m/%d'
# # print(datetime.datetime.today())
# # date = datetime.strptime(open_date, format_data)
# # print(date)
#
# datetime = datetime.datetime.strptime(close_date, format_date)
#
# print(datetime.date())
# print(type(datetime))


# from datetime import *
import datetime as dt
from dateutil import relativedelta

# close_date = '2099/12/31'
# open_date = '2000/01/01'
#
# format_date = '%Y/%m/%d'
#
# datetime1 = datetime.strptime(close_date, format_date)
# datetime2 = datetime.strptime(open_date, format_date)
#
# t = datetime.today()

# print(datetime2.date())
# print(datetime1.date())
# print(date.today())
# cd= (t - datetime2).days // 365
# rd= (datetime1 - t).days // 365
# print(f'remaining days: {rd}')
# print(f'completed days: {cd}')

# delta = relativedelta.relativedelta(t, datetime2)
# delta1 = relativedelta.relativedelta(datetime1, t)
# print(delta.years, 'completed Years')
# print(delta1.years, 'remaining Years')


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# fruits.remove('banana')
# print(fruits)
#
# fruits[2]='grapes'
# print(fruits)

p = [i for i in fruits if i != 'banana']

l = ['grapes' if i == 'kiwi' else i for i in fruits]

print(l)
#
# y = [i * 7 for i in range(778) if i * 7 <= 777]
#
# print(y)
