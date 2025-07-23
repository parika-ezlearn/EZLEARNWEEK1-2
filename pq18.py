'''Convert string to datetime in Python with timezone
'''
import datetime
s = '2021-09-01 15:27:05.004573 +0530'
res = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S.%f %z')
print(res)