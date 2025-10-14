# ------------------------------------- OOPs Concepts Part-1 (Basics of OOPs – Classes, Objects, Constructors, Methods) ------------------------------------------------

# 1. Create a Car class with attributes like brand, model, and price. Write methods to display details and apply discounts.
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model 
        self.price = price
    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, price: {self.price}")
            
    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)
        print(f"Price after discount: {self.price}")
        
Car = Car("Toyota", "Corolla", 20000)
Car.display_details()
Car.apply_discount(10)    
         
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
           
# 2. Design a BankAccount class with methods deposit(), withdraw(), and check_balance().
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
       
# 3. Create a Student class that stores name, roll_no, and marks. Write a method to calculate grade.
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        
    def calculate_grade(self):
        if self.marks >=90:
            return "A"
        elif self.marks >=75:
            return "B"
        elif self.marks >=60:
            return "C"
        else:
            return "D"
s = Student("Sneha", 101, 85)
print("Student GradeL", s.calculate_grade())
           
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Define a Book class with attributes title, author, and price. Add a method to apply discount if price > 500.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price 
        
    def apply_discount(self):
        if self.price > 500:
            self.price *= 0.9
        return self.price
    
b = Book("Java Basics", "James", 600)
print("Discounted Price:", b.apply_discount())    
           
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Create an Employee class with methods to calculate annual salary and bonus.
class Employee:
    def __init__(self, name, salary):   # <-- fixed here
        self.name = name
        self.salary = salary
     
    def annual_salary(self):
        return self.salary * 12
    
    def bonus(self):
        return self.salary * 0.1

e = Employee("Rahul", 40000)
print("Annual Salary:", e.annual_salary(), "Bonus:", e.bonus())        

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 6. Implement a ShoppingCart class with methods to add_item, remove_item, and display_cart.
class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item):
        self.cart.append(item)
        print(f"Added {item} to cart.")

    def remove_item(self, item):
        if item in self.cart:
            self.cart.remove(item)
            print(f"Removed {item} from cart.")
        else:
            print("Item not found!")

    def display_cart(self):
        print("Cart Items:", self.cart)

shop = ShoppingCart()
shop.add_item("Shampoo")
shop.add_item("Soap")
shop.display_cart()
shop.remove_item("Soap")
                        
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 7. Write a Restaurant class that maintains a menu as dictionary and has methods to add_dish, remove_dish, and show_menu.
class Restaurant:
    def __init__(self):
        self.menu = {}

    def add_dish(self, dish, price):
        self.menu[dish] = price

    def remove_dish(self, dish):
        if dish in self.menu:
            del self.menu[dish]

    def show_menu(self):
        print("Menu:", self.menu)

r = Restaurant()
r.add_dish("Pizza", 250)
r.add_dish("Burger", 150)
r.show_menu()
r.remove_dish("Burger")
r.show_menu()                    

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 8. Create a Flight class with methods to book_ticket, cancel_ticket, and available_seats.
class Flight:
    def __init__(self, total_Seats):
        self.available = total_Seats
    
    def book_ticket(self, n):
        if n <= self.available:
            self.available -= n
            print(f"Booked {n} seat(s). Remaining: {self.available}")
        else:
            print("Not enough seats!")
            
    def cancel_ticket(self, n):
        self.available += n 
        print(f"Cancelled {n} seat(s). Available: {self.available}")
        
flight = Flight(100)
flight.book_ticket(5)
flight.cancel_ticket(2)                  
                
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 9. Design a Library class with methods to add_book, remove_book, and search_book.
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, name):
        self.books.append(name)
        print(f" Added book: {name}")
        
    def remove_book(self, name):
        if name in self.books:
            self.books.remove(name)
            print(f"Removed book: {name}")
            
    def search_book(self, name):
        print(f"{name} {'found' if name in self.books else 'not found'} in library.")
        
lib = Library()
lib.add_book("Java")
lib.search_book("Java")     
                   
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 10. Implement a Laptop class with attributes like brand, ram, storage, and method to upgrade RAM.
class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        
    def upgrade_ram(self, new_ram):
        self.ram = new_ram
        print(f"RAM upgraded to {self.ram}GB")
        
lap = Laptop("HP", 8, 512)
lap.upgrade_ram(16)
            
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 11. Create a Movie class with attributes title, duration, and method to check if it’s a long movie (>2 hrs).
class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        
    def is_long(self):
        print(f"{self.title} is {'a long' if self.duration > 120 else 'a short'}")    

movie = Movie("Avatar", 180)
movie.is_long()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 12. Define a Mobile class with constructor and methods to display details and check battery percentage.
class Mobile:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery
        
    def display_details(self):
        print(f"Brand: {self.brand}, Battery: {self.battery}%") 
        
    def check_battery(self):
        print("Battery Low!" if self.battery < 20 else "Battery OK!") 
        
mob = Mobile("Samsung", 50)
mob.display_details()
mob.check_battery()     
         
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 13. Create a Hospital class that maintains patients list and methods admit_patient, discharge_patient, and show_patients.
class Hospital:
    def __init__(self):
        self.patients = []

    def admit_patient(self, name):
        self.patients.append(name)
        print(f"Admitted: {name}")

    def discharge_patient(self, name):
        if name in self.patients:
            self.patients.remove(name)
            print(f"Discharged: {name}")

    def show_patients(self):
        print("Current Patients:", self.patients)

hos = Hospital()
hos.admit_patient("Rina")
hos.show_patients()
                       
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 14. Implement a Hotel class with rooms and methods book_room, vacate_room, and show_available_rooms.
class Hotel:
    def __init__(self, rooms):
        self.available = rooms

    def book_room(self, n):
        if n <= self.available:
            self.available -= n
            print(f"Booked {n} room(s). Remaining: {self.available}")
        else:
            print("Not enough rooms!")

    def vacate_room(self, n):
        self.available += n
        print(f"Vacated {n} room(s). Available: {self.available}")

hotel = Hotel(20)
hotel.book_room(3)
hotel.vacate_room(1)                       
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 15. Create a Bus class with attributes like route, capacity, and method to check available seats.
class Bus:
    def __init__(self, route, capacity):
        self.route = route
        self.capacity = capacity
        self.booked = 0

    def available_seats(self):
        print(f"Available seats: {self.capacity - self.booked}")

bus = Bus("Delhi-Agra", 40)
bus.available_seats()          
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 16. Write a Game class with player score tracking and method to update score.
class Game:
    def __init__(self, player):
        self.player = player
        self.score = 0
        
    def update_score(self, points):
        self.score += points
        print(f"{self.player}'s score: {self.score}")
        
g = Game("Sneha")
g.update_score(10)        
            
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 17. Design a University class that stores departments and has methods to add or remove departments.
class University:
    def __init__(self):
        self.departments = []
        
    def add_department(self, name):
        self.departments.append(name)
        print(f"Added department: {name}")
        
    def remove_department(self, name):
        if name in self.departments:
            self.departments.remove(name)
            print(f"Removed department: {name}")

uni = University()
uni.add_department("Computer Science")                    
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 18. Create a Bank class that tracks multiple accounts using a dictionary.
class Bank:
    def __init__(self):
        self.accounts = {}
        
    def add_account(self, acc_no, balance):
        self.accounts[acc_no] = balance
        print(f"Account {acc_no} added with {balance}")
        
bank = Bank()
bank.add_account(101, 5000)
            
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 19. Implement a Teacher class that stores subjects taught and method to add a new subject.
class Teacher:
    def __init__(self, name):
        self.name = name
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)
        print(f"Subject '{subject}' added for {self.name}.")

teacher1 = Teacher("Mrs. Sharma")
teacher1.add_subject("Math")
teacher1.add_subject("Science")
print("Subjects taught:", teacher1.subjects) 
              
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 20. Define a ShoppingMall class with shops list and methods to add/remove shops.
class ShoppingMall:
    def __init__(self):
        self.shops = []
        
    def add_shop(self, shop):
        self.shops.append(shop) 
        print(f"Shop {shop} added.")

    def remove_shop(self, shop):
        if shop in self.shops:
            self.shops.remove(shop)
            print(f"Shop '{shop}' removed.")
        else:
            print(f"Shop '{shop}' not found.")

mall = ShoppingMall()
mall.add_shop("Zara")
mall.add_shop("H&M")
mall.remove_shop("Zara")
print("Current shops:", mall.shops)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 21. Create a Cafe class with method to add/remove menu items and calculate bill.
class Cafe:
    def __init__(self):
        self.menu = {}
        
    def add_item(self, item, price):
        self.menu[item] = price
        print(f"Added '{item}' to menu with price {price}.")
        
    def remove_item(self, item):
        if item in self.menu:
            del self.menu[item]
            print(f"Removed '{item}' from menu.")
        else:
            print(f"Item '{item}' not found.")
         
    def calculate_bill(self, order_list):
        total = 0
        for item in order_list:
            if item in self.menu:
                total += self.menu[item]
                print(f"Added {item} - {self.menu[item]}")
            else:
                print(f"{item} not in menu.")
        print(f"Total Bill: {total}")
        
cafe = Cafe()
cafe.add_item("Coffee", 50)
cafe.add_item("Sandwich", 100)
cafe.calculate_bill(["coffee", "sandwich", "Juice"])                    
                                
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 22. Write a Train class with attributes train_no, source, destination, and method to check train route.
class Train:
    def __init__(self, train_no, source, destination):
        self.train_no = train_no
        self.source = source
        self.destination = destination
        
    def check_route(self):
        print(f"Train {self.train_no} runs from {self.source} to {self.destination}.")
        
train1 = Train(12345, "Mumbai", "Delhi")
train1.check_route()
            
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 23. Implement a Doctor class that keeps track of patients visited and calculates consultation fees.
class Doctor:
    def __init__(self, name, fee_per_patient):
        self.name = name
        self.fee_per_patient = fee_per_patient
        self.patients = []

    def add_patient(self, patient_name):
        self.patients.append(patient_name)
        print(f"Patient '{patient_name}' visited Dr. {self.name}.")

    def total_fees(self):
        total = len(self.patients) * self.fee_per_patient
        print(f"Total consultation fees: {total}")

doctor1 = Doctor("Dr. Mehta", 500)
doctor1.add_patient("Sneha")
doctor1.add_patient("Ravi")
doctor1.total_fees()
                
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# 24. Create a MusicPlayer class with methods play_song, pause_song, and next_song.
class MusicPlayer:
    def __init__(self):
        self.playing = None

    def play_song(self, song):
        self.playing = song
        print(f"Now playing: {song}")

    def pause_song(self):
        if self.playing:
            print(f"Paused: {self.playing}")
        else:
            print("No song is currently playing.")

    def next_song(self, song):
        print(f"Switching to next song: {song}")
        self.play_song(song)

player = MusicPlayer()
player.play_song("Shape of You")
player.pause_song()
player.next_song("Perfect")        
                         
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 25. Design a Zoo class with methods to add_animal, remove_animal, and list_animals.
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added '{animal}' to the zoo.")

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"Removed '{animal}' from the zoo.")
        else:
            print(f"'{animal}' not found in the zoo.")

    def list_animals(self):
        print("Animals in the zoo:", self.animals)

zoo = Zoo()
zoo.add_animal("Lion")
zoo.add_animal("Elephant")
zoo.remove_animal("Lion")
zoo.list_animals()                
                   
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------