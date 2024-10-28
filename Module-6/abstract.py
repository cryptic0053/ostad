from abc import ABC,abstractmethod

class Bangladesh(ABC):

    @abstractmethod
    def print10to20(self):
        pass

    def Print0to10(self):
        for i in range(10):
            print(i)


class Dhaka(Bangladesh):
    def print10to20(self):
        pass
    

obj=Dhaka()
obj.Print0to10()