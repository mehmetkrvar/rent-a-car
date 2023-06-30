# OtoKiralamaSistemi

Bu, basit bir oto kiralama sistemi uygulamasıdır. Kullanıcılar araçları sisteme ekleyebilir, araç kiralayabilir ve iade edebilir.

## Nasıl Kullanılır

1. `main.py` dosyasını çalıştırarak programı başlatın.
2. Aracınızı sisteme eklemek için `OtoKiralamaSistemi` sınıfının `arac_ekle()` yöntemini kullanın. Örnek kod: 

   ```python
   oto_kiralama_sistemi = OtoKiralamaSistemi()
   arac = Arac("Marka", "Model", 2023, 100)
   oto_kiralama_sistemi.arac_ekle(arac)
   ```
Araç kiralama durumunu kontrol etmek için OtoKiralamaSistemi sınıfının arac_kiralama_durumu() yöntemini kullanın. Örnek kod:
   ```python
   oto_kiralama_sistemi.arac_kiralama_durumu()
```
Bir araç kiralama işlemi gerçekleştirmek için OtoKiralamaSistemi sınıfının arac_kirala() yöntemini kullanın. Örnek kod:
