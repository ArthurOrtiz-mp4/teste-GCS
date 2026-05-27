# calc_estatistica.py

# Módulo D - Operações Estatísticas

# Autor: Ivan Francisco Santos da Silva

# Branch: feature/modulo-estatistica

import math

def media(valores: list):
    """ Retorna a média dos valores informados. """

    if not isinstance(valores, list): # Verifica se o valor informado é uma lista
        raise ValueError("Informe uma lista válida!") # Se não for, lança um ValueError
    
    if len(valores) == 0: # Verifica se a lista está vazia
        raise ValueError("A lista não pode estar vazia!") # Se estiver, lança um ValueError

    return sum(valores) / len(valores)

def mediana(valores: list):
    """ Retorna a mediana dos valores informados. """

    if not isinstance(valores, list): # Verifica se o valor informado é uma lista
        raise ValueError("Informe uma lista válida!") # Se não for, lança um ValueError
    
    if len(valores) == 0: # Verifica se a lista está vazia
        raise ValueError("A lista não pode estar vazia!") # Se estiver, lança um ValueError
    
    valores_ordenados = sorted(valores)
    tamanho = len(valores_ordenados)
    meio = tamanho // 2

    if tamanho % 2 == 0: # Verifica se a quantidade de elementos é par
        return (valores_ordenados[meio - 1] + valores_ordenados[meio]) / 2
    
    return valores_ordenados[meio]

def desvio_padrao(valores: list):
    """ Retorna o desvio padrão dos valores informados. """

    if not isinstance(valores, list): # Verifica se o valor informado é uma lista
        raise ValueError("Informe uma lista válida!") # Se não for, lança um ValueError
    
    if len(valores) == 0: # Verifica se a lista está vazia
        raise ValueError("A lista não pode estar vazia!") # Se estiver, lança um ValueError

    media_valores = media(valores)

    variancia = sum((valor - media_valores) ** 2 for valor in valores) / len(valores)

    return math.sqrt(variancia)