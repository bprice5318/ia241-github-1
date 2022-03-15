"""
lab7
"""

#3.1

x=0

while x!= 6: 
    
    if x!= 3:
        print (x)
    x=x+1

#3.2 
x=5
num=1

while x != 0:
    num = num * x
    x= x-1
    print (num)
    
#3.3

x=5
num=0

while x != 0:
    num = num + x
    x= x-1
    print (num)
    
#3.4

x=8
num=1

while x != 2:
    num = num * x
    x= x-1
    print (num)
    
#3.5

x=8
num=1

while x != 3:
    num = num * x
    x= x-1
    print (num)
    
    
#3.6 

x=0

num_list= [12, 32, 43, 35]


while len(num_list)!= 0:
    print (num_list)
    num_list.remove(num_list[x])
    x+x+1
    