from funcionalidades.control_voz import speak, habla
from funcionalidades.control_user import user
from funcionalidades.control_sesion import resultSesion

def menu():
    """Menu de entrada a programa"""
    
    fM=True
    while fM:
        try:
            select = """  Realice una seleccion:
                                1- Entrar
                                2- Salir
                        """
            habla(select)
            select=int(input(select))
            1<=select<=2 
              
        except ValueError:
            print(""" La entrada debe ser numerica y 
                   exclusivamente 1 o 2 """)
        
        else:
            match select:
                case 1:
                    s=(""" Bienvenido al gran Chuck & chiste,
                          Un programa que determinará si eres un autentico chuck
                          de ser así y tras valorar algunos chistes recibiras 
                          tu certificado como miembro del selecto clan de Chuck.""")
                    habla(s)
                    speak(""" Dark thoughts inc. 
                          Gladlly presents...  Chuck & Jokes.  
                          We are happy to entretain.
                          And remember you son of a gun... 
                          Don't mess with Texas... 
                          or  Llimiana for that matter """)
                    user()
                    #Al salir de este proceso debemos llamar al modulo o clase que genera el directoro el archivo pdf y informe txt privado
                    # y el certificado para el cliente
                    #
                    
                    fM=False    
                case 2:
                    s=("""  Selecciono salir del programa.
                            Deseamos que la sesión le haya 
                            resultado entretenida.
                            Muchas gracias por participar """)
                    print(s)
                    habla(s)
                    fM=False
                    
    
    habla(""" Muchas gracias por visitarnos:
        nuestro mayor respeto y agradecimiento a las personas 
        que cearon y mantienen la api de chuck Norris.
        https://api.chucknorris.io/jokes/random
        \n\tUfff,  sorry\n\t\t  Have to..\t\n
        Por qué Chuck Norris no cuenta chistes?..
        Por que cuando lo hace alguien muere de risa""")
    
if __name__=='__main__':
    menu()