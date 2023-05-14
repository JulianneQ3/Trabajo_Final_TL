#Importación de paquetes

from prompt_toolkit.shortcuts.dialogs import D

from .valoresentrada import *
from .cartaplasticidad import *
from .granulometria import *

def clasificacion():
  #ESTRUCTURA DEL CODIGO

  print("DATOS DE ENTRADA")
  print("--------------------------------")

  #DATOS DE ENTRADA

  porcentaje_pasa_T4= pasa[0]
  porcentaje_pasa_T200= pasa[7]

  cu=x1_coord/x3_coord
  cc=(x2_coord**2)/(x1_coord*x3_coord)

  #CÁLCULO DE LOS ÍNDICES

  limite_liquido= (cu-17)/(0.5-0.1*cc)
  indice_plasticidad= limite_liquido-20

  print("Porcentaje pasa tamiz Nº 4 :"+ str(porcentaje_pasa_T4))
  print("Porcentaje pasa tamiz Nº 200 :"+ str(porcentaje_pasa_T200))
  print("Cu:  " +str(cu))
  print("Cc:  " +str(cc))
  print("Límite líquido:  " +str(limite_liquido))
  print("Indice de plasticidad:  " +str(indice_plasticidad))


  #ESTRUCTURA

  linea_A=0.73*(limite_liquido-20)           #ECUACION DE LA LINEA A
  linea_u=0.9*(limite_liquido-8)             #ECUACION DE LA LINEA U

  def particulas ():                              #SE DEFINEN LOS FINOS CUANDO LO QUE PASA POR EL TAMIZ 200 ES MENOR AL 50% 
    if porcentaje_pasa_T200 < 50:

      def gruesos():                              #SE DEFINEN LOS GRUESOS CUANDO LO QUE PASA POR EL TAMIZ N4 ES MENOR AL 50%
        if porcentaje_pasa_T4 <50:

          def gravas():                           #SE DEFINEN LAS GRAVAS CUANDO LO QUE PASA POR EL TAMIZ 200 ES MENOR AL 5%
            if porcentaje_pasa_T200 <5:

              def gravas_limpias():               #SI ES UNA GRAVA LIMPIA BIEN GRADUADA CUMPLE LAS DOS CONDICIONES CU Y CC
                if cu >=4 and 1 <= cc <=3:
                  print("OUTPUT")
                  print("----------------------")
                  print("Gw: Grava bien gradada ")
                else:
                  print("OUTPUT")
                  print("------------------------")
                  print("Gp: Grava pobremente gradada")
            
              gravas_limpias()
        
            elif porcentaje_pasa_T200 >12:        #SE DEFINEN LAS GRAVAS CUANDO LO QUE PASA POR EL TAMIZ 200 ES MAYOR AL 12%
              
              def gravas_con_finos():
                if indice_plasticidad < linea_A :           #SE DEFINE SI LA GRAVA TIENE LIMOS O ARCILLAS
                  print("OUTPUT")
                  print("-----------------------------")
                  print("GM: Grava limosa ")
                elif indice_plasticidad > linea_A :
                  print("OUTPUT")
                  print("-----------------------------")
                  print("GC: Grava arcillosa ")
                else:
                  print("Error en clasificar gravas con finos: No cumple el IP")
              gravas_con_finos()


            elif 5< porcentaje_pasa_T200 <12:                           #SE DEFINEN LAS GRAVAS CUANDO LO QUE PASA POR EL TAMIZ 200 ESTÁ ENTRE EL 5 Y EL 12% (DOBLE SÍMBOLO)
            

              def gravas_limpias_con_finos():
                if cu >=4 and 1 <= cc <=3 and indice_plasticidad < linea_A :
                  print("OUTPUT")
                  print("-----------------------------")
                  print("GW-GM: Grava bien graduada con limo")
                elif cu >=4 and 1 <= cc <=3 and indice_plasticidad > linea_A :
                  print("OUTPUT")
                  print("----------------------------")
                  print("GW-GC: Grava bien graduada con arcilla")
                elif cu <4 and (1> cc or cc >3) and indice_plasticidad < linea_A :
                  print("OUTPUT")
                  print("-----------------------------")
                  print("GP-GM: Grava mal graduada con limo")
                elif cu <4 and (1> cc or cc >3) and indice_plasticidad > linea_A :
                  print("OUTPUT")
                  print("-----------------------------")
                  print("GP-GC: Grava mal graduada con arcilla")
                else:
                  print("Error en gravas limpias con finos")
                
              gravas_limpias_con_finos()
          
            else:
              print("Error en clasificacion de gravas")
          gravas()

        elif porcentaje_pasa_T4 >50:                                 #SE DEFINEN LAS ARENAS CUANDO LO QUE PASA POR EL TAMIZ N4 ES MAYOR AL 50%
          def arenas():
            if porcentaje_pasa_T200 <5:
              def arenas_limpias():                                    
                if cu >=6 and 1<= cc <=3:
                  print("OUTPUT")
                  print("-----------------------------")
                  print("SW: Arena bien graduada ")
                else:
                  print("OUTPUT")
                  print("-----------------------------")
                  print("SP: Arena mal graduada ")
              arenas_limpias()

            elif porcentaje_pasa_T200 >12:

              def arenas_con_finos():
                if indice_plasticidad < linea_A :
                  print("OUTPUT")
                  print("-----------------------------")
                  print("SM: Arena limosa ")
                elif indice_plasticidad > linea_A :
                  print("OUTPUT")
                  print("-----------------------------")
                  print("SC: Arena arcillosa")
                else:
                  print("Error en arenas con finos")
              arenas_con_finos()

            elif 5< porcentaje_pasa_T200 <12:
              def arenas_limpias_y_con_finos():
                if cu >=6 and 1<= cc <=3 and indice_plasticidad < linea_A:
                  print("OUTPUT")
                  print("-----------------------------")
                  print("SW-SM: Arena bien graduada con limo")
                elif cu >=6 and 1<= cc <=3 and indice_plasticidad >linea_A:
                  print("OUTPUT")
                  print("-----------------------------")
                  print("SW-SC: Arena bien graduada con arcilla")
                elif cu <6 and (1 > cc or cc >3) and indice_plasticidad <linea_A:
                  print("OUTPUT")
                  print("-----------------------------")
                  print("SP-SM: Arena mal graduada con limo")
                elif cu <6 and (1 > cc or cc >3) and indice_plasticidad >linea_A:
                  print("OUTPUT")
                  print("-----------------------------")
                  print("SP-SC: Arena mal graduada con arcilla")
                else:
                  print("Error en arenas limpias y con finos")
              arenas_limpias_y_con_finos()
            else:
              print("Error en clasificación de arenas")
          arenas()
        else:
          print("Error en clasificación entre grava y arena")
      gruesos()

    elif  50<= porcentaje_pasa_T200 <=100 :                                   #SE DEFINE LA CARTA DE PLASTICIDAD CUANDO EL PORCENTAJE PASA ES MAYOR O IGUAL AL 50%

      def suelo_fino():
        if limite_liquido <50:
          def baja_plasticidad():
            if linea_A < indice_plasticidad < linea_u :
              print("OUTPUT")
              print("-----------------------------")
              print("CL: Arcilla de baja plasticidad")
            elif 0< limite_liquido< 50 and indice_plasticidad>linea_A:
              if 0< indice_plasticidad < linea_A:
                print("OUTPUT")
                print("-----------------------------")
                print("ML: Limo de baja plasticidad")
            elif 7< limite_liquido <30 and 4< indice_plasticidad <7:
              print("-----------------------")
              print("CL-ML: Arcilla y limo de baja plasticidad")
            else:
              print("Suelo indefinido")
          baja_plasticidad()

        elif limite_liquido >50:
          def alta_plasticidad():
            if linea_A < indice_plasticidad < linea_u :
              print("OUTPUT")
              print("-----------------------------")
              print("CH: Arcilla de alta plasticidad")
            elif 50< limite_liquido <100:
              if 0< indice_plasticidad < linea_A:
                print("-----------------------------")
                print("MH: Limo de alta plasticidad")
            else:
              print("Error en limite liquido mayor que 50")

          alta_plasticidad()
        else:
          print("Error suelo fino")
      suelo_fino()
      grafica_carta_plasticidad()                                                 #SE GRAFICA LA CARTA DE PLASTICIDAD SI EL SUELO ES FINO
    else:
      print("Error: El porcentaje pasa del tamiz 200 debe estar entre 0 y 100")

  particulas ()