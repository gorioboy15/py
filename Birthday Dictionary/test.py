import os

bday = {}

def bday_entries(k,v):
    bday[k] = v
    return bday
true = True

while true:
    n = input("Enter your name: ")
    b = input("Enter your birthday: ")
    total = bday_entries(n,b)
    print(total)
#bday = open("bday.txt", "w")
#bday.closed