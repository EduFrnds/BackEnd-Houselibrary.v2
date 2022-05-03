import re

#Validate arquivo

def phone_number_valid(phone_number):
    """check if the cell phone is valid(xx 9xxxx-xxxx)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, phone_number)
    return resposta

#def name_valid(name):
#    modelo_name = ''
#    resposta_name = re.findall(modelo_name, name)
#    return resposta_name