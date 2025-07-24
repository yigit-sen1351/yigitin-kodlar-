import random
import time 
o1_puan=100
o2_puan=100
def oyun():
    global o1_puan, o2_puan 
    pc_karar =["taş","kağıt","makas"]
    oyuncu1 = random.choice(pc_karar)
    print("1.hamle : ",oyuncu1)
    oyuncu2 = random.choice(pc_karar)
    print("2.hamle : ",oyuncu2)
    
        
    if oyuncu1=="makas" and oyuncu2== "kağıt":
        print("oyuncu 1 kazandı")
        o1_puan+=50
        print(" \n")
    elif oyuncu1 == "makas" and oyuncu2 == "taş":
        print("oyuncu 2 kazandı")
        o2_puan+=50
        print(" \n")
    elif oyuncu1 == "makas" and oyuncu2 == "makas":
        print("kazanan yok","tekrar")
        print(" \n")
    elif oyuncu1 == "kağıt" and oyuncu2 == "makas":
        print("oyuncu 2 kazandı")
        o2_puan+=50
        print(" \n")
    elif oyuncu1 == "kağıt" and oyuncu2 == "taş":
        print("oyuncu 1 kazandı")
        o1_puan+=50
        print(" \n")
    elif oyuncu1 == "kağıt" and oyuncu2 == "kağıt":
        print("kazanan yok","tekrar")
        print(" \n")
    elif oyuncu1 == "taş" and oyuncu2== "makas":
        print("oyuncu 1 kazandı")
        o1_puan+=50
        print(" \n")
    elif oyuncu1 == "taş" and oyuncu2 == "kağıt":
        print("oyuncu 2 kazandı")
        o2_puan+=50
        print(" \n")
    elif oyuncu1=="taş" and oyuncu2=="taş":
        print("kazanan yok ","tekrar")
        
    print("puan durumu \n","oyuncu 1 puanı : ",o1_puan," \noyuncu 2 puanı : ",o2_puan)
    print(" \n")



while True:
    for i in range(5):
        oyun()
        time.sleep(2)
    if o1_puan >= 250 or o2_puan >= 250:
        print("Kazanan:", "Oyuncu 1" if o1_puan > o2_puan else "Oyuncu 2")
    tekrar = input("Tekrar oynamak ister misin? (E/H)\n").strip().upper()
    if tekrar == "E":
        o1_puan = 100
        o2_puan = 100
        print("Yeni oyun başlatılıyor ")
    else:
        print("Oynadığınız için teşekkürler")
        break
