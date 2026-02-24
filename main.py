import json


class Tarefa:

    def __init__(self, nome, importancia, concluida=False):
        self.nome = nome
        self.importancia = importancia
        self.concluida = concluida

    def concluir(self):
        self.concluida = True

    def editar(self, novo_nome=None, nova_importancia=None):
        if novo_nome is not None:
            self.nome = novo_nome
        if nova_importancia is not None:
            self.importancia = nova_importancia

    def to_dict(self):
        return {
            "Nome": self.nome,
            "Importancia": self.importancia,
            "Concluida": self.concluida
        }

    @staticmethod
    def from_dict(dados):
        return Tarefa(
            nome=dados["Nome"],
            importancia=dados["Importancia"],
            concluida=dados["Concluida"]
        )


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


def menu():
    print("\n===== MENU =====")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Editar tarefa")
    print("0 - Sair")


def executar_opcao(gerenciador, opcao):

    if opcao == "1":
        nome = input("Nome da tarefa: ")

        while True:
            try:
                importancia = int(input("Nível de importância (1 a 5): "))
                break
            except ValueError:
                print("Digite apenas números.")

        if gerenciador.criar_tarefa(nome, importancia):
            print("Tarefa criada com sucesso!")
        else:
            print("Importância inválida.")

    elif opcao == "2":
        lista = gerenciador.listar_tarefas()

        if not lista:
            print("Nenhuma tarefa disponível.")
        else:
            for i, tarefa in enumerate(lista, start=1):
                status = "✔" if tarefa.concluida else "✘"
                print(f"\nTarefa {i}")
                print("Nome:", tarefa.nome)
                print("Status:", status)
                print("Importância:", tarefa.importancia)

    elif opcao == "3":
        lista = gerenciador.listar_tarefas()

        if not lista:
            print("Nenhuma tarefa disponível.")
            return True

        for i, tarefa in enumerate(lista, start=1):
            print(i, "-", tarefa.nome)

        try:
            numero = int(input("Digite o número da tarefa: "))
            if gerenciador.concluir_tarefa(numero - 1):
                print("Tarefa concluída!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite apenas números.")

    elif opcao == "4":
        lista = gerenciador.listar_tarefas()

        if not lista:
            print("Nenhuma tarefa disponível.")
            return True

        for i, tarefa in enumerate(lista, start=1):
            print(i, "-", tarefa.nome)

        try:
            numero = int(input("Digite o número da tarefa: "))
            removida = gerenciador.remover_tarefa(numero - 1)

            if removida:
                print("Tarefa removida:", removida.nome)
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite apenas números.")

    elif opcao == "5":
        lista = gerenciador.listar_tarefas()

        if not lista:
            print("Nenhuma tarefa disponível.")
            return True

        for i, tarefa in enumerate(lista, start=1):
            print(i, "-", tarefa.nome)

        try:
            numero = int(input("Digite o número da tarefa: "))
            indice = numero - 1

            if 0 <= indice < len(lista):

                print("\n1 - Editar nome")
                print("2 - Editar importância")
                escolha = input("Escolha: ")

                if escolha == "1":
                    novo_nome = input("Novo nome: ")
                    if gerenciador.editar_tarefa(indice, novo_nome=novo_nome):
                        print("Nome atualizado!")
                    else:
                        print("Erro ao atualizar.")

                elif escolha == "2":
                    while True:
                        try:
                            nova_importancia = int(input("Nova importância (1 a 5): "))
                            break
                        except ValueError:
                            print("Digite apenas números.")

                    if gerenciador.editar_tarefa(indice, nova_importancia=nova_importancia):
                        print("Importância atualizada!")
                    else:
                        print("Importância inválida.")

                else:
                    print("Opção inválida.")

            else:
                print("Número inválido.")

        except ValueError:
            print("Digite apenas números.")

    elif opcao == "0":
        print("Saindo...")
        return False

    else:
        print("Opção inválida.")

    return True


if __name__ == "__main__":

    gerenciador = GerenciadorDeTarefas()

    while True:
        menu()
        opcao = input("Escolha: ")

        if not executar_opcao(gerenciador, opcao):
            break