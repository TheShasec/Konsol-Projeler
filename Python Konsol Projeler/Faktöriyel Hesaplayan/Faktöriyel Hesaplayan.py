sayi = int(input("Faktoryel hesaplayan uygulamaya hos geldiniz lutfen bir sayi girin "))
def faktoryelHesaplayan(sayi):
  sonuc = 1
  for i in range(1,sayi+1):
    sonuc=sonuc*i
  print(sonuc)
faktoryelHesaplayan(sayi)