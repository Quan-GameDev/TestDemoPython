import base64

a = 'TmljZSEgTm93IGtlZXAgZ29pbmcuIDU0Nzc2ZjIwNmQ2ZjcyNjUyZTIwMzAzMTMwMzAzMDMxMzEzMDIwMzAzMTMxMzAzMTMwMzAzMTIwMzAzMTMxMzAzMTMxMzEzMDIwMzAzMTMxMzAzMDMwMzAzMTIwMzAzMTMxMzAzMTMxMzAzMDIwMzAzMDMxMzAzMDMwMzAzMDIwMzAzMTMwMzAzMDMxMzAzMDIwMzAzMTMxMzAzMDMxMzAzMTIwMzAzMTMxMzAzMDMwMzEzMTIwMzAzMTMxMzEzMDMwMzEzMDIwMzAzMTMxMzEzMTMwMzAzMTIwMzAzMTMxMzEzMDMwMzAzMDIwMzAzMTMxMzEzMDMxMzAzMDIwMzAzMTMxMzAzMTMwMzAzMTIwMzAzMTMxMzAzMTMxMzEzMTIwMzAzMTMxMzAzMTMxMzEzMDIwMzAzMDMxMzAzMDMwMzAzMTIwMzAzMDMxMzAzMDMwMzAzMDIwMzAzMTMwMzEzMDMwMzAzMTIwMzAzMDMxMzEzMDMwMzAzMTIwMzAzMTMwMzEzMDMwMzEzMDIwMzAzMTMwMzAzMDMxMzEzMTIwMzAzMTMxMzAzMDMxMzAzMTIwMzAzMDMxMzEzMDMwMzAzMDIwMzAzMTMxMzAzMTMxMzAzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMwMzAzMTIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMDMxMzEzMDMwMzAzMTIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMTMwMzAzMDMxMzEzMDIwMzAzMTMwMzAzMTMwMzEzMDIwMzAzMTMwMzEzMDMwMzAzMDIwMzAzMTMwMzEzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMTMwMzEzMDMwMzEzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzAzMDIwMzAzMDMxMzEzMDMwMzAzMDIwMzAzMTMwMzEzMTMwMzEzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzEzMTIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMDMxMzEzMTMwMzAzMTIwMzAzMTMwMzEzMDMxMzEzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMwMzAzMTIwMzAzMDMxMzEzMTMxMzAzMTIwMzAzMDMxMzEzMTMxMzAzMQ=='

flag = base64.b64decode(a)

print(flag)

#Giai ma lan 1
b = '54776f206d6f72652e203031303030313130203031313031303031203031313031313130203031313030303031203031313031313030203030313030303030203031303030313030203031313030313031203031313030303131203031313130303130203031313131303031203031313130303030203031313130313030203031313031303031203031313031313131203031313031313130203030313030303031203030313030303030203031303130303031203030313130303031203031303130303130203031303030313131203031313030313031203030313130303030203031313031313030203031313030313130203031303130303031203031303130313031203030313130303031203031313030313130203031303130313031203031303030313130203031303031303130203031303130303030203031303130313130203031303130313031203031303130303130203031313030313130203031303130313030203030313130303030203031303131303130203031313030313130203031303130313131203031303130313031203030313131303031203031303130313130203031313030313130203031303130303031203030313131313031203030313131313031'

#Giai ma hexa -> String
flag = bytes.fromhex(b)

print(flag)

#Giai ma lan 2
c= '01000110 01101001 01101110 01100001 01101100 00100000 01000100 01100101 01100011 01110010 01111001 01110000 01110100 01101001 01101111 01101110 00100001 00100000 01010001 00110001 01010010 01000111 01100101 00110000 01101100 01100110 01010001 01010101 00110001 01100110 01010101 01000110 01001010 01010000 01010110 01010101 01010010 01100110 01010100 00110000 01011010 01100110 01010111 01010101 00111001 01010110 01100110 01010001 00111101 00111101'

#Chuyen thanh kieu mang 1 chieu
n = c.split()
print(n)

#Su dung vong lap for
#Chuyen doi sang ky tu
#Cong don ky tu
flag = ''
for i in n:
    flag += chr(int(i,2))

print(flag)

#Giai ma base64
f = 'Q1RGe0lfQU1fUFJPVURfT0ZfWU9VfQ=='
flag = base64.b64decode(f)

print(flag)