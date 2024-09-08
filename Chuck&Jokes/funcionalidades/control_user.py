import json
from time import *
from pathlib import Path
from funcionalidades.control_rutas import ruta
from funcionalidades.control_entrada import *
from funcionalidades.control_archivos import arquitecto
from funcionalidades.control_voz import *

def user():
    """Comprueva si el cliente exite, 
    de ser así crea nuevas sesiones 
    en los archivos json user y json chistes sesion
    SI NO crea los diccionarios base y lanza arquitecto que crearArchUser 
    los directorios y archivos parArchUser alojar los datos"""
    
    fU=True
    while fU:
        l= """  Introduzca su nombre y dos apellidos
                Primero un nombre luego los apellidos
                O salir para regresar a menu principal\t""" 
        habla(l)               
        cliente=input(l).lower().strip()
        print(cliente)
        
        if cliente == 'salir':
            print(""" Regresando a menu principal""")
            fU=False
            exit
        
        elif not cliente:
            print("""Debe introducir un nombre y dos apellidos""")
        
        else:
            cliente=cliente.split(' ')
            print(cliente)
            if len(cliente)!= 3:
                print("""  Mala entrada...
                        El campo no puede quedar vacio
                        Necesario un nombre y dos apellidos """)   
            else:
                c=(f"""  Bienvenido Mr{str(cliente)}...
                        encantada de conocerle.
                        Vamos a comprovar si usted existe en nuestra
                        base de datos""")
                habla(c)
                inTime = ctime()
                print(len(cliente), cliente)
                nombre, apellido1, apellido2 = cliente[0:3]    
                rVoz=Path(f"{ruta()}/DBChuck_audio")
                dirUser=Path(f'{ruta()}/ChuckNData')
                rArchUser=Path(f'{dirUser}/dataUser_{nombre}_{apellido1[:3]}_{apellido2[:3]}.json')
                rchistesS= Path(f"{dirUser}/chistesSesion_{nombre}_{apellido1[:3]}_{apellido2[:3]}.json")
                rDBchiste= Path(f"{ruta()}/DBChuckChistes")
                rDBC=Path(f"{rDBchiste}/chisteChuck_BD_{nombre}_{apellido1[:3]}_{apellido2[:3]}.json")
                print(dirUser,rArchUser)
     
                # SI LOS ARCHIVOS CLIENTE EXISTEN:--->
                # CREAMOS E INCORPOrArchUserMOS NUEVA SESION CON MISMO USER
                # A ARCHIVO USER--data
                
                if rArchUser.exists() and rchistesS.exists() and rDBC.exists():
                    c=(f""" Bien venido { str(cliente)}...
                            que alegría verle de nuevo...
                            Vamos a crear una nueva sesión para usted """)
                    habla(c)
                    
                    with rArchUser.open(mode='r',encoding='utf-8') as archivojson:
                        userDic=json.load(archivojson)
                        #MODIFICAMOS LOS DATOS USER COMUNES A TODAS LAS SESIONES DEL USER
                        nSes=userDic["totalSesiones"]
                        userDic["totalSesiones"]= nSes+1
                        nSes=userDic["totalSesiones"]
                        print(len(userDic["sesiones"]))
                        lSesiones=userDic["sesiones"]
                        print(lSesiones,end='\n')
                        
                        #CREAMOS Y INCORPOrArchUserMOS LA NUEVA SESION CON VALORES BASE A LISTA DE SESIONES
                        #DE USUARIO
                        sesion={
                                "resultado_sesion":None,
                                "valorsesion":[],
                                "Nsesion":nSes,
                                "TimeStart":inTime,
                                "TimeFin":None,
                                "Njokes":None,
                                "votoChiste":[],
                                "valorChiste":[]
                                }    
                        lSesiones.append(sesion)
                        userDic["sesiones"]=lSesiones
                        print(userDic["sesiones"],len(userDic["sesiones"]))
                        with rArchUser.open(mode="w",encoding='utf-8') as archivojson:
                            json.dump(userDic,archivojson,indent=2, sort_keys=1)
                            
                    #--->CREAMOS E INCORPOrArchUserMOS NUEVO DICT A ARCHIVO BASE DE DATOS CHISTES
                    
                    with rDBC.open(encoding='utf-8') as dBChistes:
                        lDicBD= json.load(dBChistes)
                        dicDB={   
                                "datachiste":{ 
                                    'categories': None,
                                    'created_at':None ,
                                    "valorChiste": [],  
                                    'value': str()},
                                "numvisto":None,
                                "votos_Total":{
                                    "unaStar":None, 
                                    "dosStar":None, 
                                    "tresStar":None, 
                                    "noStar":None }
                                    }
                        lDicBD.append(dicDB)
                        with rDBC.open(mode="w",encoding='utf-8') as dBChistes:
                            json.dump(lDicBD,dBChistes,indent=2, sort_keys=1) 
                    # con valores Base modificados parArchUser nueva sesion
                    # Y LANZAMOS AL USUARIO A ENTrArchUserDA VOTOS       
                            
                    with rchistesS.open(encoding='utf-8') as sesionChistes:
                        sesChist=json.load(sesionChistes)
                        lses=sesChist["chistes"]
                        diclses=lses[-1]
                        nSes=diclses["sesion"]
                        sesionC= {
                                    "sesion":nSes +1,
                                    "nchiste":None,
                                    "votoChiste":int(), 
                                    "valorsesion":None,
                                    "valorChiste":None,
                                    "chiste":str() }
                        lses.append(sesionC)
                        sesChist["chistes"]=lses
                        with rchistesS.open(mode='w', encoding='utf-8') as sesionChistes:
                            json.dump(sesChist,sesionChistes,indent=2,sort_keys=1)    
                         
                        fU=False
                        entradaVoto(userDic)
                        exit
                #Creamos e incorporArchUsermos dict (sin datos) de chiste parArchUser base de datos
                
                        
                # SI LOS DIRECTORIOS DE CHISTES SESION(datauser) Y DB(basedatos_chiste) NO EXISTEN 
                
                # SE CREAN LOS DICCIONARIOS  Y SE LLAMA A ARQUITECTO PArArchUser CREAR ARCHIVOS Y DIRECTORIOS 
                else:
                    print(""" Cliente inexistente: 
                            \nCreando diccionarios y redirigiendo 
                            a arquitecto""")
                    nSes= 1  
                    #CREAMOS DICCIONARIO  Y RUTAS: 
                    # A DIR Y ARCHIVO DBgenerArchUserl de chistes visualizados INCORPOrArchUserMOS A DICT USER
                    userDic = { 
                                "nombre":nombre,
                                "apellido1": apellido1,
                                "apellido2": apellido2,
                                "creacionUser": inTime,
                                "totalSesiones": nSes,
                                "rDBchiste":str(rDBchiste),
                                "rVoz":str(rVoz),
                                "rDBC":str(rDBC),
                                "rchistesS":str(rchistesS),
                                "rDirUser":str(dirUser),
                                "rArchUser":str(rArchUser),
                                "sesiones": [{
                                        "resultado_sesion":None, #LLamada a funcion valorArchUserr O LISTA DE ARGUMENTOS PArArchUser LA LLAMADA A CREACION DE INFORME
                                        "valorsesion":[],
                                        "Nsesion":nSes,
                                        "TimeStart":inTime,
                                        "TimeFin":None,
                                        "Njokes":None,
                                        "votoChiste":[],
                                        "valorChiste":[] 
                                        }]
                                } 

                    chistesS= {
                               "chistes":[ {
                                        "sesion":nSes,
                                        "nchiste":None,
                                        "votoChiste":int(), 
                                        "valorsesion":None,
                                        "valorChiste":None,
                                        "chiste":str()
                                        }
                                        ]
                                 }
                            
                                
                    chuc_N_ChisteDB=[ {   
                                        "datachiste":{ 
                                            'categories': None,
                                            'created_at':None ,
                                            "valorChiste": [],  
                                            'value': str()},
                                        "numvisto":None,
                                        "votos_Total":{
                                            "unaStar":None, 
                                            "dosStar":None, 
                                            "tresStar":None, 
                                            "noStar":None }
                                            }
                                        ]
                                    
                    fU= False
                    arquitecto(userDic,chuc_N_ChisteDB,chistesS)
                    
                    exit
                    
        

            
           