File = open('chuj.txt', 'r')
A = list(map(str.strip,File.readlines()))
A = [item.split(" ") for item in A]
A= [item for l in A for item in l]
print(A)
Sign = []
import string
Alphabet=list(string.ascii_uppercase)
print(Alphabet)
def DOPISZ(a):
    Sign.append(a)
def ZMIEN(a):
    licznik=0
    for i in Sign:
        licznik=licznik+1
    Sign[licznik-1]=a
def USUN_1():
    licznik=0
    for i in Sign:
        licznik=licznik+1
    Sign.pop(licznik-1)
def PRZESUN(a):
    ##for i in Alphabet:
    n=0
        ##if a in i:
    licznik = 0
    for x in Alphabet:

        if(a != Alphabet[n]) and  (a >= Alphabet[n]):
            licznik=licznik+1
        #print(licznik)
        #print(Alphabet[licznik])
        n = n + 1
    n=0
    if a != str(a):

        print(" ")
    else:
        for i in Sign:
            if a in i:
                break
            n=n+1
        if licznik<25:
            Sign[n]=Alphabet[licznik+1]
        else:
            Sign[n]='A'

JD=0
for i in A:
    if A[JD]=="DOPISZ":
        DOPISZ(A[JD+1])
    if A[JD]=="USUN":
        USUN_1()
    if A[JD]=="ZMIEN":
        ZMIEN(A[JD+1])
    if A[JD]=="PRZESUN":
        PRZESUN(A[JD+1])

    JD=JD+1
#4.1
chuj=0
for i in Sign:
    chuj=chuj+1
print(Sign)
print(chuj)
#4.2
licznik=0
Dis=2 #Jebac orka
niggest_number=0
niggest_phrase=""
for i in A:
    ulumulu=len(A)-2
    if Dis<ulumulu:

        if A[Dis] == A[Dis+2]:
            licznik=licznik+1
        if A[Dis] != A[Dis+2]:
            licznik = 1

        if licznik>=niggest_number:
            niggest_number=licznik
            niggest_phrase=A[Dis]

    else:
        licznik=0
    Dis=Dis+2
    print(niggest_number)
    print("chuj")
