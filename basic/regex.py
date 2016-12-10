#####################################################
#   Author:       RR
#   Created:      10/12/2016
#
#   Description:  Regular expressions
#####################################################
#
#   DATE        AUTHOR  DESCRIPTION
#   10/12/2016  RR      initialised
#
#####################################################

import re

test = re.compile(r'\d\d\d-\d\d\d')
s1 = '333-444is there a number here 111-111 and 222-222 is also here'

print('match from start:')
reResult = re.match(test, s1)
print(reResult.group(0) + '\n\n')

reResult = re.findall(test, s1)

print('find all:')
for x in reResult:
    print(x)
    





