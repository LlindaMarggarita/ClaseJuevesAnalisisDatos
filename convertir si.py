import pandas as pd

#crear el Dataframe

data ={
  "Nombre":["Ana","Luis",None],
"Edad":[23,34,None],
  "Ciudad":["Bogota","Medellin",None]
}

#En este segmento por medio de la clase Dataframe llamandola con pandas(pd)convertir
dataConvertidaADataFrame = pd.DataFrame(data)

print(dataConvertidaADataFrame["Nombre"])

print(dataConvertidaADataFrame)

edades =[]

edades = dataConvertidaADataFrame["Edad"]

print("Estas son las personas registradas que pueden votar") 

for edad in edades:
  if edad>18:
     print(f'las edades de las personas que se pueden votar(edad)')

#esta funcion me permiteacceder a los datos del dataframe por medio de la posicion
print (dataConvertidaADataFrame.iloc[0])

#esta funcion me permite acceder a los datos por columnas
print (dataConvertidaADataFrame.loc[:,["Nombre","Ciudad"]])

print ("filtro personamayores de edad")
filtroMayores = dataConvertidaADataFrame[dataConvertidaADataFrame["Edad"]>18]
print (filtroMayores)

filtroPersonasEnBogota = dataConvertidaADataFrame [dataConvertidaADataFrame["Ciudad"]=="Bogota"]
print (filtroPersonasEnBogota)

filtroPersonasEnBogota = dataConvertidaADataFrame [dataConvertidaADataFrame["Ciudad"]!="Bogota"]
print (dataConvertidaADataFrame )

filtroPersonasNotBogota = dataConvertidaADataFrame [dataConvertidaADataFrame["Ciudad"]=="Bogota"]
print (filtroPersonasEnBogota)

dataConvertidaADataFrame['edades con Iva']= dataConvertidaADataFrame['Edad'] *0.19
print(dataConvertidaADataFrame)
print (dataConvertidaADataFrame.isnull())
print ("cantidad de valores nulos: ")
print (dataConvertidaADataFrame.isnull().sum())

print("para tener encuentaque Sogamoso no esta en esta encuesta")
dataConvertidaADataFrame ['Ciudad'] = dataConvertidaADataFrame ['Ciudad'].fillna("Sogamoso")
print (dataConvertidaADataFrame )

dataConvertidaADataFrame ['Edad'] = dataConvertidaADataFrame ['Edad'].fillna(dataConvertidaADataFrame['Edad'].mean())
print (dataConvertidaADataFrame)

dataConvertidaADataFrame = dataConvertidaADataFrame.drop(columns ="Ciudad")
print("los ganadores para esta encuesta")
dataConvertidaADataFrame = dataConvertidaADataFrame.rename(columns = {'edadesconIva':'edadesmodificadas'}) 
print(dataConvertidaADataFrame)



