'''-----------------------------------------------
Tuple - Immutable - ()
-> Duplication allowed
-> Immutable - so we can not modify it.
-> ordered - we can access it through a[?].
-> representation - ()
-> ex. a = ( 10, 20, 'python', 20.6 )
-----------------------------------------------'''
t = (1,2,'python',3.4,2,3,2,-3,2)
tup = 1,2,'python',3.4,-3
tp = (2,)

print(t)
print(tup)
print(type(tp))

print(t[2])
print(t[1:3])
print(tup[::-1])