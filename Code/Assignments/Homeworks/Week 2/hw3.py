# Name:
# Section:
# hw3.py

##### Template for Homework 3, exercises 3.1 - ######
import math
# **********  Exercise 3.1 ********** 

# Define your function here
def list_intersection(list1, list2):
	section = []
	for element in list1:
		if element in list2:
			section += [element]
	return section

# Test Cases for Exercise 3.1
print list_intersection([1, 3, 5], [5, 3, 1])
print list_intersection([1, 3, 6, 9], [10, 14, 3, 72, 9])
print list_intersection([2, 3], [3, 3, 3, 2, 10])
print list_intersection([2, 4, 6], [1, 3, 5])
print list_intersection([1, 2, 3], [3 ,2, 2])
# **********  Exercise 3.2 **********

# Define your function here
def ball_collide(ball1, ball2):
    
    distance = math.sqrt((ball2[0]-ball1[0])**2 + (ball2[1] - ball1[1])**2)

    return distance <= (ball1[2] + ball2[2])

# Test Cases for Exercise 3.2
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True

# **********  Exercise 3.3 **********

# Define your dictionary here - populate with classes from last term
my_classes = {'18.123': 'Calculus for Computer Science', '6.1': 'Basics of Programming'}

def add_class(class_num, desc):
    ##### YOUR CODE HERE #####
    my_classes[class_num] = desc

# Here, use add_class to add the classes you're taking next term
add_class('6.189', 'Introduction to Python')

def print_classes(course):
	cnt = 0
	course_numbers = my_classes.keys()
	for course_numb in course_numbers:
		if course == course_numb.split('.')[0]:
			print course_numb, '-', my_classes[course_numb]
			cnt += 1

	if cnt == 0:
		print "No Course", course, "classes taken"

# Test Cases for Exercise 3.3
##### YOUR CODE HERE #####
print_classes('18')
print_classes('6')
print_classes('8')
# **********  Exercise 3.4 **********

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Define your functions here
def combine_lists(l1, l2):
    comb_dict = {}
    for i in range(len(l1)):
    	comb_dict[l1[i]] = l2[i]
    return comb_dict

combined_dict = combine_lists(NAMES, AGES) # Finish this line...

def people(age):
	people_list = []
	for key in combined_dict:
		if combined_dict[key] == age:
			people_list += [key] 

	return people_list

# Test Cases for Exercise 3.4 (all should be True)
print 'Dan' in people(18) and 'Cathy' in people(18)
print 'Ed' in people(19) and 'Helen' in people(19) and\
       'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)
print people(21) ==   ['Bob']
print people(22) ==   ['Kelly']
print people(23) ==   []

# **********  Exercise 3.5 **********

def zellers(month, day, year):
	date = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
	mon_num = {'March': 1, "April": 2, 'May': 3, 'June': 4, 'July': 5, 'August': 6, 'September': 7, 'October': 8, 'November': 9, 'December': 10, 'January': 11, 'February': 12}
	A = mon_num[month]
	B = day
	if A == 11 or A == 12:
		year -= 1

	C = year % 100
	D = year / 100
	W = (13*A-1) / 5
	X = C /4
	Y = D / 4
	Z = W + X + Y + B + C - 2*D
	R = Z%7

	if R < 0:
		R = R + 7

	return date[R]

# Test Cases for Exercise 3.5
print zellers("March", 10, 1940) == "Sunday"
print zellers("June", 17, 1997) # This should be True