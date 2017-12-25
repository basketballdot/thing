#!/usr/bin/env python
import sys

IPv6Address=sys.argv[1]
PtrNs=sys.argv[2]

lenth=int(len(IPv6Address.split(':')))
actlen=9-int(lenth)


def Nzero(n):
    c=':'.join(int(n) * '0'.zfill(4).split(':'))
    #b=int(n) * '0'.split(':')
    #c=':'.join(b)
    d=':' + c +':'
    print d
    #print d #:0000:0000:0000:0000: 
    return  d #:0000:0000:0000:0000: 

def Ipv6AddRev(a):
    nn=Nzero(actlen)
    d=a.replace("::", nn) 
    #print d #2001:dc7:1000:0:0:0:0:1
    dotlist=[]
    for i in d.split(':'):
        c=i.zfill(4)  #'123'.zfill(4) ===>'0123'
        e='.'.join(c)
        #e='.'.join(i.zfill(4))
        dotlist.append(e)
    #print dotlist #['2.0.0.1', '0.d.c.7', '1.0.0.0', '0.0.0.0', '0.0.0.0', '0.0.0.0', '0.0.0.0', '0.0.0.1'] 
    Ipv6Str='.'.join(dotlist) #2.0.0.1.0.d.c.7.1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1
    Ipv6Rev=Ipv6Str[::-1]+'.ip6.arpa.' #1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.7.c.d.0.1.0.0.2.ip6.arpa.
    return Ipv6Rev 

if __name__ == '__main__':
    IPv6Address=sys.argv[1]
    PtrNs=sys.argv[2]
    ss=Ipv6AddRev(IPv6Address)
    print 'update add '+ss +'\t'+ '3600'+'\t'+'IN' +'\t'+ 'PTR' +'\t'+PtrNs.strip('.')+'.' 
