#3.1

class my_stat:
    
    
    def sigma (self,m,n):
        
        result = 0
        
        for i in range(n,m+1):
            result = result + i
            
        return result
        
    
    def calc_pi (self, m, n):
        
        result = 1
        
        for i in range (n,m+1):
            
            result = result + i
            
        return result
        
        
    def calc_f (self,m):
        
        if m ==0:
            return 1
        else:
            return m * self.calc_f(m-1)
            
     
            
    def calc_p (self,m,n):
    
        return self.calc_f(m)/self.calc_f(m-n)

    

#3.2 

my_cal = my_stat()

print (my_cal.sigma(5,3))

print (my_cal.calc_pi(5,3))

print (my_cal.calc_f(5))

print (my_cal.calc_p(5,3))