#Module + functions = the standard library
import os
import datetime
import time
import random

dir (random)
help (random.randint)

print (os.getcwd())
print (os.environ)
print (os.getenv('HOME'))


print (datetime.date.today())
print (datetime.date.isoformat(datetime.date.today()))

print (time.strftime("%H:%M"))
print (time.strftime("%A %P"))

#built-in data structures
#IF-ELIF-ELSE
today = datetime.date.weekday(datetime.date.today())
if today == 5:
    print ('party!')
elif today == 6:
    print ('Recover.')
else:
    print ('Work!')

# time.sleep (secs) - pause execution
# random.randint (a,b) - generate random number
# use 'for' loop when knowing number of times; use 'while' when do not know
odds = [1,3,5,7,9]

for i in range (5): # iterates 5 times
    times = datetime.time.minute
    if times in odds:
        print ("Yes")
    else:
        print ("No")
    wait_time = random.randint (1,60)
    time.sleep(wait_time)



