'''
lab5
'''

#3.1

alien_color = 'green'

if alien_color == 'green':
    print ("you have earned 5 points")
    
#3.2 

alien_color = 'red'

if alien_color == 'green':
    print ("you have earned 5 points")
    
else:
    print ("you have earned 10 points")
    
#3.3 

favorite_fruits = ['apples', 'pears', 'oranges']


if 'bananas' in favorite_fruits:
    print ("You really like Bananas!")
    
if 'apples' in favorite_fruits:
    print ("You really like Apples!")
    
if 'melon' in favorite_fruits:
    print ("You really like Melon!")

age = 18

if age < 10:
    print ("The person is a kid")
    
elif age >= 10 and age < 20:
    print ("The is person is a teenager")
    
elif age >= 20:
    print ("The person is an adult")
    
if age >= 65:
    print ("The person is also an elder")