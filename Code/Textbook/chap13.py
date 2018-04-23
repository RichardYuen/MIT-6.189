class Time:
	pass
#####Section 13.1
def printTime(time):
	print "%d:%d:%d" % (time.hours, time.minutes, time.seconds)

def after(t1, t2):
	if t1.hours < t2.hours:
		return True
	elif t1.hours > t2.hours:
		return False
	else:
		if t1.minutes < t2.minutes:
			return True
		elif t1.minutes > t2.minutes:
			return False
		else:
			if t1.seconds < t2.seconds:
				return True
			else:
				return False


time1 = Time()
time1.hours = 11
time1.minutes = 59
time1.seconds = 30

time2 = Time()
time2.hours = 15
time2.minutes = 37
time2.seconds = 12

time3 = Time()
time3.hours = 11
time3.minutes = 24
time3.seconds = 46

printTime(time1)
printTime(time2)
printTime(time3)

print after(time1, time2) #Return True
print after(time1, time3) #Return False
#####Section 13.2
def addTime(t1, t2): 
  sum = Time() 
  sum.hours = t1.hours + t2.hours 
  sum.minutes = t1.minutes + t2.minutes 
  sum.seconds = t1.seconds + t2.seconds 

  if sum.seconds >= 60: 
    sum.seconds = sum.seconds - 60 
    sum.minutes = sum.minutes + 1 

  if sum.minutes >= 60: 
    sum.minutes = sum.minutes - 60 
    sum.hours = sum.hours + 1 

  return sum 

currentTime = Time() 
currentTime.hours = 9 
currentTime.minutes = 14 
currentTime.seconds =  30 

breadTime = Time() 
breadTime.hours =  3 
breadTime.minutes =  56 
breadTime.seconds =  31

doneTime = addTime(currentTime, breadTime) 
printTime(doneTime) 
#####Section 13.3
def increment(time, seconds):
	time.seconds =  time.seconds + seconds

	if  time.seconds >= 60:
		time.minutes = time.minutes + time.seconds // 60
		time.seconds = time.seconds % 60
	if  time.minutes >= 60:
		time.hours = time.hours + time.minutes // 60
		time.minutes = time.minutes % 60
def pure_increment(time, seconds):
	time.seconds =  time.seconds + seconds

	if  time.seconds >= 60:
		time.minutes = time.minutes + time.seconds // 60
		time.seconds = time.seconds % 60
	if  time.minutes >= 60:
		time.hours = time.hours + time.minutes / 60
		time.minutes = time.minutes % 60

	return time

time = Time()
time.hours = 20
time.minutes = 7
time.seconds = 13

increment(time, 120)
pure_increment(time, 620)
#####Section 13.4
def pro_dev_increment(time, plus_seconds):
	
	minutes = time.hours * 60 + time.minutes 
	seconds = minutes * 60 + time.seconds

	seconds = seconds + plus_seconds

	time.hours = seconds // 3600 
  	time.minutes = (seconds%3600) // 60 
  	time.seconds = seconds%60 
  	
  	return time

printTime(pro_dev_increment(time, 1000)) 