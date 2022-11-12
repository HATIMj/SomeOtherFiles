import random 
class Hangman:
    def __init__(self,name):
        self.name=name
        self.list=['cat','rat','bat','sat']
        self.turns=7
        
        self.nw=random.choice(self.list)
        self.word=[None for i in range(len(self.nw))]
    def turn(self):
        m=self.nw

        while self.turns!=0 or self.word==''.join(self.nw):
          o=input()
        
          for i in range(len(self.nw)):
              if self.nw[i]==o:
                  self.word[i]=self.nw[i]
                  print(self.word)
                
              else:
                self.turns-=1
                print(self.word)
k=Hangman('jojo')
print(k.nw)
k.turn()
                    
