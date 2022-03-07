'''
lab6
'''

#3.1
for x in range (6):
   if x != 3:
       print (x)
       

#3.2

num = 1

for x in range (1,6):
   
   num = num * x
   
   print (num)
   
   
#3.3

result = 0

for x in range (1,6):
   
   result = result + x
   
   print (result)

#3.4

num = 1

for x in range (3,9):
   
   num = num * x
   
   print (num)
   
#3.5

top = 1

for x in range (1,9):
   
   top = top * x
   
bottom = 1

for x in range (1,4):
   
   bottom = bottom * x
   
print (top/bottom)

"realized I made this needlessly complicated "

#3.6 

x=0

sentence = "This is my 6th String"

for word in sentence.split():
   x = x +1
   
print (x)




#3.7 

my_tweet = { 
"favorite_count":1138, 
"lang": "en", 
"coordinates": (-75, 40), 
"entities": {"hashtags": ["Preds", "Pens", "SingIntoSpring"]}
}

count = 0

for x in my_tweet["entities"]["hashtags"]:
   print (x)
   count= count +1 
   
print (count)