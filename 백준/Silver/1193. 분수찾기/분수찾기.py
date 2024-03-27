X = int(input())

length = 1
while X > length:
    X -= length 
    length += 1

if length % 2 ==0:
    y = X
    x = length - X + 1
else:
    y = length - X + 1
    x = X

print(str(y)+'/'+str(x))