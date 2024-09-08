import os



def ruta():
    """Crea la ruta hasta directorio principalChuck3
    Usamos como ruta base para crear directorios secundarios y archivos
    necesarios"""
    
    print("""\nEntro en control de ruta
          Generando ruta a directorio principal""")
  
    ruta_relativa = "." # Lugar donde se lanza funcion
    ruta_absoluta = os.path.abspath(ruta_relativa) #absolute path usamos os para obtener
    
    print(ruta_absoluta)
    print(ruta_relativa)
 
    return ruta_absoluta