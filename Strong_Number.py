import math
n=int(input())
c=0
for i in str(n):
    F=math.factorial(int(i))
    c+=F
if c==n:
    print("The number {} is a strong number".format(n))
else:
    print("The number {} is not a strong number".format(n))

