class Myclass:
    x=10
    y=20

    @staticmethod
    def addtwo():
        z=Myclass.x+Myclass.y
        print(z)

Myclass.addtwo()