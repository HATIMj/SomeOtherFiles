                                                               #MULTI LEVEL INHERITANCE IN CLASSES + SINGLE INHERITANCE + MULTIPLE INHERITANCE






class electronic_devices:
    Types=10
    def __init__(self,name,use):
        self.name=name
        self.use=use

    def fun(self):
        return f"The name of the device is {self.name}. It is used for {self.use}."

class pocket_gadgets(electronic_devices):
    Types=3
    Names=["Mobiles","Tablets","music players"]

    @classmethod
    
    def types(cls):

        
        return f"They are of {cls.Types} types. There names are {cls.Names}. "




class Phone(pocket_gadgets):
    Types=2
    Names=["Android","Ios"]
    


karan=pocket_gadgets("Android","Multitasking")
print(karan.types())

    