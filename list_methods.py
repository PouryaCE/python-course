names = ["bob", "patrik", "sandy", "Garry", "kevin", "Plunktun"]
print(names)

# append => add a obj to the end of the list
names.append("pourya")
print(names)


# extend => add a iterable obj to the end of the list
names.extend(['mrs puff', 'mr krusty', 'Nepton', 'pourya'])
print(names)


# insert => add a obt to a position
names.insert(1, "john")
print(names)

# remove => remove a obj from list
names.remove("kevin")
print(names)


# remove => take a position and delete an object
# if you do not send a parameter the last object will remove from list
# pop always return deleted object
print(names.pop(0))
print(names)



# clear => deleted all of the objects in the list
# names.clear()
# print(names)



# index => return index of given parameter if exist in the list
print(names.index("pourya"))



# count
print(names.count("pourya"))


names.extend(['d', 'b', 'c', 'a', 'D', 'C', 'B', 'A'])
names.sort()
print(names)

