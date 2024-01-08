 	'''
Data Types: 
	1. List - Always in Square Brackets	#Mutable
	2. Set - Always in Curly Brackets
	3. Dictionary - Use as pair and ( value 1: value 2)
	4. Int - 0
	5. Float - 0.0
	6. Complex - a + j #we have to only use j for the imaginary part.
	7. Tuple -	#Immutable
	8. String - chars
'''
a = [1,'Harsh',3.3,1+2j]
print(a)
print(type(a))

b = {1,'Harsh',3.3,1+2j}
print(b)
print(type(b))

c = {"Harsh":"Dalwadi"}
print(c)
print(type(c))

d = ("Harsh","Dalwadi")
print(d)
print(type(d))

'''-----------------------------------------------
List - Mutable
-----------------------------------------------'''
lst = ["Harsh","Jimit","Aalap","Vishnu","Nisarg","Lay"]
print(lst)

#Access Items [start:end:interval]
print(lst[1:5:2])

#Change Element
lst[2] = "Aalap Modi"
print(lst[2])

#Check Length of List
print(len(lst))

#Add Value in List [append element at last]
lst.append(["Laxman","Dalwadi"])
print(lst)

#Add value at specified place (index , value)
lst.insert(4,"Harsh Dalwadi")
print(lst[4])

#delete particular element
lst.remove("Harsh Dalwadi")
print(lst)

#delete element at last from list
lst.pop()
print(lst)

#delete element from particular index
del lst[0]
print(lst)

#delete whole list
# del lst
# print(lst)

#empty list
lst.clear()	
print(lst)

#Copy list
#Method 1	
Numbers = (1,2,3,4,5,6,7,8,9)
print(Numbers)
print(type(Numbers))
lst1 = list(Numbers)
print(lst1)
#Method 2	
lst = lst1.copy()
print(lst)

#Concate two list
x = [1,2,3,4,5]
y = ["Harsh","Jimit","Aalap"]
z = x + y
print(z)

#Other way to concate list
# x.extend(y)
# print("Y = ",y)
# print("X = ",x)
y.extend(x)
print("Y = ",y)
print("X = ",x)


#Reverse List
x.reverse()
y.reverse()
print(x)
print(y)


'''---------------------------------------------------------------------------------------
Dictionary

-> A dictionary is a collection which is unordered, changeable and indexed.
-> In Python dictionaries are written with curly brackets, and they have keys and values.
---------------------------------------------------------------------------------------'''

dic = {
	"Name" : "Harsh Dalwadi" ,
	"Age" : 22 , 
	"Work" : "SW"
}

print(dic)

#Accessing Items

x = dic["Name"]
print(x)

#Change Value

dic["Age"] = 21
print(dic["Age"])
print(dic)

dic[21] = "Harsh"
print(dic)

#Access key & values

print(dic.keys())
print(dic.values())

#check key is present in the dictionary or not??

print("Name" in dic)
print("Harsh" in dic)

#Dictionary length
print(len(dic))

#add items in dictionary
dic["Work"] = "Data Scientist"
print(dic)


#pop item from dictionary
dic.popitem()
print(dic)

#delete item from dictionary
del dic["Age"]
print(dic)

# del dic
# print(dic)

#create dictionary also like this and clear it
thisdict = {
	"Name" : "Harsh Dalwadi" , 
	"Age" : "22" , 
	"Work" : "Data Scientist" ,
	"Interest" : ["AI","ML","IOT"]
}

print(thisdict)

# thisdict.clear()
# print(thisdict)

#copy dict
mydict = dict(thisdict)
print("MY DICT",mydict)

ourdict = mydict.copy()
print("ourdict",ourdict)

#Nested Dictionary
family = {
		"Fam1" : {
		"Name" : "Harsh HD",
		"Age" : 22
		},
		"Fam2" : {
		"Name" : "Harshil HP",
		"Age" : 17
		},
		"Fam3" : {
		"Name" : "HD",
		"Age" : 10
		}
}
print(family)
print(family["Fam2"])
print(family["Fam1"]["Name"])

#other method nested dict
fam1 = {
		"Name" : "Harsh HD",
		"Age" : 22
		}
fam2 = {
		"Name" : "Harshil HP",
		"Age" : 17
		}
fam3 = {
		"Name" : "HD",
		"Age" : 10
		}


fam = {
	"family1" : fam1,
	"family2" : fam2,
	"family3" : fam3
}

print(fam)

#get method to get values
print(dic.get("Name"))

#items
print(dic.items())

#update - update data simulateously

dic.update({
		"color" : "green",
		"passion" : "PC"
	})

print(dic)
