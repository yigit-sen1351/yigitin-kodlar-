s1=float(input("İlk Sayınınzı Giriniz : "))
s2=float(input("İkinci Sayınınzı Giriniz : "))
islem=input(("+,-,*,/""\n"))
if islem== "+":
    print(s1+s2)
elif islem== "-":
    if s1<s2:
        print(s2-s1)
    elif s2<s1:
        print(s1-s2)
elif islem== "*":
    print(s1*s2)
elif islem == "/":
    if s1<s2:
        print(s2/s1)
    elif s2<s1:
        print(s1/s2)  