#!/bin/python
#author: tobias mueller 13.6.13
#byteplay test

from sys import version_info
from dis import dis
try:
    from dis import HAVE_ARGUMENT
    if version_info.major == 3:from byteplay import *
    else:from byteplay2 import *
except ImportError:
    from wbyteplay import *
from pprint import pprint

def f(a, b):
    res = a + b
    return res

def g(a, b):
    res = a + b if a < b else b + a
    r = 0
    for a in range(res):
        r += 1
    return r or 2

for x in (f, g):
    #get byte code for f
    c = Code.from_code(x.__code__)
    pprint(c.code)

    #generate byte code
    cnew = c.to_code()

    x.__code__ = cnew
    dis(x)

    print(x(3,5))