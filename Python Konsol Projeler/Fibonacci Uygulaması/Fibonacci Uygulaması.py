sayi = int(input("Fibonacci uygulamasina hos geldiniz lutfen bir sayi girin "))
def FibonacciUygulamasi(sayi):
  fibonacciList = []
  a = 0
  b=1
  while len(fibonacciList)<sayi:
    fibonacciList.append(a)
    a,b=b,a+b
  print(fibonacciList)
FibonacciUygulamasi(sayi)