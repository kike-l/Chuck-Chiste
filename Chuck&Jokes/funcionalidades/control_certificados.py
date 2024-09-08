import json
from pathlib import Path
from funcionalidades.control_voz import *

def certificados(userDic):
    """Aprueva y crea los certificados correspondientes 
    o por el contrario insta al usuario a intenatarlo de nevo"""
    
    def docTxt():
        """Aqui se generara y se guardara un informe en formato txt"""
        print(s)
        print(result)
        
        
    def docPdf():
        """Aqui se generara y se guardara un certificado de chuck en formato pdf"""
        print(s)
        print(result)
    print(" llego a emision de certificados ")
    rArchUser=Path(userDic.get("rArchUser"))
    with rArchUser.open(mode='r',encoding='utf-8') as urDic:
           user=json.load(urDic)
           uL=user["sesiones"]
           usr=uL[-1]
           arr_ResSes=usr["resultado_sesion"]
           result=0
           for n in arr_ResSes:
               if n>0:
                   result=result+n
               elif n<0:
                   result=result+n 
           
           if result>=1:
               s=(""" Congratulations you are a real chuck""")
               speak(s)
               docTxt()
               docPdf()
               exit
           
           elif 1>result>=0:
               s=(""" What a pitty you aren't ready for chuck
                  but you will, dont worry """)
               speak(s)
               docTxt()
               exit
           
           elif result<0:
               s=(""" Uff you have a problem, 
                  an angry person can not be a chuck, laugh over others pain
                  ain't cool man  seriously seek help """)
               speak(s)
               docTxt()
               exit 
    
   

 