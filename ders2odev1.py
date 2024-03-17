
ogrencier = ["Emir Akay","Veysel Solak"]

#Aldığı isim soy isim ile listeye öğrenci ekleyen

def ogrEkle():
    ogrenciEkle = input("Eklenecek olan öğrencinin adını ve soyadını giriniz: ")
    ogrencier.append(ogrenciEkle)
    print(ogrencier)
ogrEkle()

#Aldığı isim soy isim ile eşleşen değeri listeden kaldıran

def ogrSil():
    ogrenciSilmek = input("Silinecek olan öğrencinin adını ve soyadını giriniz: ")
    ogrencier.remove(ogrenciSilmek)
    print(ogrencier)
ogrSil()

#Listeye birden fazla öğrenci eklemeyi mümkün kılan

def cokluOgrenci():
    sayi= int(input("Kaç tane öğrenci gireceksiniz: "))
    for i in range(sayi):
        ogrenciEkle = input("Eklenecek olan öğrencilerin adını ve soyadını giriniz: ")
        ogrencier.append(ogrenciEkle)
        print(ogrencier)
cokluOgrenci()

#Listedeki tüm öğrencileri tek tek ekrana yazdıran

for a in ogrencier:
    print(ogrencier)

#Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan

def ogrenciIndex():
    print(ogrencier)
    for i in range(len(ogrencier)):
        print(f"Numara: {i}  İsim: {ogrencier[i]}")
print(ogrencier)
ogrenciIndex()

#Listeden birden fazla öğrenci silmeyi mümkün kılan 

def ogrListeSil():
    sayi2 = int(input("Kaç tane öğrenci sileceksiniz: "))
    i = 0
    while i < sayi2:
        cokluSilme = input("Silinecek olan öğrencilerin adını ve soyadını giriniz: ")
        ogrencier.remove(cokluSilme)
        print(ogrencier)
        i += 1
ogrListeSil()

def ogrListeSil():
    sayi2 = int(input("Kaç tane öğrenci sileceksiniz: "))
    i = 0
    while i < sayi2:
        cokluSilme = input("Silinecek olan öğrencilerin adını ve soyadını giriniz: ")
        ogrencier.remove(cokluSilme)
        print(ogrencier)
        i += 1
ogrListeSil()
