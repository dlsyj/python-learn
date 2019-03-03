#Module + functions = the standard library
import os
import datetime
import time

print (os.getcwd())
print (os.environ)
print (os.getenv('HOME'))


print (datetime.date.today())
print (datetime.date.isoformat(datetime.date.today()))

print (time.strftime("%H:%M"))
print (time.strftime("%A %P"))