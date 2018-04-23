date = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

first_name = raw_input("Enter your first name:")
last_name = raw_input("Enter your last name:")

print("Enter your date of birth:")

mo = int(raw_input("Month?"))
day = int(raw_input("Day?"))
year = int(raw_input("Year?"))

A = mo
B = day
C = year % 100
D = year / 100

W = (13*A-1) / 5
X = C /4
Y = D / 4
Z = W + X + Y + B + C - 2*D
R = Z%7

if R < 0:
	R = R + 7

print first_name, last_name,",you was born on", date[R]