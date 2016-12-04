#####################################################
#   Author:       RR
#   Created:      04/12/2016
#
#   Description:  Demonstration of tuples
#####################################################
#
#   DATE        AUTHOR  DESCRIPTION
#   04/12/2016  RR      initialised
#
#####################################################


# DECLARING A TUPLE
mytuple = ("a","b","c")

print(mytuple)

# ACCESSING THE VALUES OR GETTING SUB TUPLES
print(mytuple[1])
print(mytuple[1:])
print(mytuple[:1])


# SWAPPING THE CONTENTS OF VARIABLES USING TUPLE SYNTAX

x = "steve"
y = "annie"

print("x:" + x)
print("y:" + y)
print("\n")

(x,y) = (y,x)

print("x:" + x)
print("y:" + y)

