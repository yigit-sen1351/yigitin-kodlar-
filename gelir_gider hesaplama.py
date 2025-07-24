print("=== GELİR GİRİŞİ ===")
gelirler=[]
for i in range(5):
    gelir= input("Gelir kalemi gir (bitirmek için 'q') : ")
    if gelir.lower() == 'q':
        break
    try:
        girdi=int(gelir)
        gelirler.append(girdi)
    except:
        print("hata var")
print("\n=== GİDER GİRİŞİ ===")
giderler=[]
for i in range(5):
    gider= input("Gider kalemi gir (bitirmek için 'q') : ")
    if gider.lower() == 'q':
        break
    try:
        cikti=int(gider)
        giderler.append(cikti)
    except:
        print("hata var")
toplam_gelir=sum(gelirler)
toplam_gider=sum(giderler)
butcen= toplam_gelir - toplam_gider

print("\n=== BÜTÇE DURUMU ===")
print("Toplam Gelir :", toplam_gelir)
print("Toplam Gider :", toplam_gider)
print("Bütçe        :", butcen)
if butcen < 0 :
    print("Durumun : Zarardasın")
elif butcen > 0:
    print("Durumun :",butcen,"TL Kardasın")
else :
    print("kar ya da zarar yok")

        
        
