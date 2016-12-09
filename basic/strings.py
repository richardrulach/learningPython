#####################################################
#   Author:       RR
#   Created:      04/12/2016
#
#   Description:  Working with strings
#####################################################
#
#   DATE        AUTHOR  DESCRIPTION
#   09/12/2016  RR      initialised
#
#####################################################

s = "Where is there hope in the world?"

print("Accessing as a sequence of characters:")

print(s[0:5])

print(s[-6:])

print(s[::-1])

print(s[::2])

print("Using functions:")

print(s.startswith("Where"))

print(s.endswith("world"))

print("hello".upper())

print("WHERE IS THE REMOTE?".lower())

print("\n\nString formatting with %:")

name = "Tom"
emotion = "happy"
print("welcome %s" % name)
print("welcome %s are you %s?" % (name, emotion))

print("\n\nNumber formatting string with %:")
print("it will cost %.4d" % (2.45676))
print("it will cost %.2f" % (2.45676))


