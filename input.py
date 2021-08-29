import datetime

name = input('Enter your name: ')
birth_year = input('Enter your birth year: ')

current_year = datetime.datetime.now().year
age = current_year - int(birth_year)

print("Hi " + name + "! You're " + str(age) + " old.")