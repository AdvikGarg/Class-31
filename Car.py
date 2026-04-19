class BMW:

    def Milage(self):
        print("BMW milage is: 21")

    def Max_speed(self):
        print("BMW top speed is 250 km/h")


class Ferrari:

    def Milage(self):
        print("Ferrari milage is: 16")

    def Max_speed(self):
        print("Ferrari top speed is 340 km/h")



car1=BMW()
car2=Ferrari()


for i in (car1,car2):
    i.Milage()
    i.Max_speed()
    