from timeit import default_timer as timer

print('Kullanım: "_recursive(cetvel uzunluğu, çizgi sayısı)"')
print('Kullanım: "_iterative(cetvel uzunluğu, çizgi sayısı)"')
###############################################

def ruler(k):
    pow = 1
    while ((2*k) % (2**pow)) == 0:
        pow += 1
    return pow-1
def _iterative(cm, cizgi): 
  start=timer()
  print('-' * cizgi, cm, end='\n')
  for y in range(cm, 0, -1):
    for x in range(1, (2**(cizgi - 1))):
      result=ruler(x)
      end=timer()
      passing_time=round((end-start),5)
      print('-' * result, " " * 30, "Geçen Süre: ",passing_time, end='\n')
    print('-' * cizgi, y - 1, end='\n')    
###############################################
def _recursive(cm, cizgi):
  _cizgi(cizgi, cm, 1)
  _ic(cizgi - 1)
  if (cm - 1) == 0:
    _cizgi(cizgi, 0, 1)
  else:  
   _recursive(cm - 1, cizgi)
   
def _ic(uzunluk):
  if uzunluk > 0:      
        _ic(uzunluk - 1)
        _cizgi(uzunluk, 0, 0)
        _ic(uzunluk - 1)        
        
def _cizgi(cizgi, sayi, ayar):
  print('-' * cizgi, end='')
  if sayi == 0:
    if ayar != 0:      
      print(" {}".format(sayi), end='\n')
    else:
      print(end='\n')     
    return
  else:
    if ayar != 0:
      print(" {}".format(sayi),end='\n')  
    else:
      print(end='\n')         
##############################################