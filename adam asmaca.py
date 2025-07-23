import random

kelimeler =["kalemlik"]
gizli_kelime = random.choice(kelimeler)
tahmin_edilen = ["_" for _ in gizli_kelime]
tahminler = []
hak = 6

adam_cizimleri = [
    """
     _______
    |/      |
    |
    |
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      ( )
    |
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      ( )
    |       |
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      ( )
    |      /|
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      ( )
    |      /|\\
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      ( )
    |      /|\\
    |      /
    |
    |___
    """,
    """
     _______
    |/      |
    |      ( )
    |      /|\\
    |      / \\
    |
    |___
    """
]

print(" Adam Asmaca oyununa hoş geldin!")
print("Kelime", len(gizli_kelime), "harfli. Başlayalım!\n")

while hak > 0:
    print(adam_cizimleri[6 - hak])
    print("Kelime: ", " ".join(tahmin_edilen))
    print("Tahmin edilen harfler:", " ".join(tahminler))

    harf = input("Bir harf tahmin et: ").lower()

    if not harf.isalpha() or len(harf) != 1:
        print("Lütfen sadece 1 harf gir.\n")
        continue

    if harf in tahminler:
        print(" Bu harfi zaten tahmin ettin.\n")
        continue

    tahminler.append(harf)

    if harf in gizli_kelime:
        for i in range(len(gizli_kelime)):
            if gizli_kelime[i] == harf:
                tahmin_edilen[i] = harf
        print(" Doğru tahmin!\n")
    else:
        hak -= 1
        print("Yanlış tahmin. Kalan hakkın:", hak, "\n")

    if "_" not in tahmin_edilen:
        print("TEBRİKLER Yiğit abi! Kelimeyi buldun:", gizli_kelime)
        break

if hak == 0:
    print(adam_cizimleri[6])
    print(" Kaybettin! Kelime:",gizli_kelime)