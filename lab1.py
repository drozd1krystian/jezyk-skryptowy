#zad1
print(2+2)
print(5/2)
print(10*5)
print(25*33/5+2)
print()

#zad2
imie=input("podaj imie\n")
print("Witaj "+imie)

#zad3
x=5
suma=0
while x>0:
    x=float(input("podaj liczbe"))
    suma=suma+x
print("Wynik = "+str(suma))

#zad4

print(str(sum(range(8,81,1))))


#zad 5

from datetime import date
today = date.today()

data=date(2018,3,4)
czas= abs(today-data)
print(str(czas.days))

#zad 6

a=int(input("Podaj liczbe"))
b=int(input("Podaj druga liczbe"))

print("1-dodawanie, 2-odejmowanie, 3-mnozenie, 4-dzielenie")

x=input("Co chcesz zrobic?")

if x==1:
    print(a+b)
elif x==2:
    print(a-b)
elif x==3:
    print(a*b)
else:
    if b!=0:
       print(a/b)