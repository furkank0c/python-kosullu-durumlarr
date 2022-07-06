# Kullanıcıdan 3 Sayı Alalım

a = int(input("1. Sayıyı Yazınız: "))
b = int(input("2. Sayıyı Giriniz: "))
c = int(input("3. Sayıyı Giriniz: "))

# Karşılaştırma

if (a > b and a > c):
    print (a)

elif (b > a and b > c):
    print (b)

else:
    print (c)