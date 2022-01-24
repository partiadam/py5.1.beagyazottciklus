'''
1. Feladat - Pocak
Készíts egy programot while ciklussal , amely a felhasználótól bekér egy páros számot, majd ennek megfelelően rajzol ki a képernyőre egy pocak szerű alakzatot az alábbiak szerint!

  Adj meg egy páros számot! 8
  
  O 
  O O 
  O O O 
  O O O O 
  O O O O 
  O O O 
  O O 
  O 
'''

darab_karakter = 1
sor = int(input("Kérem adjon meg egy számot: "))
x = 1
while x <= sor / 2:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    x = x + 1

f = 1
while f <= sor / 2:
    oszlop = 2
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter - 1
    f = f + 1 
