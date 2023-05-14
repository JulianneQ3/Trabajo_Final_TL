#Importación de paquetes

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath

def grafica_carta_plasticidad():

  #INGRESAR LOS VALORES DEL LIMITE LIQUIDO E INDICE DE PLASTICIDAD DEL SUELO

  limite_liquido= float(input("Ingrese el limite liquido: "))         
  indice_plasticidad=float(input("Ingrese el indice de plasticidad: "))
  
  #Definiendo los valores de x y y
  
  x = np.array([0,100])       
  y = np.array([0,100])
  
  #ECUACION DE LA LINEA A
  linea_A=0.73*(x-20)       
  
  #ECUACION DE LA LINEA U   
  linea_u=0.9*(x-8)           
  
  #VALORES PARA GRAFICAR LA LINEA A    
  #linea A                                
  linea_A_x= [20,100]
  linea_A_y= [0,58.4]
  
  #VALORES PARA GRAFICAR LA LINEA B
  #linea B                               
  linea_B_x= [50,50]
  linea_B_y= [0,60]
  
  #VALORES PARA GRAFICAR LA LINEA U
  #linea U                              
  linea_U_x= [8,75]
  linea_U_y= [0,60.3]
  
  #linea inferior        
  linea_baja_pi_x= [12.44,26]
  linea_baja_pi_y= [4,4]
  
  #linea superior       
  linea_baja_ps_x= [15.78,30]
  linea_baja_ps_y= [7,7]
  
  # Tamaño de grafica
  plt.figure(figsize=(8,8))
  
  # Graficar lineas
  plt.plot(linea_A_x, linea_A_y, label = "Línea A",color="purple")      #LINEA A
  plt.plot(linea_B_x, linea_B_y, color="red")                           #SEPARACION ZONA ALTA Y BAJA PLASTICIDAD
  plt.plot(linea_U_x, linea_U_y, label = "Línea U",color="blue",linestyle=":")   #LINEA U
  
  plt.plot(linea_baja_pi_x, linea_baja_pi_y, color="gray")             #ZONA CL-ML
  plt.plot(linea_baja_ps_x, linea_baja_ps_y, color="gray")             #ZONA CL-ML
  
  plt.title("CARTA DE PLASTICIDAD",fontsize=12)                   #TITULO DE LA GRAFICA
  plt.xlabel("Límite líquido LL (%)",fontsize=10)                 #ETIQUETA EJE X
  plt.ylabel("Indice de plasticidad IP (%)",fontsize=10)          #ETIQUETA EJE Y

  plt.vlines(limite_liquido,0,60,'k','--')
  plt.hlines(indice_plasticidad,0,100,'k','--')
  
  #Graficar etiquetas

  region_MH = np.array([[50,0], [50,22], [100,58], [100,0]])                 #REGION MH
  region_ML = np.array([[25.5,4], [12.4,4], [8,0], [20,0], [50,0], [50,22]]) #REGION ML
  region_CH = np.array([[50,22], [100,58], [100,60], [75,60], [50,38]])      #REGION CH
  region_CL_ML = np.array([[29.5,7], [15.7,7], [12.4,4], [25.5,4]])          #REGION CL-ML
  region_CL = np.array([[15.7,7], [29.5,7], [50,22], [50,38]])               #REGION CL

  #Graficar regiones

  path_MH = mpath.Path(region_MH)
  path_CH = mpath.Path(region_CH)
  path_CL = mpath.Path(region_CL)
  path_CL_ML = mpath.Path(region_CL_ML)
  path_ML = mpath.Path(region_ML)
  
  #UBICACION DEL PUNTO EN LA CARTA DE PLASTICIDAD

  point = np.array([limite_liquido,indice_plasticidad])

  #SE IDENTIFICA EN QUE REGION SE ENCUENTRA EL PUNTO

  if path_MH.contains_point(point):
      print('El punto se encuentra en la zona MH')
  elif path_CH.contains_point(point):
      print('El punto se encuentra en la zona CH')
  elif path_CL.contains_point(point):
      print('El punto se encuentra en la zona CL')
  elif path_CL_ML.contains_point(point):
      print('El punto se encuentra en la zona CL-ML')
  elif path_ML.contains_point(point):
      print('El punto se encuentra en la zona ML')
  else:
      print('El punto no se encuentra en la carta de plasticidad')

  
  plt.annotate('Linea A', (90,50),rotation=48) # Etiqueta de la linea A
  plt.annotate('Linea U', (60,45),rotation=52) # Etiqueta de la linea U
  plt.annotate('CL-ML', (17,5))   # Etiqueta de la zona CL-ML
  plt.annotate('MH', (80,20))     # Etiqueta de la zona MH
  plt.annotate('CL', (30,15))     # Etiqueta de la zona CL
  plt.annotate('CH', (62,40))     # Etiqueta de la zona CH
  plt.annotate('ML', (35,5))      # Etiqueta de la zona ML
  plt.annotate('NO EXISTE', (15,35))  # Etiqueta de la zona que NO EXISTE
  
  #ESTETICA
  
  a=[50,50,100,100]
  b=[0,22,58,0]
  plt.fill(a,b,'pink')
  c=[25.5,12.4,8,20,50,50]
  d=[4,4,0,0,0,22]
  plt.fill(c,d,'lightblue')
  e=[50,100,100,75,50]
  f=[22,58,60,60,38]
  plt.fill(e,f,'lightgreen')
  g=[29.5,15.7,12.4,25.5]
  h=[7,7,4,4]
  plt.fill(g,h,'bisque')
  i=[15.7,29.5,50,50]
  j=[7,7,22,38]
  plt.fill(i,j,'orchid')
  
  #CUADRICULA
  plt.grid(linestyle="-")
  plt.legend()
  plt.scatter(limite_liquido,indice_plasticidad)
  plt.show()