# Kullanıcıdan Boy ve Kilo Değerlerini Alalım

print ("""Beden Kitle İndeksi Programına Hoş Geldiniz

Beden Kitle İndeksinizi Ölçmek İçin;
Boy ve Kilo Değerlerinizi Almalıyız
""")

# Boy ve Kilo Alımı

boy = float(input("Boyunuz: "))
kilo = int(input("Kilonuz: "))

bki = kilo / boy * boy

# Sonuç

if (bki < 18.5):
    print("Zayıf")

elif (bki >= 18.5 and bki < 25):
    print("Normal")

elif (bki >= 25 and bki < 30):
    print("Fazla Kilolu")

else:
    print("Obez")

