s = list(input())

total1 = s.count('1')

if total1 % 2 == 0:
    s.append('0')
else:
    s.append('1')

print("".join(s))