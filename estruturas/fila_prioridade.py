class FilaPrioridade:
    def __init__(self):
        self.fila = []

    def inserir(self, ordem):
        self.fila.append(ordem)

    def esta_vazia(self):
        return len(self.fila) == 0

    def remover_maior_prioridade(self):
        if self.esta_vazia():
            return None

        indice_maior = 0

        for i in range(1, len(self.fila)):
            if self.fila[i].prioridade > self.fila[indice_maior].prioridade:
                indice_maior = i

        return self.fila.pop(indice_maior)

    def tamanho(self):
        return len(self.fila)

    def remover_por_codigo(self, codigo):
        for i in range(len(self.fila)):
            if self.fila[i].codigo == codigo:
                self.fila.pop(i)
                return True

        return False