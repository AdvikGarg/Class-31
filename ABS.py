from abc import ABC, abstractmethod

class abs(ABC):
    def print(self, x):
        print('Past value: ',x )
        
    @abstractmethod
    def task(self):  
        print('We are inside abs')

class test(abs):
    def task(self):
        print('We are inside the test class!')
        
t1=test()
t1.task()
t1.print(100)                  