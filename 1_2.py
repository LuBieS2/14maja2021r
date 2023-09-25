n=5000
if n < 1000 or n > 8999:
    print("nieprawidlowa liczba")
n_list=[]
for i in str(n):
    n_list.append(int(i))
d_list=[]
for i in n_list:
    n=9-i
    d_list.append(n)
d=""
for i in d_list:
    d=d+str(i)
print(d)