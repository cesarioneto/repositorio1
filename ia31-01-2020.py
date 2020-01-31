#oi
"""
import pandas as pd
df =pd.read_csv('nas.csv', sep=';', encoding = 'cp1252')

print( df.head()   )
print( df.count()  )
print( df.dtypes   )

print( df['NOME_REGIAO_UNIDADE'].value_counts() )
print (df)



-------------------------------------------------  PLOT--------------------------------
 



 -*- coding: utf-8 -*-

# Spyder Editor

# cesario 2019-06-27
# import pandas as pd
# import numpy as np

import matplotlib.pyplot as plt

narq = '  '

tab = [0]


narq = input('Narq-> ')

qtd = 1
 
arq = open (narq,'w')

qtd1 =input ('qtd-> ')


for cc in range (1,int(qtd1)) :
    print (str(cc))
    qtd2 =input ('qtd-> ')
    arq.writelines(( str(cc)+' '+ str(qtd2)+'\n') )
    
    
arq.close()

arq = open (narq,'r')

arw = [' ']
    
for cc in range(1,int(qtd1)) :
    arw = str( (arq.readline()) )
    print (arw[0])
    print   (( (arw(1) + arw(2) ))
  #  tab.append ( int( (arw(2) + arw(3) )))
tab = 7
   



# -----------------------------------------------------------------MACHINE LEARNING
# print(tab)
#  plt.plot(tab)
 #plt.show()

# print(tab)



#  grafiko 

# qtd =input ('qtd-> ')
# tab = [0] 


# for cc in range(0, int(qtd)):
#     print (cc)
    
#    valor =int(input('->'))
 #   tab.append(valor)
#----------------------------------------------pandas numpy

print ('run')
print (' ')



kmh = [10.20, 30, 40, 50]

mph3 = [x/1.46 for x in kmh]

print (mph3)


import numpy  as np

a = np.array ([(1, 2, 3), 
               (4, 5, 6),
               (7, 8, 9)])
    
for x in a:
    print(x)
    print(' ')
    
b = np.zeros((3,3))  # matriz zero

b = np.eye(4)

print (b)
"""


import pandas as pd
import numpy as  np


arq  = pd.read_csv('c:\intel\cesar\ia\wine.csv')

data = pd.DataFrame(arq)

print (data.head())
print (data.shape)
print (data['style'])




