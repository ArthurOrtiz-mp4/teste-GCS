
def percentual(valor, total):
    """Retorna quanto valor representa em % de total.
    Lança ValueError se total == 0."""
    if total == 0:
        raise ValueError("O total não pode ser zero.")
    return (valor / total) * 100


def acrescimo(valor, percentual):
    """Retorna o valor com acréscimo de x%.
    Lança ValueError se percentual < 0."""
    if percentual < 0:
        raise ValueError("O percentual de acréscimo não pode ser negativo.")
    return valor * (1 + percentual / 100)


def desconto(valor, percentual):
    """Retorna o valor com desconto de x%.
    Lança ValueError se percentual < 0 ou > 100."""
    if percentual < 0 or percentual > 100:
        raise ValueError("O percentual de desconto deve estar entre 0 e 100.")
    return valor * (1 - percentual / 100)