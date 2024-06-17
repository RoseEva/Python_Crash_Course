#For loop *Note: plurality
animals = ['fox', 'bobcat', 'snake', 'gopher tortoise']
for animal in animals:
    print(animal)

for animal in animals:
    print(f"Wow that {animal} is beautiful!")
    print(f"I have never seen such a lovely {animal} before.\n")

print("Aren't those animals simply majestic?")

#Using range function
for value in range(1, 5):
    print(value)

for value in range(5):
    print(value)

#Using range to make a list
numbers = list(range(6))
print(numbers)

#Third argument in range function is number of steps up
even_numbers = list(range(2,11,2))
print(even_numbers)

#Range of exponents
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

#More concise range of exponents
squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

#Even more concise with list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

#Simple statistics with a list of numbers
digits = []
for value in range(1,11):
    digits.append(value)

print(min(digits))

print(max(digits))

print(sum(digits))

#Slicing a list
workers = ['Steve', 'John', 'Bill', 'Chris', 'Amanda', 'Ashley']
print(workers[0:3])

#If you leave out the first index then it starts from the beginning of list
print(workers[:4])

#Leave off the end index it will run through until the end
print(workers[2:])

#Use negative for the last elements of the list
print(workers[-3:])

print(workers[-3:5])

#Use third value in brackets to define number of elements to skip
print(workers[1::2])

#Looping through slice
print('Here are the fist three presenters:')
for worker in workers[:3]:
    print(worker.title())

#Copy a list by making a slice of the entire list
my_teammates = ['Josh', 'James', 'Berry']
my_coworkers = my_teammates[:]

my_teammates.append('Amy')
my_coworkers.append('Larry')

print('My teammates are:')
print(my_teammates)

print('\nMy coworkers are:')
print(my_coworkers)

#Tuples (similar to lists but immutable and uses parentheses instead of brackets)
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


