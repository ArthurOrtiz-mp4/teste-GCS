# calc_conversao.py

# Módulo E - Operações de Conversão

# Autor: Amanda Ayumi Koga Kikuta

# Branch: feature/modulo-conversao

def celsius_para_fahrenheit(valor: float):
    """ Retorna a conversão do valor que está em celsius para fahrenheit. """

    if not isinstance(valor, (int, float)): # Verifica se o valor informado é numérico
        raise ValueError("Informe um valor válido!") # Se não for, lança um ValueError

    return valor * 1.8 + 32

def km_para_milhas(valor: float):
    """ Retorna a conversão do valor que está em quilômetros para milhas. """

    if not isinstance(valor, (int, float)): # Verifica se o valor informado é numérico
        raise ValueError("Informe um valor válido!") # Se não for, lança um ValueError
    
    return valor * 0.621371

def kg_para_libras(valor: float):
    """ Retorna a conversão do valor que está em quilogramas para libras. """

    if not isinstance(valor, (int, float)): # Verifica se o valor informado é numérico
        raise ValueError("Informe um valor válido!") # Se não for, lança um ValueError
    
    return valor * 2.2046