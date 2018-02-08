import pandas as pnds


ufo = pnds.read_table('http://bit.ly/uforeports',sep=',')
print(ufo.head())
print("################## CITY ##################")
print(ufo['City'])
print("################# State ###################")
print(ufo['state'])
