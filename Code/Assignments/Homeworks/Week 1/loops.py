print 'Part 1'

for i in range(2,11):
	print "The decimal equvalents of 1/"+ str(i), "is", 1.0/i

print 'Part 2'

n = int(raw_input("Enter number:"))

if n > 0:
	while (n >= 0):
		print n
		n = n - 1
elif n < 0:
	print "This is a negative number"

print "Part 3"

base = input("Base?")
exp = input("Exponent?")
result = 1
for i in range(exp):
	result *= base 
print "The result is", result

print "Part 4"

while n % 2 == 1:
	n = input("Enter a number which divisible by 2:")	
	if n % 2 == 1:
		print "Please enter a new number!"
	else:
		print "Congratulation you are right!"
