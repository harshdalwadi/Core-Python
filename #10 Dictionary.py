## DATA TYPES ##
# INT - numbers - 5
# STRING - alphabet - "string" - "5" - "5.5" 
# FLOAT - decimal - 5.5
# BOOl - True or false | 1 or 0 | yes or no
# LIST - [] - order - mutable - repeat allow
# TUPLE - () - order - immutable - repeat allow
# SET - {} - Unorder - mutable - repeat not allow
# dictionary - {} - order - mutable - repeat not allow

# dictionary
# {KEY : VALUE} #pair


data = {
  "name": "Harsh",
  "age": 12,
  "roll": 27,
   4: "HD"
}

print(data['name'])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

x = thisdict.get("model") #Get the value of the "model" key
print(x)

x = thisdict.keys() #Get a list of the keys
print(x)

x = thisdict.values() #Get a list of the values
print(x)

x = thisdict.items() #Get a list of the key:value pairs
print(x)

#add values
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

# Change the "year" to 2018
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#Update the "year" of the car by using the update() method
thisdict.update({"year": 2020})

# Adding an item to the dictionary
thisdict["color"] = "red"
print(thisdict)

# The pop() method removes the item with the specified key name
thisdict.pop("model")
print(thisdict)

# The del keyword removes the item with the specified key name
del thisdict["model"]
print(thisdict)

#this will cause an error because "thisdict" no longer exists.
del thisdict
print(thisdict) 

# Make a copy of a dictionary with the copy() method
mydict = data.copy()
print(mydict)

# Make a copy of a dictionary with the dict() function
mydict = dict(thisdict)
print(mydict)

# Create a dictionary that contain two dictionaries
family = {
  'fam1': { 'name':'python',  'year' : (1998,2000)  },
  'fam2' : { 'name' : 'java',  'year' : [1998,1999]  }
}

print(myfamily)

print(family['fam1']['year'][0])
print(family['fam2']['year'][1])