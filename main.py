# main.py — importa módulos conforme são mergeados na main
def menu():
    print("=== Calculadora GCS ===\n")
    try:
        from calc_basico import somar, subtrair, multiplicar, dividir
        print("Módulo Básico carregado.")
        print("  2 + 3 =", somar(2, 3))
    except ImportError:
        print("Módulo Básico ainda não disponível.")


    try:
        from calc_potencia import potencia, raiz_quadrada
        print("Módulo Potência carregado.")
        print("  2^10 =", potencia(2, 10))
    except ImportError:
        print("Módulo Potência ainda não disponível.")


    try:
        from calc_conversao import celsius_para_fahrenheit, km_para_milhas, kg_para_libras
        print("Módulo Conversão carregado.")
        print("  10 Graus Celsius =", celsius_para_fahrenheit(10)
    except ImportError:
        print("Módulo Conversão ainda não disponível.")


    try:
        from calc_estatistica import media, mediana, desvio_padrao
        print("Módulo Estatística carregado.")
        print("  Média de 3, 4, e 5 =", media([3, 4, 5]))
    except ImportError:
        print("Módulo Estatística ainda não disponível.")


    try:
        from calc_percentual import percentual, acrescimo, desconto
        print("Módulo Percentual carregado.")
        print("  10 é", percentual(10, 25), " de 25 =")
    except ImportError:
        print("Módulo Percentual ainda não disponível.")

if __name__ == "__main__":
    menu()

