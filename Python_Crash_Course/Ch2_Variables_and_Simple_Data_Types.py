#Ch. 2: Variables and Simple Data Types


#Newline
print('Hello World')
print('Hello\nWorld')

#New Tab
print('Hello\tWorld')

#List
animals = ['fox, tortoise, armadillo']
print(animals[0])

#Format List
group_name = "environmental research team"
message = f"Hello, we are the {group_name}"
print(message)

group_name = "environmental research team"
message = f"Hello, we are {group_name.title()}"
print(message)

group_name = "environmental research team"
message = f"Hello, we are {group_name.upper()}"
print(message)

#Remove Whitespace

task = ' monitoring '
print(task.rstrip())
print(task.lstrip())
print(task.strip())

website = 'https://county.org'
print(website.removeprefix('https://'))
print(website.removesuffix('.org'))

#Permanently remove whitespace requires reassigning the variable name to stripped value
task = task.strip()
print(task)


