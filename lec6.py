'''
lec
'''

for item in ['a','b','c']:
    
    print (item)

demo_str = "this is my string"

for c in demo_str:
    print (c)

x=0
for word in demo_str.split():
    x = x +1
    
print ("There are", x,  "Words")


for num in range(5):
    print(num)
    
for num in range (1,5):
    print (num)
    
num_list = [1234,43212,345,3,11,23,4,5,3,12,1234,4,5,54] 

num_max = num_list[0]

for num in num_list:
    if num >= num_max:
        num_max = num
        
print (num_max)
