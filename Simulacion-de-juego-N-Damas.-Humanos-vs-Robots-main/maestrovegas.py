import pygame,sys
from pygame.locals import *
from random import randint
from numpy import *
from collections import *
from tkinter import *
from tkinter import ttk, font
import getpass
#from interfaz import*


##contara las damas puestas validas antes de cada reinicio
##el reinicio se da cuando no hay posiciones validas para alguna dama
n_damas_arrayss = []
#ins_interfaz= Interfaz
tiempo_por_movimiento = 0

class Logica :       
      
            
      def valida_horizontal_vertical ( fila,columna,itere):
            
              #window=pygame.display.set_mode ((fila*40,fila*40))
              global n_damas_arrayss
              global tiempo_por_movimiento
              
              n_damas_array = n_damas_arrayss
              
            
              fila,columna = int(fila), int(columna)
              #llenar tablero de ceros
              matriz= zeros ( ( fila,columna ))            
            
              #esta lista sera la principa
              #el indice de la lista indicara la columna de la matriz
              #el valor en el indice indicara la fila de la matriz
              #esto para ahorro de iteracion recorriendo o llenando matricez
              #entonces los valores que sean igual a la variable fila , no tendran una dama puesta.
              guarde_damas= [fila]*fila         
              
              itere= True
              
              #esta indicara cuando debemos reiniciar el algoritmo.
              #si todos sus valores son iguales a 1, se reiniciara el algoritmo
              #funcionara iniciandolo, entonces si se comprueba que un valor no es valido...
              #...colocar una dama, pondra un 1 . si en ninguno fue valido, todo estara lleno de unos.
              valide = [0]*fila

              #dira la fila donde ya hay una dama,para que nunca vuelva a colocar una ahi
              #indice igual a las damas en total
              #valores del indice indican el numero de la fila donde esta puesto 
              ocupado= [0]*fila

              #esta variable se usara como contador para saber las damas que estan puestas...
              #...antes del reinicio              
              n_damas= 0
              
              
              i=0
              while (i <  columna)and (itere):
                
                #genera numero aleatorio
                donde=randint(0,fila-1)
                
                #  ***** descomentar para observar los cambio detalladamente ***** #

                #print("salio este numero ->", donde)
                #print ("como va guardando damas -->>>  " , guarde_damas)
                #print("dama ocupada en columna" , ocupado )
                #print ("si todo es un entonces reinicio ->", valide)

                # **********************************************************************#


                #condicion que valida que no se pueda poner nunca en una misma fila o columna
                
                if ( ocupado [donde]==0 )and (valide[donde] == 0 ):
                     
                     valide[donde] = 1
                     ii=0
                     matriz [donde] [i] =5
                     guarde_damas[i]=donde
                     ocupado[donde]=1

                     # *******************    observar los cambios  de como pone las reinas en la matriz 
                     # descomentar para observar cambios en la matriz paso por paso :3 y la giu

                     
                     #**************************       VER ***********************************************
                     #                                                                                                                   *
                     #print (matriz )                                                                                                #
                     #ins_interfaz.muestre_tablero(fila,guarde_damas,window,True)                          #
                     #                                                                                                                    *
                     #************************************************************************************

                     # este llama a validar diagonales, si retorna que fue valido (True )
                     #entonces entra a el if                     
                     if (Logica.valide_diagonales (matriz,guarde_damas)):
                       
                       #imprime si fue valido donde quedo puesta la reina
                       #print ("valida")
                       i+=1
                       n_damas +=1
                       tiempo_por_movimiento+=1 
                       
                       valide = [0]*fila
                     else :
                       
                       #print ("no se puede " )    
                       matriz [donde] [i] = 0
                       valide[donde] = 1                       
                       ocupado[donde]=0
                else :
                        
                        valide[donde] = 1
                        
                
                #validacion para comprobar si valide ya esta llena de unos, si sí ,
                #hace llamado a si mismo para reiniciar proceso                  
                if ( valide.count(1) == fila ):
                    
                    #print ("*********REINICIO POR NINGUNA POSICION VALIDA***********")
                    n_damas_array.append ( n_damas)
                    #print (" numero de damas que puso antes de reinicio ->>>>  " , n_damas_array )
                    return Logica.valida_horizontal_vertical ( fila,columna,itere)


                
                # para validar que si ya estan todas las damas puestas,termine todo....
                #....y retorne las damas como quedaron guardadas para posteriormente pintarlas  

                
                if (ocupado.count(1) == fila ):
                    
                    #print (matriz )                  
                    #print (" numero de damas que puso en total  antes de los reinicios ->>>>  " , n_damas_array )
                    #print ("numero de reinicios (que lo intento y no pudo) = " , len (n_damas_array) )
                    
                    itere = False
                    
                    
                    return tiempo_por_movimiento
                    break
              
                                  
                
                  
            
              
      
            
            
            
            
              #return guarde_damas 
      ##________________________________________
          
      def valide_diagonales (matriz,guarde_damas):
        
        fila = len (matriz)
        
        
        valido = True
        
        j=0
        

        
        
        
        while ( j < fila ):
            i = guarde_damas[j]

            if ( i != fila ) : 
            
                  #angulo 45°
                  k= j 
                  
                  while (k < fila-1 )and ( i > 0 ):
                     
                      i-=1
                      k+=1
                      
                      
                      if (matriz[i][k]==0 ) :
                        valido = True
                        
                      
                      else:
                        valido= False
                        #print ("falso por 45° ")
                        return False
                        break
                      
                  #angulo 315°
                  
                  k=j
                  i= guarde_damas[j]
                  
                  while (k < fila-1 )and ( i < fila-1 ):
                      
                      
                      i+=1
                      k+=1
                      
                      
                      if (matriz[i][k]==0 ) :
                        valido = True
                        
                      
                      else:
                        valido= False
                        #print ("falso por 315° ")
                        return False
                        break
                
                
            j+=1
              
          
          
        
        
        return True
        
      ##________________________________________     
            ##_____________________fin metodo __________________________________##


#si quiere que se muestre solo el procedimiento de la matriz (sin GIU )-> descomentar todos ...
#... los print  comentados en el codigo ...
# esto mostrara con mucha precicion cada paso del algoritmo.

#descomentar esto para hacer uso de esta clase unicamente e ingresar N manualmente
#ins_logica = Logica
#ins_logica.valida_horizontal_vertical(15,15,True)

      

  


