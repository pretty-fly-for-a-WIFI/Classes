
  

#https://www.youtube.com/watch?v=apACNr7DC_s


class User:
    pass
user1=User() #user1 is an "instance" or an "object" of User
user1.first_name="Dave"  #Field: Data attached to an object, so "Dave" is a field of the object
user1.last_name="Bowman"
print(user1.first_name)
print(user1.last_name)

first_name="Arthur"
last_name="Clark"
print(first_name,last_name)
print(user1.first_name,user1.last_name)

user2=User()
user2.first_name="Frank"
user2.last_name="Poole"
print(user2.first_name,user2.last_name)

user1.age=37
user2.favorite_book="2001: A Space Odyssey"

#Class Features
#Methodes
#Initialization
#Help text
class User:    # init method, unit=initialization a.k.a "Construction
    def __init__(self, full_name, birthday):
        self.name=full_name
        self.birthday=birthday #yyyymmdd
user=User("Dave Bowman", "19710315")
print(user.name)
print(user.birthday)

class User:    # init method, unit=initialization a.k.a "Construction
    def __init__(self, full_name, birthday):
        self.name=full_name
        self.birthday=birthday #yyyymmdd

        #extract first and last names
        name_pieces=full_name.split(" ")
        self.first_name=name_pieces[0]
        self.last_name=name_pieces[-1]

user=User("Dave Bowman", "19710315")
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)

import datetime
class User:
    """A member of FriedFace. For now we are only
    storing their name  and birthday.
    But soon we will store an uncomfortable amount of user information"""
    def __init__(self, full_name, birthday):
        self.name=full_name
        self.birthday=birthday #yyyymmdd

        #extract first and last names
        name_pieces=full_name.split(" ")
        self.first_name=name_pieces[0]
        self.last_name=name_pieces[-1]

    def age(self):
        """
        Return the age of the user in years
        """
        today=datetime.date(2001,5,12)
        yyyy=int(self.birthday[0:4])
        mm=int(self.birthday[4:6])
        dd=int(self.birthday[6:8])
        dob=datetime.date(yyyy,mm,dd) #Date of birth
        age_in_days=(today-dob).days
        age_in_years=age_in_days/365
        return int(age_in_years)

user=User("Dave Bowman","19710315")
print(user.age())

user=User("Dave Bowman", "19710315")
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)

#instance variables vs class variables
#https://www.youtube.com/watch?v=BJ-VvGyQxho&t=626s
class Employee:
    
    num_of_emps=0
    raise_amount=1.04
    
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"@company.com"
        
        Employee.num_of_emps+=1
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
    
        
emp1=Employee("Shinichi","Kawai",40000)
emp2=Employee("Francisco", "Flores",80000)
print(Employee.num_of_emps)

print(emp1.email)
print(emp2.email)
print(emp1.fullname())

emp1.raise_amount=1.05
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
