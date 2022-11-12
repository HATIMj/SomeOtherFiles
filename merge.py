import random
class Dice:
    def __init__(self,name,*args,**kwargs):
        self.roll=None
        self.name=name
    def rollthedice(self):
        self.roll=random.randint(0,6)
        return self.roll
    
    @staticmethod
    def compare(m,n):
        if int(m)<int(n):
            print(f"{m} wins")
        elif n<m:print(f"{n} wins")
        else:print("Draw")
    
j=Dice("jojo")
k=Dice("koko")
m=j.rollthedice()
n=k.rollthedice()
Dice.compare(m,n)
