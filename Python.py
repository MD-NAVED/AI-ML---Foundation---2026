# user =  "navd has 0 $ in his$ $ $$$$$pocket "
# print(user.count("$"))


# age =  16

# if(age >= 18):
#     print("can aligble for licence")
# if(age <=18):
# #     print("not aligable for licence")

# marks = int(input(""))
# if(marks >= 90):
#     grade="A"
# elif(marks <= 90 and marks >=80):
#     grade="B"
# elif(marks <=80 and marks >=70):
#     grade="C"
# elif(marks <= 60 and marks >= 50 ):
#     grade="D"       
    
# print("GRADE OF THE STUNDENT",grade)

# num = int(input(""))
# num2 = int(input(""))
# sum = num+num2
# print(sum)
 
# side = float(input("area of square")) 
# # print( side ** 2)

# average = float((input("")))
# print(average /2)

# a = int(input(""))
# b =  int(input(""))



# if(a>= b):
#     print("true")
# else:
#     print("False")    

# Num = int(input(""))

# if(Num %2==0 ):
#     print("Even")
# else:print("Odd")    
# num = int(input(""))
# num1 = int(input(""))
# num2 = int(input(""))

# if(num > num1 and num2):
#     print(num)
# if(num1 >num  and num2):
#     print(num1)
# if(num2 > num and num1):
#     print(num2)    

# Num = int(input(""))
# if(Num % 7==0):
#     print("multiple of seven ")
# else:print("Not muiltiple of seven")

# Movies = (input(""))
# Lis = [Movies]
# print(type(Lis))

# Grade = ["A","B",'C','D','B','A','A','D','A']
# Grade.sort()
# print(Grade)

# count =  1 
# while count <=5:
#     print("hy Naved")
#     count += 1

# Num = 1 
# while Num <=100:
#     print(Num)
#     Num+=1

# Num = 100 
# while Num >= 1:
#     print(Num)
#     Num-=1
  
# n= int(input(""))
# Num = 1
# while Num <=10:
#     print(n*Num)
#     Num +=1
# idx = 0
# nums = [3,54,6,77,22,78,25,98,1,245,878]
# while idx < len(nums):
#     print(nums[idx])
#     idx+=1
# nums = (3,54,6,77,22,78,25,98,1,245,878)

# N = 1
# i = 0
# while i < len(nums):
#     if(nums[i] == N):
#         print("Found",i)
#     i+=1
# nums = [3,54,6,77,22,78,25,98,1,245,878]
# x = 22
# idx = 0
# for les in nums:
#     if(les == x):
#         print("X found =",les,)
#         print("At idx =",idx)
#     idx += 1
  
# for ren in range(1,101):
    # print(ren)

# for N in range(100,0,-1):
#     print(N)

# n =int(input())

# for M in range(1,11):

#     print(M * n )

# n = 100
# idx = 0
# sum = 1
# while idx<= n:
#     idx += sum
#     sum+=1
# print(sum)

# class Student:
    
#     def __init__(self,name,marks):
#        self.name = name
#        self.marks = marks
       
#     def welcome(self):
#      print("student",self.name)
     
     
#     def Get_marks (self):
#         print("Marks",self.marks )
      
         

# s1 = Student("karan",97)
# s1.welcome()
# s1.Get_marks()
  
# class  student :
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def GetAvarage(self):
#         sum =  0 
#         for Avg in self.marks:  
#             sum += Avg
#         print("This is your Avarage:",sum/3)      
    
# s1 = student("karan",[56,66,78])    
# s1.GetAvarage()

# class car :
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
    
#     def start(self):
#           self.acc = True
#           self.brk = True
#           self.clutch = True
#           print("your car is started")
         

# car1 = car()
# car1.start()

# class Account:
    
#      def __init__(self ,bal ,acc):
#         self.balance = bal
#         self.accNo  = acc
#         self.add = [self.balance,self.accNo]
        
#      def debit(self, amount):
#          self.balance -= amount
#          print("RS.",amount, "was debited")
#          print("Total balance",self.get_balance())
         
         
#      def cradit(self, amount):
#          self.balance += amount
#          print("RS.",amount, "was cardited")
#          print("Total balance",self.get_balance())
         
         
#      def get_balance(self):
#         return self.balance
         
       
        
# acc1 = Account(10000, 133205145)
# acc1.debit(1000)
# acc1.cradit(500)




# class car :
#     def __init__(self,type):
#         self.type = type
    
    
#     @staticmethod
#     def start():
#      print("Stated..")
     
#     @staticmethod
#     def stop():
#         print("Stoped..")
        
# class mahindra(car):
#     def __init__(self, name, type):
#         super().start()
#         super().__init__(type)
#         self.name = name
        
# car1 = mahindra("thar","electric")
# print(car1.name,car1.type)

        
# class person:
#     name = "unknown"  
    
#     # def changeName (self, name):
#     #     person.name  = name
#     @classmethod
#     def changeName (cls, name):
#         cls.name  = name    

# p1 = person()
# p1.changeName("math")
# print(p1.name)
# print(person.name)


# @staticmethod #used to create the method which is not related to the class variable and can be called without creating the object of the class

# @classmethod #used to change the class variable without creating the object of the 

# @instance #used to change the instance variable and can be      called only by creating the object of the class
      
    
# class students:
    
#     def __init__(self,physics,chemistry,maths):
#      self.physics = physics
#      self.chemistry = chemistry
#      self.maths = maths
     
#     @property
#     def average(self):
#         return str((self.physics + self.chemistry + self.maths)/3) + "%"
        
    
# stu1 = students(68,90,98)
# print(stu1.average)
# stu1.physics =70
# print(stu1.average)

# @property = used to create the method which is related to the class variable and can be called by creating the object of the class


  # {Panding excersise} :-

#polymorphism = the ability of an object to take on many forms. It allows objects of different classes to be treated as objects of a common superclass. In Python, polymorphism is achieved through method overriding and duck typing.

#dunder method = a special method in Python that starts and ends with double underscores (__) and is used to define the behavior of an object for built-in operations. For example, the __str__ method is used to define how an object should be represented as a string when printed.


# Q1: Define a Circle class to create a circle with radius r using the constructor . Define an Area() method of the class which calculates the area of the circle. Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.



# class circle:
#     def __init__(self,radius):
#         self.radius = radius
        
#     def Area(self):
#         return 3.14 * self.radius **2
    
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
    
# c1 = circle(21)
# print("Area of the circle is",c1.Area())
# print("Perimeter of the circle is",c1.perimeter())



# Q2: Define an Employee class with attributes role, department & salary (0:59:51). This class should have a showDetails() method (1:05:32). Create an Engineer class that inherits properties from Employee & has additional attributes: name & age (1:06:17).



# class Empoyee:
#     def __init__(self, role, department , salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
       
#     def showDetails(self):
#         print("role:",self.role)
#         print("department:",self.department)
#         print("salary:",self.salary)
#         print("name:",self.name)
#         print("age:",self.age)

# class Engineer(Empoyee):
    
#     def __init__(self, name,age):
#             super().__init__("software engineer", "IT", 50000)
#             self.name = name
#             self.age = age 
            
           
# e1 = Engineer("naved", 24)
# e1.showDetails()

# class Ordera:
#      def __init__(self, item, prise):
#          self.prise = prise
#          self.item = item
             
#      def __gt__(self, order2):
#         return self.prise > order2.prise
    
    
# order1 = Ordera("bergur",100)
# order2 = Ordera("pizza", 200)
# print(order1 > order2)



