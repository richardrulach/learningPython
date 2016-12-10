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
reResult = re.match(test, 'is there a number here 111-111 and 222-2fds22 is also here')
print(reResult)




