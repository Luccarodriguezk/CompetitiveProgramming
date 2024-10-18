def Dichotomic_search (Y , t ):
  if len( Y )==0 or Y [0] > t : return None
    a , b = 0 , len( Y ) # a <= i < b
  while b -a >1:
    c = ( a + b )//2
  if Y [ c ] <= t :
    a = c
  else:
    b = c
  return a
Y = sorted ( X )
for t in T :
  print ( Dichotomic_search(Y , t ))
