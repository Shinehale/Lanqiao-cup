N=int(input())
standard_time=60*60*24*1000
data=N%standard_time
data=data//1000
hour=data//3600
data%=3600
minute=data//60
data%=60
print("{0:02d}:{1:02d}:{2:02d}".format(hour,minute,data))