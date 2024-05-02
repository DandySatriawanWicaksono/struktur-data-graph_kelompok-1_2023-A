class Peta:
    def __init__(self):
        self.cityList = {}
    
    def printPeta(self):
        for kota in self.cityList:
            print(kota, ":",self.cityList[kota])
        
    def tambahkanKota(self,kota):
        if kota not in self.cityList:
            self.cityList[kota] = []
            return True
        return False
    
    def hapusKota(self,kotaDihapus):
        # Menghapus jalan yang terhubung dengan cara menghapus kota yang akan dihilangkan 
        if kotaDihapus in self.cityList:
            for kotalain in self.cityList:
                if kotaDihapus in self.cityList[kotalain]:
                    self.cityList[kotalain].remove(kotaDihapus)
            del self.cityList[kotaDihapus]
            return True
        return False
    
    def tambahkanJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            # Masukkan kota 1 di list kota 2
            self.cityList[kota2].append(kota1)
            # Masukkan kota 2 di list kota 1
            self.cityList[kota1].append(kota2)
            return True
        return False
    
    def hapusJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            # Menghapus kota 1 di list kota 2
            self.cityList[kota2].remove(kota1)
            # Menghapus kota 1 di list kota 1
            self.cityList[kota1].remove(kota2)
            return True
        return False

peta_jatim = Peta()
peta_jatim.tambahkanKota("Surabaya")
peta_jatim.tambahkanKota("Sidoarjo")
peta_jatim.tambahkanKota("Probolinggo")
peta_jatim.tambahkanKota("Malang")
peta_jatim.tambahkanKota("Blitar")
peta_jatim.tambahkanKota("Nganjuk")
peta_jatim.tambahkanKota("Ponorogo")
peta_jatim.tambahkanKota("Ngawi")
peta_jatim.tambahkanKota("Bojonegoro")
peta_jatim.tambahkanKota("Tuban")

# Menambahkan jalan diantara kedua kota secara terpisah
print('---------------Sebelum-----------------')
peta_jatim.tambahkanJalan("Surabaya", "Sidoarjo")
peta_jatim.tambahkanJalan("Surabaya", "Tuban")
peta_jatim.tambahkanJalan("Surabaya", "Bojonegoro")
peta_jatim.tambahkanJalan("Surabaya", "Nganjuk")
peta_jatim.tambahkanJalan("Nagano", "Kanazawa")
peta_jatim.tambahkanJalan("Sidoarjo", "Probolinggo")
peta_jatim.tambahkanJalan("Sidoarjo", "Malang")
peta_jatim.tambahkanJalan("Sidoarjo", "Nganjuk")
peta_jatim.tambahkanJalan("Sidoarjo", "Bojonegoro")
peta_jatim.tambahkanJalan("Blitar", "Malang")
peta_jatim.tambahkanJalan("Blitar", "Ponorogo")
peta_jatim.tambahkanJalan("Blitar", "Nganjuk")
peta_jatim.tambahkanJalan("Nganjuk", "Ngawi")
peta_jatim.tambahkanJalan("Nganjuk", "Ponorogo")
peta_jatim.tambahkanJalan("Nganjuk", "Bojonegoro")
peta_jatim.tambahkanJalan("Nganjuk", "Probolinggo")
peta_jatim.tambahkanJalan("Ngawi", "Bojonegoro")
peta_jatim.tambahkanJalan("Ngawi", "Ponorogo")
peta_jatim.tambahkanJalan("Ngawi", "Tuban")

# Menghapus kota yang akan dihilangkan
peta_jatim.printPeta()
print('-----------------Sesudah---------------------')
peta_jatim.hapusKota("Surabaya")
peta_jatim.printPeta()