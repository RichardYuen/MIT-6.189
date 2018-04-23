# Name:
# Section:
# strings_and_lists.py

# **********  Exercise 2.7 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])


def cumulative_sum(number_list):
    # number_list is a list of numbers

    ##### YOUR CODE HERE #####
    new_list = []
    for i in range(len(number_list)):
        new_list += [sum_all(number_list[:i+1])]
    return new_list

# Test Cases
##### YOUR CODE HERE #####
print cumulative_sum([4,3,6])
print cumulative_sum([1,2,3,4,5])
# **********  Exercise 2.8 **********

def report_card():
    ##### YOUR CODE HERE #####
    class_numb = []
    grade = []
    gpa_sum = 0
    classes = int(raw_input("How many classes did you take? "))
    for i in range(classes):
        class_numb.append(raw_input("What was the name of this class? "))
        grade.append(int(raw_input("What was your grade? ")))
    
    print "REPORT CARD"
    for i in range(classes):
        print class_numb[i],"-",grade[i]
    print "Overall GPA", float(sum_all(grade))/classes

# Test Cases
report_card()
## In comments, show the output of one run of your function.

# **********  Exercise 2.9 **********

# Write any helper functions you need here.

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    # word is a string to convert to pig-latin
    new_word = []
    ##### YOUR CODE HERE #####
    if word[0] not in VOWELS:
        new_word = word[1:]+ word[0] +'ay'
        return new_word
    else:
        new_word = word + 'hay'
        return new_word

# Test Cases
##### YOUR CODE HERE #####

print pig_latin('fuck')
print pig_latin('you')

# **********  Exercise 2.10 **********
cube = [i**2 for i in range(1,11)]
coin_flip = [j + i for i in ['h', 't'] for j in ['h', 't']]
def string_list_comp():
    string = raw_input("Enter a string: ")
    return [letter for letter in string if letter in VOWELS]

list_comp = []
for x in [10,20,30]:
    for y in [1,2,3]:
        list_comp.append(x+y)
# Test Cases
print cube
print coin_flip
print string_list_comp()
print list_comp
#**********  Optional Exercise 2  ********
def type_int(number_list):
    return [for num in number_list if type(num) == type(int)]

coordinate = [[x, x**2 + 1] for x in range(-5,6) if x**2 + 1 in range(11)]
circle_coord = [[x, y] for x in range(-5, 6) for y in range(-5, 6) if x**2 + y**2 == 25]