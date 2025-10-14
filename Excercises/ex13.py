# ------------OOPs Concepts Part-2 (Advanced – Inheritance, Polymorphism, Abstraction, Encapsulation, Exception Handling) --------------------

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Create a base class Vehicle and derive Car and Bike classes with their own methods.
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is being driven")
        
class Bike(Vehicle):
    def ride(self):
        print("Bike is being ridden")

c = Car()
c.start()
c.drive()

b = Bike()
b.start()
b.ride()                        

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Implement single inheritance with Person as base class and Employee as derived class.
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def show(self):
        print(f"Employee name: {self.name}")
        
e = Employee("Sneha")
e.show()                

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Demonstrate multiple inheritance with Teacher and Researcher classes and derived class Professor.
class Teacher:
    def teach(self):
        print("Teaching students")
        
class Researcher:
    def research(self):
        print("Conducting research")
        
class Professor(Teacher, Researcher):
    def guide(self):
        print("Guiding students and researchers")
        
p = Professor()
p.teach()
p.research()
p.guide()
 
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        
# 4. Implement multilevel inheritance with Animal -> Mammal -> Dog.
class Animal:
    def eat(self):
        print("Animal eats food")
        
class Mammal(Animal):
    def breathe(self):
        print("Mammal breathes air")
        
class Dog(Mammal):
    def bark(self):
        print("Dog barks")
        
d = Dog()
d.eat()
d.breathe()
d.bark()                        

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
# 5. Write a program using hierarchical inheritance with Shape as base and Circle, Rectangle, Triangle as derived classes.
class Shape:
    def area(self):
        print("Calculating area")

class Circle(Shape):
    def area(self):
        print("Area of circle = pi * r^2")

class Rectangle(Shape):
    def area(self):
        print("Area of rectangle = l × b")

class Triangle(Shape):
    def area(self):
        print("Area of triangle = ½ × b × h")

for s in [Circle(), Rectangle(), Triangle()]:
    s.area()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        
# 6. Create an abstract base class Payment with abstract methods pay(). Implement it in CreditCard, UPI, and NetBanking.
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid Rs{amount} using Credit Card.")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid Rs{amount} using UPI.")

class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid Rs{amount} using NetBanking.")

# Example
c = CreditCard()
c.pay(500)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 7. Demonstrate method overloading (by default arguments) in a Calculator class.
class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c
    
calc = Calculator()
print(calc.add(5,10)) 
print(calc.add(5))
print(calc.add(5,10,15))
  
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
# 8. Show method overriding using base class Bird and derived class Parrot.
class Bird:
    def sound(self):
        print("Some generic bird sound")
        
class Parrot(Bird):
    def sound(self):
        print("Parrot says: Hello!")
        
b = Bird()
b.sound()
p = Parrot()
p.sound()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
# 9. Create a BankAccount class that raises an exception if withdrawal is more than balance.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient Balance!")
        self.balance -= amount
        print(f"Withdrawal successful! Remaining balance: Rs{self.balance}")

acc = BankAccount(1000)
try:
    acc.withdraw(1500)
except ValueError as e:
    print("Error:", e)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 10. Implement encapsulation in a Customer class by making __balance private and accessing it with getter/setter.
class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount!")

c = Customer("Sneha", 5000)
print("Balance:", c.get_balance())
c.set_balance(6000)
print("Updated Balance:", c.get_balance())

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 11. Create a Student class that demonstrates class variables vs instance variables.
class Student:
    school = "ABC School"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

s1 = Student("Sneha")
s2 = Student("Riya")
print(s1.name, s1.school)
print(s2.name, s2.school)
Student.school = "XYZ School"
print(s1.name, s1.school)
print(s2.name, s2.school)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 12. Write a program to demonstrate polymorphism using a common method make_sound() in different classes Dog, Cat, Cow.
class Dog:
    def make_sound(self):
        print("Dog barks")
        
class Cat:
    def make_sound(self):
        print("Cat meows")
        
class Cow:
    def make_sound(self):
        print("Cow moos")
        
for animal in [Dog(), Cat(), Cow()]:
    animal.make_sound()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                            
# 13. Implement operator overloading (+) in a ComplexNumber class.
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)
print("Sum:", c1 + c2)    

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
# 14. Demonstrate multiple constructors using @classmethod.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2025 - birth_year)

p1 = Person("Sneha", 21)
p2 = Person.from_birth_year("Riya", 2004)
print(p1.name, p1.age)
print(p2.name, p2.age)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
         
# 15. Create a base class Appliance with derived classes WashingMachine and Refrigerator showing polymorphism.
class Appliance:
    def operate(self):
        print("Operating an appliance")
        
class WashingMachine(Appliance):
    def operate(self):
        print("Washing Clothes...") 
        
class Refrigerator(Appliance):
    def operate(self):
        print("Cooling food...")
        
for app in [WashingMachine(), Refrigerator()]:
    app.operate()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                           
# 16. Write a program that demonstrates super() usage in inheritance.
class Parent:
    def show(self):
        print("This is the parent class.")
        
class Child(Parent):
    def show(self):
        super().show()
        print("This is the child class.")
        
obj = Child()
obj.show()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
# 17. Implement exception handling for division by zero inside a MathOperation class.
class MathOperation:
    def divide(self, a, b):
        try:
            result = a / b
            print("Result:", result)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!") 
            
m = MathOperation()
m.divide(10, 2)
m.divide(5, 0)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
               
# 18. Create a Library system with abstract class Item and derived classes Book and Magazine.
from abc import ABC, abstractmethod

class Item(ABC):
    def display_info(self):
        pass
    
class Book(Item):
    def display_info(self):
        print("This is a Book item.")
        
class Magazine(Item):
    def display_info(self):
        print("This is a Magazine item.") 
        
b = Book()
m = Magazine()
b.display_info()
m.display_info()                   

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 19. Write a program that demonstrates destructor (__del__) usage in a class.
class Demo:
    def __init__(self):
        print("Object created!")
    
    def __del__(self):
        print("Destructor called, object deleted!")
        
obj = Demo()
del obj            

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 20. Create a Bank system with custom exception InsufficientFundsError.
class InsufficientFundsError(Exception):
    pass

class Bank:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds!")
        self.balance -= amount
        print(f"Withdrawal successful. Remaining: Rs{self.balance}")
        
b = Bank(2000)
try:
    b.withdraw(3000)
except InsufficientFundsError as e:
    print("Error:", e)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
# 21. Implement encapsulation by making attributes private and exposing them through methods in a Car class.
class Car:
    def __init__(self, brand, price):
        self.__brand = brand
        self.__price = price
        
    def get_info(self):
        print(f"Car: {self.__brand}, price: {self.__price}")
        
car = Car("Honda", 900000)
car.get_info()            

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 22. Create a Shape class that demonstrates polymorphism by overriding area() in derived classes.
class Shape:
    def area(self):
        pass
 
class Circle(Shape):
    def area(self):
        print("Area = pi * r^2")
        
class Square(Shape):
    def area(self):
        print("Area = side^2")
        
for s in [Circle(), Square()]:
    s.area()                    

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 23. Implement a Logger class as a singleton design pattern.
class Logger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

log1 = Logger()
log2 = Logger()
print("Same instance:", log1 is log2)        

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 24. Write a program demonstrating hybrid inheritance with multiple classes.
class A:
    def showA(self): print("Class A")

class B(A):
    def showB(self): print("Class B")

class C(A):
    def showC(self): print("Class C")

class D(B, C):
    def showD(self): print("Class D")

d = D()
d.showA()
d.showB()
d.showC()
d.showD()                

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 25. Implement duck typing in Python with a function that accepts any object with fly() method.
class Bird:
    def fly(self): print("Bird is flying")
    
class Airplane:
    def fly(self): print("Airplane is flying")
    
def lift_off(flier):
    flier.fly()
    
lift_off(Bird())
lift_off(Airplane())            

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------