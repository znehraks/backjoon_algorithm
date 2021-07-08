thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

x = thisdict["model"]
print(x)

y = thisdict.get("model")
print(x)

for i in thisdict:
    print(i, thisdict[i])

for i in thisdict.values():
    print(i)

for i in thisdict.keys():
    print(i)

for x, y in thisdict.items():
    print(x, y)

if "moddel" in thisdict:
    print(True)

print(len(thisdict))

thisdict["color"] = "red"
print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdictCopy = thisdict.copy()
print(thisdictCopy)

thisdictCopy2 = dict(thisdict)
print(thisdictCopy2)

child1 = {
    "name" : "enil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linux",
    "year" : 2001
}

myFamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(myFamily)