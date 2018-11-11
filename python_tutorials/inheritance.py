class Car:
    classVarPublic=0000
    __classVarprivate=1111
    def __init__(self):
        print('car created')
        self.number=10
    def printName(self):
        print('name',self.name,self.number)

    def trial(self,a,b):
        print('in car',a,b)

class Marooti(Car):
    __provateNum = 2222
    def __init__(self):
        super().__init__()
        print('marooti car created with base as ',Marooti.__bases__)
        self.name='marooti'
    def __call__(self, *args, **kwargs):
        print('__call__ method called')

    def printName(self):
        super().printName()
        print('name',self.name,self.number)

    def printName(self,a):
        super().printName()
        print('name',self.name,self.number,'overloaded',a)

    def trial(self, a):
        print('overriding in marooti', a)

    # def __str__(self):
    #     print('self.name',self.name)
    #     print('self.classVarPublic',self.classVarPublic)

obj = Marooti()
# obj.printName(a=1010)
# print('obj.classVarPublic', obj.classVarPublic)
# print('__classVarprivate',obj._Marooti__provateNum)

# print(dir(obj))
# print(obj.__eq__(obj))
# print(obj.__str__())
# obj.trial(10)


# obj()


print(obj.__repr__())
print(obj.__str__())
