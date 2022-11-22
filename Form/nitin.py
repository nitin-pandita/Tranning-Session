def MaxWealth(self,accounts):

        maxwealth = 0
        
        for i in range(1,len(accounts)):
            
            maxwealth = max(sum(accounts),maxwealth)
            
            
        print(maxwealth) 
        
    
    
MaxWealth([1,2],[3,5])