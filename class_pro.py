# class demo:
#     def __init__(self,name,age):
#         # print("in init function")
#         self.name =name
#         self.age =age
#     def function1(self):
#         print("in function1")
# obj1 =demo('abc',22)
# obj2 =demo('xyz',23)
# obj1.function1()


#inheritace
# 1)single inheritace
# class A:
#     def functionA(self):
#         print("in functiona")
# class B(A):
#     def functionB(self):
#         print("in functionb")        
# objb =B()
# objb.functionA()

# 2)multiple inheritace
# class A:
#     def functionA(self):
#         print("in functiona")
# class B() :
#     def functionB(self):
#         print("in functionb")
# class C(A,B):
#     def functionC(self):
#         print("in functionc")                
# objc =C()
# objc.functionC()
# objc.functionA()
# objc.functionB()


# 3)multilevel inheritace
# class A:
#     def functionA(self):
#         print("in functiona")
# class B(A):
#     def functionB(self):
#         print("in functionb")
# class C(B):
#     def functionC(self):
#         print("in functionc")                
# objc =C()
# objc.functionC()
# objc.functionA()
# objc.functionB()

#super keyword in class
class A:
    # def __init__(self,name,age):
    #     self.name =name
    #     self.age =age
    def functionA(self):
        print("in functiona")
    # def functionB(self):
    #     print("in functionb")
        # self.functionA()

class B(A):
    #  def __init__(self,):
    #     super().__init__()
     def functionA(self):
         print("in functiona")
         super().functionA()
obj2 =B()
obj2.functionA()