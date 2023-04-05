class Demo:
    def __init__(self, name,age) -> None:
        self.name = name
        self.age = age
    
    def _private(self):
        print('Sure Here I am ', self)
        

de = Demo("Yeab", 22)
de._private()

list  = list()

print(list)