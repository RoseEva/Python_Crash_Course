#Create list
animals = ['fox', 'bobcat', 'snake', 'gopher tortoise']

#Access elements from left of list
print(animals[0].title())
print(f"There is a {animals[0].upper()}!")
print(animals[1])

#Access elements from right of list
print(animals[-1])
print(animals[-2])

#Modify list
animals[0] = 'rabbit'
print(animals)

#Add to list (defaults to end of list)
animals.append('fox')
print(animals)

#Can build lists dynamically, for example, with an empty list
plants = []
plants.append('passion flower')
plants.append('button bush')
plants.append('willow')
print(plants)

#Insert in list (may specify any position)
animals.insert(3, 'hog')
print(animals)

#Delete element in list
del animals[3]
print(animals)

#Pop method removes last item in a list but lets you work with the item after removing it
print(animals)

popped_animals = animals.pop()
print(animals)
print(popped_animals)

print(f"The last animal observed was a {popped_animals.upper()}!")

#Removing from a list if you don't know the position but do know the value
print(animals)
animals.remove('snake')
print(animals)

#Can work with a removed value by assigning the value to a variable. 
#*Note remove only deletes the first occurrence of the value but if there are more occurrences then a loop is required.*
print(animals)
listed_species = 'gopher tortoise'
animals.remove(listed_species)
print(animals)
print(f"{listed_species.title()} is a listed species.")

#Sorting alphabetically permanently 
print(plants)
plants.sort()
print(plants)

#Reverse alphabetical sorting with reverse=True argument
plants.sort(reverse=True)
print(plants)

#Sort temporarily with sorted() function
print('Here is the original list:')
print(plants)

print('\nHere is the sorted list:')
print(sorted(plants))

print('\nHere is the original list again:')
print(plants)

#Reverse list
regions = ['northwest', 'northeast', 'central', 'south']
print(regions)

regions.reverse()
print(regions)

#Length of list
members = ['Steve', 'Shawn', 'James']
len(members)
print(len(members))



