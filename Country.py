class India:
    def capital(self):
        print('The Capital of India is New Dehli.')
    
    def language(self):
        print('Hindi and Tamil are the most spoken languages in India.')
        
    def type(self):
        print('India is a developing and self reliant country.\n\n')  

class USA:
    def capital(self):
        print('The Capital of USA is Washington D.C .')
    
    def language(self):
        print('English is the most spoken languages in Usa.')
        
    def type(self):
        print('USA is a developed and Oil Greedy country.\n\n')  

obj1=India()
obj2=USA()

for i in (obj1, obj2):
    i.capital()
    i.language()
    i.type()
                  