#!/usr/bin/python3
for _ in range(0, 99):
#    if (( _ % 10 ) > 9):
#        char = ( _ % 10 ) + 97
#        val = chr(char)
#    else:
#        val = _
    print("{} = {}".format(_, hex(_)))
