class Car:
    __BRAND="Toyota"

    def DISPLAY(self):
        print(f"Our brand name is {self.__BRAND}")


class SEDAN(Car):

    def DisplayFromChilde(self):
        print(f"Our brand name is {self.__BRAND}")


OBJ=Car()
#print(OBJ.__BRAND)
OBJ.DISPLAY()

# obj=SEDAN()
# obj.DisplayFromChilde()

#_ is for protected access modifier(inside class+child class+out of the class(not recommended))
#__is for private access modifier(inside class+child classXXX+out of the classXXX)