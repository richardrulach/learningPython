#####################################################
#   Author:       RR
#   Created:      10/12/2016
#
#   Description:  Time and sleep functions
#####################################################
#
#   DATE        AUTHOR  DESCRIPTION
#   10/12/2016  RR      initialised
#
#####################################################
import time
import sys

def pr(x):
     sys.stdout.write(x)

print(1)
time.sleep(0.1)

print(2)
time.sleep(0.2)

print(3)
time.sleep(0.3)

print(4)

print('What size of tree do you want?\n')
size = int(input()) + 1

for x in range(1,size):
     pr(' ' * (size - x + 2))
     pr('x' * (x * 2 - 1) + '\n')
     time.sleep(0.2)

