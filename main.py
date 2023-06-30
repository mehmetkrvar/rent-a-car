class Arac:
    def __init__(self, marka, model, yil, gunluk_ucret):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.gunluk_ucret = gunluk_ucret
        self.kirada_mi = False
    def kiralama_durumu(self):
        if self.kirada_mi:
            return "Kirada"
        else:
            return "Boşta"
    def araci_kirala(self):
        if not self.kirada_mi:
            self.kirada_mi = True
            print(f"{self.marka} {self.model} başarıyla kiralandı.")
        else:
            print(f"{self.marka} {self.model} zaten kirada.")
    def araci_iade_et(self):
        if self.kirada_mi:
            self.kirada_mi = False
            print(f"{self.marka} {self.model} başarıyla iade edildi.")
        else:
            print(f"{self.marka} {self.model} zaten boşta.")
class OtoKiralamaSistemi:
    def __init__(self):
        self.arac_listesi = []
    def arac_ekle(self, arac):
        self.arac_listesi.append(arac)
        print(f"{arac.marka} {arac.model} sisteme eklendi.")
    def arac_kiralama_durumu(self):
        for arac in self.arac_listesi:
            print(f"Marka: {arac.marka}, Model: {arac.model}, Kiralama Durumu: {arac.kiralama_durumu()}")
    def arac_kirala(self, marka, model):
        for arac in self.arac_listesi:
            if arac.marka == marka and arac.model == model:
                arac.araci_kirala()
                return
        print("Araç bulunamadı.")  
    def arac_iade_et(self, marka, model):
        for arac in self.arac_listesi:
            if arac.marka == marka and arac.model == model:
                arac.araci_iade_et()
                return
        print("Araç bulunamadı.")
def arac_listesini_yukle(dosya):
    arac_listesi = []
    with open(dosya, 'r') as f:
        for satir in f:
            marka, model, yil, gunluk_ucret = satir.strip().split(',')
            arac = Arac(marka, model, int(yil), float(gunluk_ucret))
            arac_listesi.append(arac)
    return arac_listesi
