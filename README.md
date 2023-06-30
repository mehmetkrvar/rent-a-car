# OtoKiralamaSistemi

Bu, basit bir oto kiralama sistemi uygulamasıdır. Kullanıcılar araçları sisteme ekleyebilir, araç kiralayabilir ve iade edebilir.

## Nasıl Kullanılır

1. main.py dosyasını çalıştırarak programı başlatın.
2. Aracınızı sisteme eklemek için OtoKiralamaSistemi sınıfının arac_ekle() yöntemini kullanın. Örnek kod: 

   ```python
   oto_kiralama_sistemi = OtoKiralamaSistemi()
   arac = Arac("Marka", "Model", 2023, 100)
   oto_kiralama_sistemi.arac_ekle(arac)
   ```
3.Araç kiralama durumunu kontrol etmek için OtoKiralamaSistemi sınıfının arac_kiralama_durumu() yöntemini kullanın. Örnek kod:
   ```python
   oto_kiralama_sistemi.arac_kiralama_durumu()
```
4.Bir araç kiralama işlemi gerçekleştirmek için OtoKiralamaSistemi sınıfının arac_kirala() yöntemini kullanın. Örnek kod:
```python
oto_kiralama_sistemi.arac_kirala("Marka", "Model")
```
5.Bir aracı iade etmek için OtoKiralamaSistemi sınıfının arac_iade_et() yöntemini kullanın. Örnek kod:
 ```python
oto_kiralama_sistemi.arac_iade_et("Marka", "Model")
```

## Araç Listesini Yükleme
Araç listesini bir dosyadan yüklemek için arac_listesini_yukle() fonksiyonunu kullanabilirsiniz. Fonksiyon, dosyayı okur ve her satırı bir araç nesnesine dönüştürerek bir araç listesi döndürür. Örnek kod:
```python
arac_listesi = arac_listesini_yukle("arac_listesi.txt")
oto_kiralama_sistemi = OtoKiralamaSistemi()
for arac in arac_listesi:
    oto_kiralama_sistemi.arac_ekle(arac)
```
Dosya biçimi şu şekilde olmalıdır: marka, model, yıl, günlük ücret.
Bu projeyi çalıştırmak için Python 3 gereklidir.
