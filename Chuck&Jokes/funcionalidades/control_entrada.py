import json
from time import *
from pathlib import Path
from funcionalidades.control_voz import speak, speakChiste, habla
from funcionalidades.control_chiste import chukJoke
from funcionalidades.control_valor_chistes import valor_chiste
from funcionalidades.control_sesion import resultSesion




def entradaVoto(userDic):
    """ Control de entrada de dastos a dicts.
    (archivos json) votos, valor chiste y sesion """
    def entradaUser():
        """Abre archivo e Inserta datos en dict user""" 
        n = 1
        with rAUser.open(encoding='utf-8') as userjson:
            user = json.load(userjson)
            lsesiones=user["sesiones"] 
            sesion=lsesiones[-1]
            sesion["votoChiste"].append(voto)
            sesion["valorsesion"].append(vChisteInt)
            sesion["valorChiste"].append(vChisteFloat)
            #Primer chiste de la sesion
            if sesion["Njokes"]==None:
                sesion["Njokes"]=n
            #No primer chiste de la sesion
            else:
                n=sesion["Njokes"]
                sesion["Njokes"]=n+1
            user["sesiones"]=lsesiones
            with rAUser.open(mode='w',encoding='utf-8') as userjson:
                json.dump(user,userjson,indent=2,sort_keys=1)
    def entradaSesionChiste():
        """Abre archivo y incorpora datos
        a diccionario sesion chistes """
        n = 1
        with rCS.open(encoding='utf-8') as sesionesChistes:
            sesionC= json.load(sesionesChistes)
            lSChist= sesionC["chistes"]
            sChiste=lSChist[-1]
            
            #Primer chiste de la sesion
            if sChiste["nchiste"]==None:
                sChiste["nchiste"]=n
                sChiste["votoChiste"]=voto
                sChiste["valorsesion"]=vChisteInt
                sChiste["valorChiste"]=vChisteFloat
                sChiste["chiste"]=chiste
            #No primer chiste de la sesion
            else:
                n=sChiste["nchiste"]
                sChiste["nchiste"]=n+1
                sChiste["votoChiste"]=voto
                sChiste["valorsesion"]=vChisteInt
                sChiste["valorChiste"]=vChisteFloat
                sChiste["chiste"]=chiste
            lSChist.append(sChiste)
            sesionC["chistes"]=lSChist
            with rCS.open(mode='w',encoding='utf-8') as sesionesChistes:
                json.dump(sesionC,sesionesChistes,indent=2,sort_keys=1)
    def entradaDB():
        """Abre y inserta datos en archivo
        base datos general chistes"""
        print("Entradas a base de datos")
        n=1
        with rDB.open(encoding='utf-8') as BDgeneral:
            baseDatos= json.load(BDgeneral)
            print('Comprobando si chiste existe en base datos cliente')
            #Comprobamos si el chiste ya existe en base de datos
            
            for dic in baseDatos: 
                for k,v in dic.items():
                    if k==dic["datachiste"]["value"] and v==chiste:
                        print(f"este es el chiste ...{chiste} que ya existe en la base de datos")
                        if not dic["votos_Total"][rdB]==None:
                            n=dic["numvisto"]
                            dic["numvisto"]=n+1
                            v_T=[]
                            v_T.append(dic["votos_Total"][rdB])
                            dic["votos_Total"][rdB]=v_T
                            print('Chiste repetido!!!! Modificando dict para retener lista valores voto')
                            break

                        else:
                            dic["votos_Total"][rdB]=voto
                            n=dic["numvisto"]
                            dic["numvisto"]=n+1
                            break
                           
            else:
                print("""El chiste no existe en la base de datos
                      y ya existe el diccionario base para 
                      incorporar el chiste""")
                #Si el chiste no existe en la base de datos            
                ultCh=baseDatos[-1]
                if ultCh["datachiste"]["categories"]==None:
                    ultCh["datachiste"]["categories"]=catChiste
                    ultCh["datachiste"]["created_at"]=created
                    ultCh["datachiste"]["valorChiste"]=vChisteFloat
                    ultCh["datachiste"]["value"]=chiste
                    ultCh["votos_Total"][rdB]=voto
                    ultCh["numvisto"]=n
                else:
                #Si el chiste no existe en base de datos 
                # pero no existe el dic base para incorporar el chiste
                    ultCh= {   
                            "datachiste":{ 
                                'categories': catChiste,
                                'created_at':created,
                                "valorChiste": [vChisteFloat],  
                                'value': str(chiste)},
                            "numvisto":n,
                            "votos_Total":{
                                "unaStar":None, 
                                "dosStar":None, 
                                "tresStar":None, 
                                "noStar":None }
                                } 
                    ultCh["votos_Total"][rdB]=voto
                    baseDatos.append(ultCh)
            with rDB.open(mode='w',encoding='utf-8') as BDgeneral:
                json.dump(baseDatos,BDgeneral,indent=2,sort_keys=1)
                           
    print("llego a  modulo control entradas ")
    #Adquirimos los path a los archivos de datos json 
    rAUser=Path(userDic["rArchUser"])
    print(rAUser)
    rDB=Path(userDic["rDBC"])
    print(rDB)
    rCS=Path(userDic["rchistesS"])
    print(rCS) 
    #
    fCV=True
    while fCV:
        n=1 #CONTADOR
        dataChiste=chukJoke()
        dB_chiste=dataChiste
        del dB_chiste['url']
        del dB_chiste['id']
        del dB_chiste['icon_url']
        chiste = dB_chiste['value']
        created = dB_chiste["created_at"]
        vChisteFloat, vChisteInt=valor_chiste(chiste)
        print(f""" Valores de:
              chiste:-->{vChisteFloat}
              sesion chistes:-->{vChisteInt}
              """)
        # NORMALIZADO VALORES CHISTES FLOAT a valores str
        if vChisteFloat==0:
            catChiste="Neutro"
            
        elif vChisteFloat<=0.5:
            catChiste="Picante"
            
        elif vChisteFloat>=0.5:
            catChiste="Irrespetuoso"
            
        elif vChisteFloat==1:
            catChiste="Ofensivo" 
         
        try:
            #vozDVal(chiste)
            speakChiste(chiste)
            print(chiste)
            voto = input('Indique su voto con [*]\n\t\t tres [***]>---{es mejor que}---< un [*]\n\t O no para  votar con [0]\nEntre salir para ir al menu\n\t').lower()
            voto.strip()
            voto == '*' or voto == '**' or voto == '***' or voto == 'no' or voto=='salir'
        except ValueError:
            print("""La entrada voto solo puede ser:
                  no --> para no voto 
                  o *  
                  o ** 
                  o *** 
                  o salir--> para terminar la sesion """)
        else:
            if voto==' ' or voto=='' or not voto:
                    print("debe entrar un voto o salir ")
            fV=True
            while fV:
                match voto:
                    case '*':
                        voto= 1
                        rdB= "unaStar"
                        entradaUser()
                        entradaSesionChiste()
                        entradaDB()
                        fV=False
                        
                    case '**':
                        if catChiste=="Ofensivo" or catChiste=="Irrespetuoso":
                            voto= -2
                            rdB="dosStar"
                            
                        else:
                            voto= 2
                            rdB="dosStar"
                            
                        entradaUser()
                        entradaSesionChiste()
                        entradaDB()
                        fV=False
                            
                    case '***':
                        if catChiste=="Ofensivo"or catChiste=="Irrespetuoso":
                            voto= -3
                            rdB="tresStar"
                            
                        else:
                            voto= 3
                            rdB="tresStar"
                            
                        entradaUser()
                        entradaSesionChiste()
                        entradaDB()
                        fV=False
                            
                    case 'no':
                        if catChiste=="Ofensivo":
                            voto= 3
                            rdB="noStar"
                            
                        elif catChiste=="Irrespetuoso":
                            voto= 3
                            rdB="noStar"
                                
                        elif catChiste=="Neutro":
                            voto= -1
                            rdB="noStar"
                            
                        else:
                            voto= 0
                            rdB="noStar"
                            
                        entradaUser()
                        entradaSesionChiste()
                        entradaDB()
                        fV=False
                    case 'salir':
                        print('Saliendo del programa')
                        #llamar a creador informe y añadir datos que falten a datauser_
                        endS=ctime()
                        with rAUser.open(encoding='utf-8') as userjson:
                            user = json.load(userjson)
                            lsesiones=user["sesiones"] 
                            sesion=lsesiones[-1]
                            sesion["TimeFin"]=endS
                            lsesiones[-1]=sesion
                            user["sesiones"]=lsesiones
                            with rAUser.open(mode='w',encoding='utf-8') as userjson:
                                json.dump(user,userjson,indent=1,sort_keys=1)
                        resultSesion(userDic) 
                        fV=False
                        fCV=False
                        exit
                    case '':
                        print( " Malisima entrada debe entrar su voto en modo  *   **   ***  no")
                        fV=False    
                            
                    case _:
                        print( " Malaisima entrada saliendo del programa")
                        fV=False
                        fCV=False
                        exit


                    
    
    
    
            
            
                
                
                
                 
                
            
            
                    
        
    
    
    
  