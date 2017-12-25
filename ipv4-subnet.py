#!/usr/bin/env python

import sys
import os

#v6addr = sys.argv[1]
#v6submask = sys.argv[2]
#2001:dc7:1000::/120 126
"""
v6addrmask=v6addr.split('/')[1]
128 - 120 

"""

base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
# base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]

#16--->10---2
#hex2dec---->dec2bin

def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


def hex2dec(string_num):
    return str(int(string_num.upper(), 16))

def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))

def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))

#print hex2bin(str(v6addr))

def Nzero(n):
    c=':'.join(int(n) * '0'.zfill(4).split(':'))
    #b=int(n) * '0'.split(':')
    #c=':'.join(b)
    d=':' + c 
    #print d  #:0000:0000:0000:0000: 
    return d  #:0000:0000:0000:0000: 

a='2001:dc7:1000::1/120'
b=126

nethost=a.split('/')[0]
netmask=a.split('/')[1]

total=int(128)
netprefix=total-int(netmask)

actlen=len(nethost.strip(':').split(':'))
print actlen

b=nethost.split(':')
mergeZero=int(8)-int(actlen)

nn=Nzero(actlen)
d=nethost.replace("::", nn)
print b
print d
