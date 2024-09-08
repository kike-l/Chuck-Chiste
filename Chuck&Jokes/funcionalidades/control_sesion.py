import json
import numpy as np 
from time import *
from pathlib import Path
from funcionalidades.control_voz import *
from funcionalidades.control_certificados import *

 

def resultSesion(userDic):
    """Realiza los calculos para determinar el resultado de la sesion 
    y generar informe txt o pdf de la sesion calculado sobre los valores
    expresados por los numpy arrays 
    array1=votoChiste--->[de -3 a 3 x nChistes] 
    array2=valorSesion-->[+ o - x nocurrencias_valorPromedio]
           ----->obtenido: promedio valorSesion determina signo valores array
           ----->SI 1 array==-n1 <-----> SI 0 array==+n0
    array3=valorChiste-->[de 0 a 1 (float 9 decimals) x nChistes]
    calculo numpy == array1**array2/array3
    homogeneizacion de valores:
    si valor=>5 :: valor = 5
    si valor=<4.9 || valor=>0 :: valor = 0
    si valor=<-0.1 || valor=<-5 :: valor = -5
    """
    rArchUser=Path(userDic.get("rArchUser"))
    with rArchUser.open(mode='r',encoding='utf-8') as urDic:
           user=json.load(urDic) 
           pL=user["sesiones"]
           sesion=pL[-1]
           print(sesion)
           arr_vChist=sesion["valorChiste"]
           arr_vChist=np.array(arr_vChist)
           arr_Voto=sesion["votoChiste"]
           arr_Voto=np.array(arr_Voto)
           nCh=sesion["Njokes"]
           
           print(nCh)
           if nCh==None or nCh<3:
              s="""  La sesion no puede ser valorada correctamenete 
              se debe votar un total de 3 chistes  """
              e="""  It is necessary to cast at least 3 votes for us to 
              be able to create a profile, please stay a bit longer next time
              ta ra  or cheer e oo """
              print(s)
              habla(s)
              speak(e)
           else:   
              arr_vSes=sesion["valorsesion"]
              print(len(arr_vSes))
              avSes=sum(arr_vSes)/len(arr_vSes)
              arr_vSes=np.array(arr_vSes)
              print('valores de array valor sesion y average de valor sesion',arr_vSes,avSes)
              if avSes<=0.5:
                     arr_vSes=np.ones(len(arr_vSes))
                     print(arr_vSes)
              elif avSes>=0.5:
                     arr_vSes=np.ones(len(arr_vSes))
                     np.place(arr_vSes,arr_vSes==1,[-1])
                     print(arr_vSes)

              arr_resultado_sesion=arr_vChist**arr_vSes*arr_Voto
              sesion["resultado_sesion"]=list(arr_resultado_sesion)
              pL[-1]=sesion
              user["sesiones"]=pL
              with rArchUser.open(mode='w',encoding='utf-8') as userjson: 
                     json.dump(user,userjson,indent=1,sort_keys=1)
              print('valores de los array de analis de datos',
                    arr_resultado_sesion,'|--->Resultado Sesion',
                    arr_vChist,'|-->Valores dados a los chistes',
                    arr_vSes,'|--->Valores dados a la sesion',
                    arr_Voto,'|--->Votos a los chistes') 
           certificados(userDic)
           exit
    
           
           
    
    
  