days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month = [31,28,31,30,31,30,31,31,30,31,30,31]

x,y = map(int, input().split())

day = 0
for i in range(x-1):
    day += month[i]
day += y
print(days[day % 7])