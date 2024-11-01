class car:
    __brand="toyota"

    @property  #for getter
    def brand(self):
        return self.__brand
    
    @brand.setter #setter
    def brand(self,value):
        self.__brand=value


obj=car()
print(obj.brand)

obj.brand="sedan"
print(obj.brand)
