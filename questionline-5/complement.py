#given number= -42
n=(2**8)-42
b=" "
while n>0:
      r=n%2
      b=b+str(r)
      n=n//2
print("2's complement of -42 is:",b[::-1])

#OR METHOD

#given number= -42
def binary(num):
      t=""
      while num>0:
            rem=num%2
            t=t+str(rem)
            num=num//2
      y=t[::-1]
      return y

def decimal(num):
      s=0
      w=str(num)
      y=w[::-1]
      for i in range(len(y)):
            s=s+(2**i)*(int(y[i]))
      return s

r="00"+binary(42)  # As it is told 8-bits Adding 2 zeroes in front so that binary of 42 which is only 6 bits becomes 8-bits
q=""
for i in r:
      if i in "1":
            q=q+"0"
      else:
            q=q+"1"
e=decimal(q)
q=e+1
u=binary(q)
print("2's Complement of -42 is:",u)
