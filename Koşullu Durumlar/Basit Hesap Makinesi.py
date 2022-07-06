# Hoş Geldiniz Ekranı ve İşlem Bilgileri

print ("""----------------------------------------------

Hesap Makinesi Programına Hoş Geldiniz...

İşlemler ;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi

----------------------------------------------
""")

# Kullanıcıdan Bilgileri Alalım

a = int(input("Birinci Sayı: "))
b = int(input("ikinci Sayı: "))

işlem = input("İşlemi Giriniz: ")

# İşlemler

if işlem == "1":
    print ("{} + {} = {}".format(a,b,a+b))  # Toplama
elif işlem == "2":
    print ("{} - {} = {}".format(a,b,a-b))  # Çıkarma
elif işlem == "3":
    print ("{} * {} = {}".format(a,b,a*b))  # Çarpma
elif işlem == "4":
    print ("{} / {} = {}".format(a,b,a/b))  # Bölme

else:
    print("İşlem için lütfen 1,2,3 ve 4 arasında bir sayı seçin")  # Hata Ekranı











