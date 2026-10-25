#Day 2 of 30 days, functions
##
#

a=min(20,30,40)
print(a) # should be 20, gives min value

b=max(20,30,120)
print(b) # gives 120, max value


c=min([20,30,120])
print(c) #lists as arguement and return min

d=max([20,30,120])#lists as arguement and return max
print(d)

e=sum([20,30,120])#lists as arguement and return sum
print(e) #20+30+120

#Variables

#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

#Examples
"""
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # if we want to use reserved word as a variable
year_2021
year2021
current_year_2021
birth_year
num1
num2
"""

#Invalid examples

"""
first-name
first@name
first$name
num-1
1num
"""
# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }

print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument

#Example printing values stored in the variables above
# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

#Declaring multiple variables in a line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#Getting the user input using input built in fucntion

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

#Data types, check which data is what

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

print(first_name)
print(last_name)
print(country)
print(city)
print(age)

# Printing out types
print(type('Asabeneh'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Asabeneh'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
#print('num_int', int(num_str))      # 10
#print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
#print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asabeneh'
#print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
#print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']



#Exercises Day 2

#Level 1
#Question 2
# 'Day 2:30 Days of Python programming

#Question 3

first_name='cheese'

#Question 4
last_name='mart1232421412in'

#Question 5
full_name=first_name+ last_name
print(full_name)

#Question 6

country="Malaysia"

#Question 7
City='Kuala Lumpur'

#Question 8
age=20

#Question 9
year=2002

#Question 10
is_married=True

#Question 11
is_true= False

#Question 12
is_light_on=True

#Question  13

cheese, burger, coop, number, boolen = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

#Exercsies LEvel 2

#Question 1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(City))
print(type(age))
print(type(year))
print(type(is_true))
print(type(is_light_on))
print(type(coop))

#Question 2
ab=(len(first_name))

#Question 3
ba=(len(last_name))

print(ab-ba)

#Question 4
num_one=int(5)
num_two=int(4)
a=[num_one,num_two]
#Question 5
question5=(sum(a))
print(question5)
#Question 6

question6=num_one-num_two

#Question 7
question7=num_one*num_two

#Question 8
Question8=num_one/num_two

#Question 9

Question9=num_two%num_one

#Quesiton10

question10=num_one**num_two

#Question11

question11=num_one//num_two

#Question 12

radius=int(30)

#i
area_of_circle=3.14*((radius**2))
#ii
circumference=2*3.14*radius
#iii
radius_0=int(input('What is your radius?'))
area_of_circle_0=3.14*((radius_0**2))

#Question 13

first_name0=str(input("what is ur name?"))
last_name0=str(input('what is ur last name?'))
country_00=str(input('what country you from'))
age_00=int(input('what is ur age?'))

#Question 14
help('keywords')