#####################################################
#   Author:       RR
#   Created:      09/12/2016
#
#   Description:  Demonstration of tuples
#####################################################
#
#   DATE        AUTHOR  DESCRIPTION
#   09/12/2016  RR      initialised
#
#####################################################

x = 0

# while demoing break and continue
while x < 10:
    x += 1      #NEEDS TO BE AT TOP OR IT WILL GO INTO INFINITE LOOP

    if x == 8:
        break;
    
    elif x % 2 == 0:
        print x
    else:
        continue

