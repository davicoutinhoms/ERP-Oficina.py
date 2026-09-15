def ordenar_por_prioridade(ordens):
    copia = ordens.copy()
    n = len(copia)

    for i in range(n):
        for j in range(0, n - i - 1):

            if copia[j].prioridade < copia[j + 1].prioridade:
                temp = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = temp

    return copia

def ordenar_por_valor(ordens):
    copia = ordens.copy()
    n = len(copia)

    for i in range(n):
        for j in range(0, n - i - 1):

            if copia[j].valor_total > copia[j + 1].valor_total:
                temp = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = temp

    return copia

def ordenar_por_codigo(ordens):
    copia = ordens.copy()
    n = len(copia)

    for i in range(n):
        for j in range(0, n - i - 1):
            if copia[j].codigo > copia[j + 1].codigo:
                temp = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = temp

    return copia