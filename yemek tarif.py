import random
ana_malzeme=["tavuk", "et", "balık", "kabak", "patates", "makarna", "nohut"]#random seçilicek ana malzeme listesi
pisirme_sekli=["fırında", "ızgarada", "haşlayarak", "kızartarak", "buharda"]#random seçilicek  pişirme şekli
ek_malzeme=["soğan", "sarımsak", "yoğurt", "domates", "baharat karışımı", "zeytinyağı", "kaşar peyniri"]#random seçilicek ek malzeme listesi
sunum=["pilav eşliğinde", "lavaş içinde", "yeşillik yatağında", "yoğurtla", "limonla", "sade"]#random seçilicek sunum listesi
icecekler=["limonata", "çay", "su", "kola", "fanta", "soda", "meyve"]#random seçilicek içecekler
def tarif():#tarif adında fonksiyon oluşturuldu
    ana = random.choice(ana_malzeme)#ana_malzeme listesinin random seçim işlemi yapılmıştır
    pisirme= random.choice(pisirme_sekli)#pisirme_sekli listesinin random seçim işlemi yapılmıştır
    ek= random.sample(ek_malzeme,2)#ek_malzeme listesinin random seçim işlemi yapılmıştır
    sun= random.choice(sunum)#sunum listesinin random seçim işlemi yapılmıştır
    icecek= random.choice(icecekler)#icecekler listesinin random seçim işlemi yapılmıştır
    print("Bugünün Yemek Menüsü")
    print(f"{ana} {pisirme} pişirilir,içine ek olarak {ek[0]} ve {ek[1]} eklenir")
    print(f"{sun} servis edilir. Afiyet Olsun.")
tarif()#fonksiyon çağrılmıştır
