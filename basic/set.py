#####################################################
#   Author:       RR
#   Created:      07/12/2016
#
#   Description:  Demonstrate sets
#####################################################
#
#   DATE        AUTHOR  DESCRIPTION
#   07/12/2016  RR      initialised
#
#####################################################
def printline():
    print "-------------------------------------------\n"
    
print("Sets demonstration")
printline()

x = {1,2,3,4,5}
print("x:")
print(x)

print("is 10 in x: " + str(10 in x))
print("is 5 in x: " + str(10 in x))


printline()
print("Comparing two sets")

y = {2,4,6,8}
print("y:")
print(y)

print("Intersect - x.insersection(y):")
print(x.intersection(y))

print("Union x.union(y):")
print(x.union(y))

print("Symmetric difference x.symmetric_difference(y):")
print(x.symmetric_difference(y))

print("Difference x.difference(y):")
print(x.difference(y))

print("Difference y.difference(x):")
print(y.difference(x))







