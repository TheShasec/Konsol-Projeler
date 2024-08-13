kelime = input("palindrom kontrolu yapan uygulamaya hos geldiniz lutfen bir kelime girin ")
def palindromKontroluYapan(kelime):
  if kelime[::-1]==kelime:
    print("Bu kelime palindrom")
  else:
    print("Bu kelime palindrom degil")
palindromKontroluYapan(kelime)