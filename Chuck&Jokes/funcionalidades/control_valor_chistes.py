import joblib 
from profanity_check import predict, predict_prob

def valor_chiste(chiste):
    """Valora los chistes adquiridos"""
    print(chiste,type(chiste))
    badWords=['kill','blood','rape','fuck','idiot','cunt','pussy',]
    valorChiste = float(predict_prob([chiste]))
    valorChiste2= int(predict([chiste]))
    print(valorChiste,valorChiste2 ,chiste)
    return (valorChiste,valorChiste2)