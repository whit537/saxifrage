#!/usr/bin/env python

# The "import" statement finds modules (whatever those are!) and defines names
# in a namespace (whatever that is!):                                                                          
#                                                                                                              
#   http://docs.python.org/reference/simple_stmts.html#the-import-statement                                    
#                                                                                                              
# The "sys" module provides things related (apparently) to the interpreter
# (whatever that is!):                                                                                         
#                                                                                                              
#   http://docs.python.org/library/sys.html

import sys

USAGE = "Usage: ./find.py word filename [filename]*"

def fail(msg):
    print >> sys.stderr, USAGE
    print >> sys.stderr, msg
    sys.exit()

try:
    word = sys.argv[1]
except IndexError:
    fail("Please provide a word to find.")

filenames = sys.argv[2:]
if not filenames:
    fail("Please enter at least one filename.")

for filename in filenames:
    file_pointer = open(filename)
    for line in file_pointer:
        if word in line:
            print filename
            break