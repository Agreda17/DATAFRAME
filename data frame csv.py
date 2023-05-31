import pandas as pd
datos = pd.read_csv('D: /Mariluz/Documents/C_machine_learnig/videos/iris.data', header = None) 
datos.to_csv('D:/Mariluz/Documents/C_machine_learnig/videos/iris2.data') 
print(datos.head())



#pd.read_csv()
#pd.read_excel()
#to_csv()
#to_excel()
