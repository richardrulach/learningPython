#####################################################
#   Author:       RR
#   Created:      07/12/2016
#
#   Description:  Demonstrate dynamic referencing
#####################################################
#
#   DATE        AUTHOR  DESCRIPTION
#   08/12/2016  RR      initialised
#
#####################################################
import sys

def printline():
    print "-------------------------------------------\n"
    
def showNumReferences(val):
    print "\n-------------------------------------------"
    print "current value = " + str(val)
    print "num references = " + str(sys.getrefcount(val))
    print "-------------------------------------------\n"
    
    
print("Dynamic referencing demonstration")
printline()


x = "hello"
y = x

print('x = ' + x)
print('y = ' + y)

y = "world"

print('\nx = ' + x)
print('y = ' + y)


x = "a completely new string"
print "\n-------------------------------------------"
print "current value = " + str(x)
print "num references = " + str(sys.getrefcount(x))
print "-------------------------------------------\n"

showNumReferences(x)

x = 1
showNumReferences(x)

# MUTABLE CHANGES - IN PLACE!!!
h = ['hello']
i = h
i[0] = ['world']

print(h)
print(i)





