from string import ascii_lowercase

a = ascii_lowercase
n = int(input("몇 칸 shift 하시겠습니까?"))
b = a[n:] + a[:n]
print(b) 

list(a)
list(b)

암호 = {k: v for k, v in zip(list(a), list(b))}
print(암호["b"])