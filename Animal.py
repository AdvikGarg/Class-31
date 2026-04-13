from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass
 
class lion(Animal):
    def move(self):
        print('I can roar')

class Snake(Animal):
    def move(self):
        print('I can slither')

class dog(Animal):
    def move(self):
        print('I can bark')

class parrot(Animal):
    def move(self):
        print('I can fly')  
        
L=lion()
L.move()

S=Snake() 
S.move()

D=dog()
D.move()

P=parrot()
P.move()                     
        
    