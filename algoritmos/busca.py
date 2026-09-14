def buscar_ordem_por_codigo(ordens, codigo):
    for i in range(len(ordens)):
        if ordens[i].codigo == codigo:
            return i

    return -1