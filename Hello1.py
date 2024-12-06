import random
a=random.randint(10,100)
b=random.randint(10,100)
c = a+b
print(a, '+', b, '=', end=' ')
ans = input()
ans = int(ans)
if (ans == c):
    print('0')
else:
    print('x')
