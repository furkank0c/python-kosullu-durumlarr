# Bilgilendirme Ekranı

print("**********\nKullanıcı Girişi\n**********\n")

# Sistemde Kayıtlı Olduğunu Düşündüğümüz Kullanıcı Adı ve Parola

sys_kullanıcı_adı = "KULLANICI ADI"  # Kullanıcı adını istediğiniz şekilde değiştirebilirsiniz
sys_parola = "PAROLA"                # Parolayı istediğiniz şekilde değiştirebilirsiniz

# Sistem Girişi

kullanıcı_adı = input("Kullanıcı Adı: ")    # Kullanıcı Adı
parola = input("Parola: ")                  # Parola

if (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
    print ("Parola Hatalı!")                           # Parola Hatalı

elif (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
    print ("Kullanıcı Adı Hatalı!")                    # Kullanıcı Adı Hatalı

elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
    print ("Kullanıcı Adı ve Parola Hatalı!")          # Kullanıcı Adı ve Parola Hatalı

else:
    print ("Sisteme Başarı İle Girildi...")
