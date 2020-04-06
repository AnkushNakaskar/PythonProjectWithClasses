#Unpacking Elements from Iterables of Arbitrary Length
from audioop import avg


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle);

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212');
grades =('Dave', '4', '4', 'dave@example.com')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)
print(drop_first_last(grades))
