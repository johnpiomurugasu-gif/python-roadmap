#this is the first comment
# pythong testing for me to learn

"""this is how i become"""


#there are many different types of values
#so most common data types are interger -3-2-1-,0,1,2130
#float: Decimal number example:-3.5, -2.25, 1.0, 0.0, 2.2
#complex example : 1+j, 2+4j

print(-2)
print(-1)
print(1.30)
print(3_5)
print(3/5)
print(3//5)
print(3%2)
print(3/2)
print(3**2)


#String
#examples, string can be oen or more crhacters in single or double quotes.
#If a string is more than one sentence then we use a triple quote.

##
#'Asabeneh'
#'Finland'
#'Python'
#'I love teaching'
#'I hope you are enjoying the first day of 30DaysOfPython Challenge'
##
#
#
# Booleans 
# data type can be True or False. T or F should be uppercase
#   True  #  Is the light on? If it is on, then the value is True
#    False # Is the light on? If it is off, then the value is False
#List
#you care about teh order of things, 
[0,1,2,3,4] # all are teh same data types, a list of numbers
['banana', 'orange', 'Mango', 'Avocado'] #all the same data types, list of strings (fruits)
['Malaysia', 'Finland', 'Singapore', 'America']
['Cheese', 10, False, 9.81] #different data types in the list 
# - string, integer, boolean and float

#Dictionary 
#python dictionary object is unordered coolection of data in a key vlaue
#pair format, there is no order to it

{
'firstname': 'Asabeneh',
'last_name': 'Yetayeh',
'country:': 'Finland',
'age':250,
'is_married': True,
'skills':['JS', 'React', 'Node', 'Pyton'],
}

print(type({'firstname': 'Asabeneh',}))
person = {
    'first_name': 'John',
    'country': 'Malaysia',
    'age': 28,
    'skills': ['Python', 'VBA'],
}

print(person['first_name'])   # John
print(person['skills'])       # ['Python', 'VBA']
print(person['skills'][0])    # Python, because the value is a list

#A list keeps order, dict and set don't: 
# when you care about order, therefore, 
# you must use list (if your choice of containers is 
# limited to these three, of course ;-) ).
#dict associates each key with a value, 
# while list and set just contain values: 
# very different use cases, obviously.

#Tuple

#A tuple is an ordered collection of 
# different data types like list 
# but tuples can not be modified once they are created. 
# They are immutable, unchangable

('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # Names

('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # planets

##
#
#2. Semantic Meaning: Records vs. Collections
#The developer community broadly distinguishes lists and 
# tuples by how they represent data structure:
#Lists are meant for homogeneous data (a collection of the same types 
# of things), where the length can change (e.g., a list of usernames).
#• Tuples are meant for heterogeneous data (different types of things) 
# where the position of the item has specific meaning—acting 
# like a "record"
#
#
#
# --- LISTS ARE MUTABLE ---
my_list = [10, 20, 30]
my_list[1] = 99  # Valid! The running program updates the list to [10, 99, 30]

# --- TUPLES ARE IMMUTABLE ---
my_tuple = (10, 20, 30)
"""my_tuple[1] = 99  # CRASH! Python stops execution and throws a TypeError"""

#Sets
#A set is a collection of data types similar to list and tuple. 
# Unlike list and tuple, set is not an ordered collection of items.
#only unique, no duplicates, no order, but it can change
# just unique unorder of items

{2, 4, 3, 5}
{3.14, 9.81, 2.7} # order is not important in set


#So list is ordered, mutable collection that allows duplicate elements.
# Set is An unordered collection of unique elements. Duplicates are automatically removed
# Tuple is oredered, immutaboe collection that allows duplicate items
#they are single stored values
#diciontary contains store key value pairs

#Types

print(type(10)) #int
print(type(3.1)) #float
print(type(1+3j)) #complex
print(type('cheese')) #string
print(type([1,2,3])) #list
print(type({'cheese':250})) #dictionary
print(type((2,3,4,1,5))) #tuple
print(type({0.1,0.2,0.3})) #set


#Exercise day 1 level 1
#operators are 3 and 4
#Question1
a=4
b=3

print(a-b)
print(a*b)
print(a%b)
print(a/b)
print(a**b)
print (a//b)
#Question 2
myname='john'
familyname='murugasu'
country='united kingdom'
text='i am enjoying the python of 30 days'
#Question 3
print(type(10))
print(type(9.8))
print(type(4-4j))
print(type(['python','Finland']))
print(type(myname))
print(type(familyname))
print(type(country))

#Level 3

#find Eucolidean distance between (2,3) and (10,8)

a=(2,3)
b=(10,8)

c=a[1] ;d=a[0]; e=b[0]; f=b[1]

a1=e-d
a2= f-c
finallength= ((a1**2)+(a2**2))**0.5
print(finallength)










