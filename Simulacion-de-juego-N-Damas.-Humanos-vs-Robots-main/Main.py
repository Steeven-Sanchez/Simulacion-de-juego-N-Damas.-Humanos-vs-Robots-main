# -*- coding: utf-8 -*-
#Instalar https://simpy.readthedocs.io/en/latest/simpy_intro/installation.html
#Ejemplos https://simpy.readthedocs.io/en/latest/examples/index.html
import random
import simpy
import numpy
from deterministico  import*
from maestrovegas import*
from time import time

#Datos de la simulación
SEMILLA = 40 #Semilla generador
CLIENTES = 0 #Vamos a simular 10 clientes
TIEMPO_TOTAL = 28800
#Variables desempeño
COLA = 0
MAX_COLA = 0
ESPERA_CLIENTES = numpy.array([])
valide = True
def llegada(env, numero, contador):
    
    global valide
    i=0 
    while valide :

        i+=1
        c = cliente(env, ' %02d' % i, contador)
        env.process(c)
        tiempo_llegada = random.uniform(10,30)
        yield env.timeout(tiempo_llegada) #Yield retorna un objeto iterable


        
ins_deterministico = deterministico
ins_vegas = Logica

def aux (n):
        
        tiempo_por_movimiento_robot =   ins_vegas.valida_horizontal_vertical (n,n,True)*5
           
        tiempo_por_movimiento_profesor = ins_deterministico.valida_horizontal_vertical (n,n,True)*5
        

        if (tiempo_por_movimiento_robot > tiempo_por_movimiento_profesor):
            return (tiempo_por_movimiento_robot*(-1))
        else : return tiempo_por_movimiento_profesor
    
def  seleccion_dama ():

    
    tamaño_tablero  = round(random.uniform(1, 7))
    #print ("que paso ?????  =  " , tamaño_tablero )

    if ( tamaño_tablero==1 ):
        tamaño= 4
    elif ( tamaño_tablero==2 ):
        tamaño= 5
    elif ( tamaño_tablero==3 ):
        tamaño= 6
    elif ( tamaño_tablero==4 ):
        tamaño= 8
    elif ( tamaño_tablero==5 ):
        tamaño= 10
    elif ( tamaño_tablero==6 ):
        tamaño= 12
    else:  tamaño= 15
    
    return tamaño

def tiempo_servicio  (n):
    tamaño_tablero  = n
    #print ("que paso ?????  =  " , tamaño_tablero )

    if ( tamaño_tablero==4 ):
        tiempo = aux (4)
    elif ( tamaño_tablero==5 ):
        tiempo = aux (5)
    elif ( tamaño_tablero==6 ):
        tiempo = aux (6)
    elif ( tamaño_tablero==8 ):
        tiempo = aux (8)
    elif ( tamaño_tablero==10 ):
        tiempo = aux (10)
    elif ( tamaño_tablero==12 ):
        tiempo = aux (12)
    else:  tiempo = aux (15)    

    return tiempo 
    
#print ( "eeeepa ->>>>    ", tiempo_servicio () )

gano="nadie aun :v"
profesor_gano= 0
robot_gano= 0.
tiempo_acumulado=0
        
def cliente(env, nombre, servidor):
    #El cliente llega y se va cuando es atendido
    llegada = env.now
    print('%7.2f'%(env.now)," Llega el Robot ", nombre)
    global COLA
    global MAX_COLA 
    global ESPERA_CLIENTES
    global profesor_gano
    global robot_gano
    global valide
    global tiempo_acumulado
    #Atendemos a los clientes (retorno del yield)
    #With ejecuta un iterador sin importar si hay excepciones o no
    with servidor.request() as req:
        
                    if (TIEMPO_TOTAL <  tiempo_acumulado ):
                        valide=False 
                    #Hacemos la espera hasta que sea atendido el cliente
                    COLA += 1
                    if COLA > MAX_COLA:
                            MAX_COLA = COLA
                    
                    #print("Tamaño cola", COLA)
                    results = yield req	
                    COLA = COLA - 1
                    espera = env.now - llegada
                    ESPERA_CLIENTES = numpy.append(ESPERA_CLIENTES, espera)
                    
                    seleccion_n = seleccion_dama ()
                    tiempo_atencion =tiempo_servicio(seleccion_n)
                    
                    if ( tiempo_atencion < 0):
                        gano= "Gano Profesor"
                        profesor_gano +=1 
                        tiempo_atencion = tiempo_atencion *(-1)#5 segundos por movimiento 
                        
                    else :
                        gano= "Gano Robot"
                        robot_gano+=1
                        tiempo_atencion = tiempo_atencion #5 segundos por movimiento 
 
                       
                    print('%7.2f'%(env.now), " El Robot ",nombre," espero: ",espera," min , jugo " , tiempo_atencion , " min y " ,gano, " con ", seleccion_n," damas." )
                    
                    
                    yield env.timeout(tiempo_atencion)

                    tiempo_acumulado = tiempo_acumulado + tiempo_atencion 
                    
                    print('%7.2f'%(env.now), " Sale Robot ",nombre)
    
                    
#Inicio de la simulación

print('Sala de cine')
random.seed(SEMILLA)
env = simpy.Environment()

#Inicio del proceso y ejecución
servidor = simpy.Resource(env, capacity=1)
env.process(llegada(env,CLIENTES, servidor))
env.run()

print("Cola máxima ",MAX_COLA)
print("Tiempo promedio de espera ",'%7.2f'%(numpy.mean(ESPERA_CLIENTES)))
print ("el profesor gano = ",profesor_gano," veces")
print ("el robot gano= ",robot_gano," veces")
print ("Ingreso $",profesor_gano*15," COP" )
print ("Egreso $",robot_gano*10," COP" )
if (profesor_gano*15 < robot_gano*10 ):
    print ( "Perdiste $" , (robot_gano*10)-(profesor_gano*15) ," COP")
else : print ( "Ganaste " , (profesor_gano*15)- (robot_gano*10)," COP" )     
print ( "TIEMPO ACUMULADO" , tiempo_acumulado )
