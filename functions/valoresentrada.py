#Importación de paquetes

import pandas as pd
import numpy as np

#Se crea la tabla de pesos retenidos obtenidos en laboratorio.

tamiz = np.array([
    'Nº 4',
    'Nº 10',
    'Nº 20',
    'Nº 30',
    'Nº 40',
    'Nº 60',
    'Nº 140',
    'Nº 200',
    'Fondo'
])

abertura =np.array([
    4.75, #DIAMETRO DEL TAMIZ Nº 4 EN mm
    2.0, #DIAMETRO DEL TAMIZ Nº 10" EN mm
    0.85, #DIAMETRO DEL TAMIZ Nº 20" EN mm
    0.6, #DIAMETRO DEL TAMIZ Nº 30" EN mm
    0.425, #DIAMETRO DEL TAMIZ Nº 40" EN mm
    0.25, #DIAMETRO DEL TAMIZ Nº 60" EN mm
    0.106, #DIAMETRO DEL TAMIZ Nº 140" EN mm
    0.075, #DIAMETRO DEL TAMIZ Nº 200" EN mm
    0,   #FONDO
])

#SE INGRESAN LOS DATOS DEL LABORATORIO

retenido =np.array([
    12, 
    23,
    22,
    35,
    26,
    11,
    20,
    15,
    200,  
])


#-----------------------------------------

retenido1=np.array(retenido)

peso_total=sum(retenido)             #SE SUMA EL TOTAL DEL PESO RETENIDO PARA CALCULAR EL % PASA


porcentaje_retenido=[]             
acumulado=[]
pasa=[]

for i in range(0,9):                              
  reteni2=(retenido[i]/peso_total)*100
  porcentaje_retenido.append(reteni2)
acumulado.append(porcentaje_retenido[0])
pasa.append(100-porcentaje_retenido[0])

for i in range(1,9):                                
  acumulado2=acumulado[i-1]+porcentaje_retenido[i]
  acumulado.append(acumulado2)
  pasa2=100-acumulado[i]                             
  pasa.append(pasa2)


Estructura = pd.DataFrame({
    'Tamiz':tamiz,
    'Abertura (mm)' : abertura,
    'Retenido (g)' : retenido,
    '% Retenido' : porcentaje_retenido,
    '% Acumulado' : acumulado,
    "% Pasa" : pasa
   
})

print(Estructura)