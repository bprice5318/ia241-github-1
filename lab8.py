"""
lab8
"""

#3.1
    
    
def wordcount (sentence):
    
    x= len(sentence.split())
 
    return x
    
    
phrase = "Hey my name is Brandon"
    
result = wordcount(phrase)
    
print(result)



    
#3.2

demo_str = 'hello world!' 

print ( wordcount(demo_str) )


#3.3 

def minnum (num_list):
    
    num_min = num_list[0]
    
    
    for num in num_list:
        
        if type(num) ==  int:
            
              if num <= num_min:
                  
                  num_min = num
        
    return num_min


#3.4 

demo_list = [1,2,3,4,5,6]


print ( minnum(demo_list) ) 



#3.5 

mix_list = [1,2,3,4,'a',5,6]

print ( minnum(mix_list) )


