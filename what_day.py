days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a = 1
b = 1
c = (sum(days[0:a]) + b) % 7
day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
print(day[c-1])