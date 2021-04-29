


from numpy import *


tiempo_por_movimiento= 0
class deterministico :       
      
            
      def valida_horizontal_vertical ( fila,columna,itere):
              global tiempo_por_movimiento
              
              #window=pygame.display.set_mode ((fila*40,fila*40))
              fila,columna = int(fila), int(columna)
              #llenar tablero de ceros
              matriz= zeros ( ( fila,columna ))                        
              guarde_damas= [fila]*fila         
              ocupado= [0]*fila
              valide=[]
              n_damas= 0              
              i= 0                       
              incorrecto = 0
              correcto = 0
              
              while ( i  < columna )and (itere):
                
                          
                #  ***** descomentar para observar los cambio detalladamente ***** #

                #print ("como va guardando damas -->>>  " , guarde_damas)
                #print("dama ocupada en columna" , ocupado )
                
                # **********************************************************************#

              
                if ( ocupado [incorrecto]==0 ) and ( matriz [incorrecto] [i] == 0):              
                     
                     
                     matriz [correcto] [i] =5
                     guarde_damas[i]=correcto
                     
                     # *******************    observar los cambios  de como pone las reinas en la matriz                  
                     #**************************       VER ***********************************************
                     #                                                                                                                   *
                     #print (matriz )                                                                                                #
                     #                                                                                                                    *
                     #************************************************************************************

                     # este llama a validar diagonales, si retorna que fue valido (True )                     
                     if (deterministico.valide_diagonales (matriz,guarde_damas)):

                           ocupado[correcto]=1                                                 
                           i  +=1
                           tiempo_por_movimiento += 1
                           incorrecto = 0                           
                           correcto = 0 
                           valide.clear()
                           
                     else :

                       valide.append(1)
                       matriz [correcto] [i] = 3
                       ocupado[correcto]=0
                       correcto +=1
                       incorrecto += 1                      
                       
                else :                  
                        valide.append(1) 
                        matriz [incorrecto][i] = 3
                        incorrecto+=1
                        correcto+=1              
                                 
                if ( valide.count(1) == fila ):
                    
                    #print ("*********RETROCEDO UNA COLUMNA POR NINGUNA POSICION FACTIBLE***********")
                  
                    j=0
                    while ( j < fila ):
                    
                       matriz [j] [i] = 0
                       j+=1
                    matriz [guarde_damas[i-1]] [i-1] =3
                    valide.clear()                    
                    ocupado [guarde_damas[i-1]] = 0
                    i -=1
                    correcto= 0
                    incorrecto = 0
                                    
                # para validar que si ya estan todas las damas puestas,termine todo....
                #....y retorne las damas como quedaron guardadas para posteriormente pintarlas                
                if (ocupado.count(1) == fila ):
                    
                    #print (matriz )                  
                    #print (guarde_damas)
                                     
                    return tiempo_por_movimiento
                    break               
            
            
            
      ##_____________METODO DIAGONALES ___________________________
          
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
                      
                      
                      if (matriz[i][k]==0 )or (matriz[i][k]==3 ) :
                        valido = True
                        
                      
                      else:
                        valido= False
                        #print ("falso por 45° ")
                        return False
                        break
                      
                  
                  
                  k=j
                  i= guarde_damas[j]
                  
                  while (k < fila-1 )and ( i < fila-1 ):
                      
                      
                      i+=1
                      k+=1
                      
                      
                      if (matriz[i][k]==0 )or (matriz[i][k]==3 ) :
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
#ins_logica = Deterministicos
#ins_logica.valida_horizontal_vertical(15,15,True)

      

  


