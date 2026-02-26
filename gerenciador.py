import json
from models import Tarefa


class GerenciadorDeTarefas:

    def __init__(self):
        self.tarefas = []
        self.carregar()

    def criar_tarefa(self, nome, importancia):
        if not isinstance(importancia, int):
            return False
        if importancia < 1 or importancia > 5:
            return False

        tarefa = Tarefa(nome, importancia)
        self.tarefas.append(tarefa)
        self.salvar()
        return True

    def listar_tarefas(self):
        return self.tarefas

    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluir()
            self.salvar()
            return True
        return False

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            removida = self.tarefas.pop(indice)
            self.salvar()
            return removida
        return None

    def editar_tarefa(self, indice, novo_nome=None, nova_importancia=None):
        if 0 <= indice < len(self.tarefas):

            if nova_importancia is not None:
                if not isinstance(nova_importancia, int):
                    return False
                if nova_importancia < 1 or nova_importancia > 5:
                    return False

            self.tarefas[indice].editar(novo_nome, nova_importancia)
            self.salvar()
            return True

        return False

    def salvar(self):
        with open("tarefas.json", "w") as arquivo:
            json.dump([t.to_dict() for t in self.tarefas], arquivo, indent=4)

    def carregar(self):
        try:
            with open("tarefas.json", "r") as arquivo:
                dados = json.load(arquivo)
                self.tarefas = [Tarefa.from_dict(item) for item in dados]
        except FileNotFoundError:
            self.tarefas = []