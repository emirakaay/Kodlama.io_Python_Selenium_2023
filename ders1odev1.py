#Veri Türleri (DERS1 ÖDEV1)

# integer: Tam Sayılarda kullanılır; örn: 5, 10, 25…

# string: Metinsel verilerde kullanılır;  örn: “Merhaba Dünya”

# float: Ondalıklı sayılarda kullanılır;  örn: 3.2, 0.55…

# list: Liste yapmak için kullanılırız;  örn: [”emir”, “akay”]

# boolan: true ve false durumlarında kullanırız.

# Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz veriler

# Sitede bulunan (eğitmenler kısmı) metinsel veri tipi şeklindedir.
# Kurs ilerleme yüzdesinin gösterildiği alan int veri tipidir.


# Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz;


kullaniciAdi= "emirakay"
sifre= 1234

kullaniciAdiGirisi= input("Kullanıcı Adı: ")
sifreGirisi= int(input("Şifre Giriniz: "))

if kullaniciAdi == kullaniciAdiGirisi and sifre == sifreGirisi:
    print("Giriş Yapılıyor...")

else:
    print("Giriş Başarısız!")
