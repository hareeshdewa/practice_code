print('Hello World!')

squares = []
for i in range(1,11):
    square = i ** 2
    squares.append(square)
print(squares)
print()

cubes = [values ** 3 for values in range(1,11)]
print(cubes,"\n")

#slicing:
names = ['charles','martina','florence','eli']
print(names[0:3])
print(names[-3:])

for name in names[:3]:
    print(name.title(),"\n")

#copying the list
myfood = ['pizza','falafel','carrot cake']
friendfood = myfood[:]

print(myfood)
print(friendfood,"\n")

food = ("Biriyani","Biscuit","Smoothies","Dosa","Noodles")
print("Before: ","\n")
for item in food:
    print(item)
food = ("Biriyani","Tandoori","Roti","Dosa","Noodles")
print("After: ","\n")
for i in food:
    print(i)
print()

aliencolor = "red"
if aliencolor == "green":
    print("5 points")
else:
    print("10 points")
print()

favourite_fruits = ["apple","banana","orange","mango","cherry"]

if "apple" in favourite_fruits:
    print("You really like apple")

if "cherry" in favourite_fruits:
    print("You really like Cherry")
print()

requested_toppings = ["mushrooms","green peppers","extra cheese",
                      "olives"]

for ingrident in requested_toppings:
    if ingrident == "mushrooms":
        print("Adding " + ingrident)
print("finished making your pizza!!")
print()

available_toppings= ["french fries","mushrooms","olives"]

for items in requested_toppings:
    if items in available_toppings:
        print("Adding "+ items)
    else:
        print("Sorry, the requested toppings isn't availavle ")
print("Enjoy your pizza!!!","\n")

usernames = ['admin','Eric','Johnson','harriton']

for users in usernames:
    if users == "admin":
        print("Hello, Admin!!, would you like to see a status report?")
    else:
        print("Hello, "+ users.title() +" ,thank you for logging")
        
print()

current_users = ["Mick","Jerry","Harry","Danny","Morris"]
new_users = ["Danny","George","Yanks","Harry","Ben"]

for user in new_users:
    if user in current_users:
        print(user +" Please enter a new username")
    else:
        print(user + " the username is available")

print()

#Dictionaries
aliens = {'colors': 'green', 'points': 5}
print(aliens["colors"])
points = aliens["points"]
print("You have earned "+ str(points)+ " points!!!","\n")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
alien_0["speed"] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1 
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] += x_increment
print("The original new X_position is "+ str(alien_0["x_position"]))

#removing

del alien_0['y_position']
print(alien_0,"\n")

avorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print(avorite_languages["jen"],"\n")

for name in avorite_languages:
    print(name)
print()

#or 
for name in avorite_languages.keys():
    print(name)
print()

#nesting
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print()

def aliensgame():
    aliens = []
  

    for alien in range(30):
        new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
        aliens.append(new_alien)

    #modiying 
    for alien in aliens[0:3]:
        if alien['color'] == 'green':
            alien['color'] = 'Blue'
            alien['speed'] = 'medium'
            alien['points'] = 10
        elif alien['color'] == 'yellow':
            alien['color'] = 'red'
            alien['speed'] = 'fast'
            alien['points'] = 15
    
    for creatures in aliens[0:5]:
        print(creatures)
    print()     
aliensgame()
print()


pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
}

for foods in pizza['toppings']:
    print(foods)
print()

favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
for name,value in favorite_languages.items():
    print(name + "'s favourite language is ")
    for languages in value:
        print(languages.title())
    print()

print()
#dictionary inside dictionary

users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },

 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }

for username,userinfo in users.items():
    print("Username: "+ username.title())
    print("full name: " + userinfo['first'] + " " + userinfo['last'])
    print("Location: "+ userinfo['location'])

print()

person_1 = {
    "first_name": "Alice",
    "last_name": "Johnson",
    "age": 28,
    "city": "New York"
}

person_2 = {
    "first_name": "Bob",
    "last_name": "Smith",
    "age": 34,
    "city": "Los Angeles"
}

person_3 = {
    "first_name": "Charlie",
    "last_name": "Brown",
    "age": 22,
    "city": "Chicago"
}
persons = [person_1,person_2,person_3]

for person in persons:
    print()
    print("Firstname: "+ person['first_name'])
    print("Lastname: "+ person['last_name'])
    print("age: "+ str(person['age']))
    print("Location: "+ person['city'])
print()

favorite_places = {
    "Alice": ["Paris", "New York", "Tokyo"],
    "Bob": ["Sydney", "San Francisco"],
    "Charlie": ["Rome", "London", "Amsterdam"]
}

for names,places in favorite_places.items():
    print()
    print(names.title() + "'s favourite places are: ")
    for place in places:
        print(place)
print()

cities = {
    "New York": {
        "country": "United States",
        "population": "8.4 million",
        "fact": "Known as the city that never sleeps."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "Home to the busiest pedestrian crossing in the world."
    },
    "Paris": {
        "country": "France",
        "population": "2.2 million",
        "fact": "Known for its iconic Eiffel Tower."
    }
}

for city,cityinfo in cities.items():
    print()
    print("City: "+ city.title())
    print("Country: " + cityinfo['country'])
    print("Population: "+ cityinfo['population'])
    print("Fact: "+  cityinfo['fact'])
print()

#input and while loop
"""
multiple = int(input("Enter a number: "))
if multiple % 10 == 0:
    print("The number is multiple of 10 ")
else:
    print("It is not sorry!!")
"""

current_number = 0
while current_number < 10:
    current_number +=1
    if current_number % 2 == 0:
        continue
   
    print(current_number)

def person():
    person = int(input("Age: "))
    while person > 0:
        if person <= 3:
            print("The ticket cost is free")
        elif person >= 3 and person < 12:
            print("The ticket cost is 12$")
        else:
            print("The ticket cost is 15$")
        break
print()

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current = unconfirmed_users.pop()
    confirmed_users.append(current.title())
    print(current)

print("The current users: ")
for user in confirmed_users:
    print(user.title())

print(unconfirmed_users,"\n")

def polling():
    responses = {}

    # Set a flag to indicate that polling is active.
    polling_active = True
    while polling_active:
    # Prompt for the person's name and response.
        name = input("\nWhat is your name? ")
        response = input("Which mountain would you like to climb someday? ")
        responses[name] = response
        #key              #value

        repeat = input("Would yu like to let another person to climb (Yes/or No): ").lower()
        if repeat == "no":
            polling_active = False
        
        for name,response in responses.items():
            print(name + " would you to climb " + response)

def sandwich():
    sandwich_order = ["chicken","tuna","paneer","fish","crad","goat",'pastrami','pastrami','pastrami']
    finsihed_sandwich = []
    while 'pastrami' in sandwich_order:
        sandwich_order.remove('pastrami')

    while sandwich_order:
        current = sandwich_order.pop()
       
        print(f"I made you {current} sandwich")
        finsihed_sandwich.append(current.title())
    print("\nAll sandwich have been made: ")
    for food in finsihed_sandwich:   
        print(f"- {food} sandwich")
sandwich() 
print()

magicians = ["Andrew","Elizbeth","Johnny","Victor"]
new_magicians = []
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
show_magicians(magicians)
print()

def make_great(magicians):

    for magician in magicians:
        magic = "Great, " + magician.title() +"!"
        print(magic)
make_great(magicians)
print()

def built_person(first_name,last_name,age = ''):
    person  = {'first': first_name,'last': last_name}
    if age:
        person['age'] = age
    return person
print(built_person('john',"felix"))
print(built_person('harry',"Gladio",23))
print()

def city_country(city,country):
    return '"'+ city + ", " + country + '"'
print(city_country("Santiago","Chile")) 
print()

def make_album(artist,title,track = ''):
    music = {'artist':artist,'title':'title'}
    if track:
        music['track'] = track
    print(music)
make_album('Michael',"Beat It")
make_album('Sandi','Robb',23)
print()



def user_album(artist,title,track=None):
    musics = {'artist': artist, 'title' : title}
    if track:
        musics["track"] = track
    return musics

while True:
    artist_prompt = input("Enter artist: ")
    if artist_prompt == 'q':
        break

    title_prompt = input("Enter the title: ")
    if title_prompt == 'q':
        break

    track_prompt = (input("Enter track: "))
    """
    if track_prompt == 'q':
        album = user_album(artist_prompt,title_prompt)
    else:
        album = user_album(artist_prompt,title_prompt,track_prompt)
    print(album)
    """
            
   
print()

def pizza(size,*toppings):
    print("Preparing "+ str(size) + " pizza: ")
    for topping in toppings:
        print("- "+ topping)

pizza(12,"pepporic")
pizza(14,"mushroom",'cauliflower','chicken')

print()
    
def build_profile(first,last, **user_info):
    profile = {}
    profile['firstname'] = first
    profile['lastname'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
profiles = build_profile('Hareesh',"Dewa",location = "Coimbatore",
                         country = "India")
print(profiles,"\n")

def sandwich(*sandwichs):
    for sandwich in sandwichs:
        print(sandwich)
prerson_sandwiches = sandwich("chicken","mutton","Vegetable")
print(prerson_sandwiches,"\n")

def cars(model,brand,**carinfo):
    carsinfo = {}
    carsinfo['carname'] = model
    carsinfo['carbrand'] = brand
    for key,value in carinfo.items():
        carsinfo[key] = value
    return carsinfo
car_profile = cars('Subaru','outback',color = 'blue',tow = True)
print(car_profile)

#class
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is sitting")

    def animal_age(self):
        print(self.name.title() + " is " + str(self.age) + " years old")
animal = Animal("johnny",26)
animal.sit()
print(animal.name)
animal.animal_age()
print()


class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.oda_meter_reading = 0

    def got_description(self):
        return self.model + " is a superior model from " + self.make + " in the year " + str(self.year)
    
    def read_meter(self):
        return "The car has " + str(self.oda_meter_reading) + " miles on it"
    
    def update_oda_meter(self,mileage):
        #self.oda_meter_reading = 0
        if mileage >= self.oda_meter_reading: #0
            self.oda_meter_reading = mileage
        return "You can't rollback an odameter"
    
    def increment_odameter(self,miles):
        self.oda_meter_reading +=miles

car1 = Car("audi","a4",2015)
print(car1.got_description())
car1.update_oda_meter(130)
car1.increment_odameter(12)
print(car1.read_meter())
print()

class Restaurant:
    def __init__(self,restaurant_name, custine_type):
        self.restaurant_name = restaurant_name
        self.custine_type = custine_type
        self.number_served = 0
    
    def describle_restaurant(self):
        print(self.restaurant_name + " is fantastic one and it has "
              + self.custine_type + " as its signature")
    
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open at France!!")
    
    def res_numbered_server(self,served):
        if served >= self.number_served:
            self.number_served = served
            print("So far " + str(self.number_served) + " people has been served in the restaurant")
    
    def increment_number_served(self,set):
        self.number_served += set
    
    def number_of_people(self):
        return "Hence "+ str(self.number_served) + " has been served finally"


restaurant = Restaurant("Cockraco","Chicken Biryani")
restaurant2 = Restaurant("Pizza","italian")

restaurant.describle_restaurant()
restaurant.open_restaurant()
restaurant.res_numbered_server(21)
restaurant.increment_number_served(31)
print(restaurant.number_of_people())

restaurant2.describle_restaurant()
print()

class User:
    def __init__(self,first_name,last_name,username,password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.login_attempt = 0
    
    def describe_user(self):
        print("Username: "+ self.username +"\n"
        "Fullname: "+ self.first_name +" "+ self.last_name)
    
    def reset_login_attempt(self):
        self.login_attempt = 0
    
    def increment_login_attempt(self):
        self.login_attempt +=1
    

    def greet_user(self):
       return "Hello " + self.username + ", welcome back!!"
userone = User("Hareesh","Dewa","hd2001","hareeshcool")
userone.describe_user()
print(userone.greet_user())

userone.increment_login_attempt()
userone.increment_login_attempt()
userone.increment_login_attempt()
userone.increment_login_attempt()
print("Login attempt: "+ str(userone.login_attempt))

userone.reset_login_attempt()
print(userone.login_attempt)



