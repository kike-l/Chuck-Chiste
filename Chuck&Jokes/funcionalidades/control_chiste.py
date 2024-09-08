import  json 
import requests



def chukJoke():
    s="""\n..HELLO!. & wellcome human humanaaaaaaaaaaan.......
    you just happend to reach chuck land.."""
   
    print(s) 
    flagCh = True
    #global data
    while flagCh:
        try: 
            url = 'https://api.chucknorris.io/jokes/random'
            response = requests.get(url)
            data = json.loads(response.text)
              
        except FileNotFoundError:
            print('\nSe produjo un error el chiste no llego')
            flagCh = False
        else:
            print(data)
            flagCh=False
    return data