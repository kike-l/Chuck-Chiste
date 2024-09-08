import json
from pathlib import Path
from funcionalidades.control_voz import *
from funcionalidades.control_entrada import entradaVoto


def arquitecto(userDic,chuc_N_ChisteDB,chistesS):
    """ Crea la raquitectura de DIR y archivos
    Necesarios para el funcionamiento del programa """
    print(""" Arquitecto, se van a crear los direcctorios 
          y archivos necesarios """)
    #COMPROVAR SI LOS ARCHIVOS Y DIRECCTorio cliente EXISTEN

    rDirUser=Path(userDic.get("rDirUser"))
    rDBDir=Path(userDic.get("rDBchiste"))
    rVoz=Path(userDic.get("rVoz"))
    rDBC=Path(userDic.get("rDBC"))
    rArchUser=Path(userDic.get("rArchUser"))
    rchistesS=Path(userDic.get("rchistesS"))
    comprovar0=rVoz.exists()
    
    if comprovar0:
        pass
    
    else:
        print("Se creara el directorio para almacenar todos los chistes evaluados")
        rVoz.mkdir()
        
    comprovar1=rDirUser.exists()
    comprovar2=rchistesS.exists()
    comprovar3=rArchUser.exists()
    comprovar4=rDBDir.exists()
    comprovar5=rDBC.exists()
    
    print(comprovar1,comprovar2,comprovar3,comprovar4,comprovar5)
    
    #SI CLIENTE EXISTE ARQUITECTO NO HACE NADA YA QUE USER INCORPORO SESIONES NUEVAS
    if comprovar2 and comprovar3 and comprovar5:
        print(""" Cliente existente en base de datos
                se incorporan nuevas sesiones de usuario
                y chistes  """)
        entradaVoto(userDic)
        exit
    #SI LOS DIRECTORIOS NO EXISTEN = 1ºCLIENTE, SE CREA TODOS DIR + ARCH
    if comprovar1 == False and comprovar4 == False:
        l=(""" Primer Cliente en base de datos
               Se va a proceder a crear los directorios 
               y archivos necesarios """)
        print(l)
        #CREAMOS LOS ARCHIVOS Y DIRECCTORIOS DE CLIENTE NUEVO
        habla(l)
        rDirUser.mkdir()
        rDBDir.mkdir()
        rDBC.touch(exist_ok=False)
        rchistesS.touch(exist_ok=False)
        rArchUser.touch(exist_ok=False)
        
        # INCORPORAMOS DICTS con VALORES BASE A ARCHIVOS JSON
        with rArchUser.open(mode="w", ) as userJson:
            json.dump(userDic,userJson,indent=2,sort_keys=1)
        with open(rchistesS,mode="w") as userJson:
            json.dump(chistesS,userJson,indent=2,sort_keys=1)
        with open(rDBC,mode="w") as userJson:
            json.dump(chuc_N_ChisteDB,userJson,indent=2,sort_keys=1)
        print(""" Diccionarios con datos base
                 incorporados a archivos 
                 HURRA! """)
        entradaVoto(userDic)
        exit 
    # SI LOS DIRECTORIOS EXISTEN PERO CLIENTE NO 
    # CREAMOS LOS ARCHIVOS DEL CLIENTE Y INCORPORAMOS
    # DICCIONARIOS CON DATOS BASE 
    elif comprovar1 == True and comprovar4 == True and comprovar2 == False and comprovar3 == False  and comprovar5 == False:
        
        rDBC.touch(exist_ok=False)
        rchistesS.touch(exist_ok=False)
        rArchUser.touch(exist_ok=False)
        
        # INCORPORAMOS DICTS con VALORES BASE A ARCHIVOS JSON
        with open(rArchUser,mode="w") as userJson:
            json.dump(userDic,userJson,indent=2,sort_keys=1)
        with open(rchistesS,mode="w") as userJson:
            json.dump(chistesS,userJson,indent=2,sort_keys=1)
        with open(rDBC,mode="w") as userJson:
            json.dump(chuc_N_ChisteDB,userJson,indent=2,sort_keys=1)
        l=(""" Diccionarios con datos base
                 incorporados a archivos 
                 HURRA! """)
        print(l)
        habla(l)
        entradaVoto(userDic)
        exit 
           
    else:
        print(f""" Ocurrio un problema creando alguno de los directorios o archivos necesarios
               No se creo correctamente. Borre los archivos del cliente 
               e inicie el proceso de nuevo
               SALIENDO DEL PROGRAMA""")
        exit