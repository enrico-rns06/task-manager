import json

tarefas = []

def salvar_tarefas():
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)


def carregar_tarefas():
    global tarefas
    try:
        with open("tarefas.json", "r") as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []

carregar_tarefas()

while True:
    print("\n===== MENU =====")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Editar tarefa")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome da tarefa: ")

        while True:
            try:
                importancia = int(input("Nível de importância (1 a 5): "))
                if 1 <= importancia <= 5:
                    break
                else:
                    print("Digite um número entre 1 e 5.")
            except ValueError:
                print("Digite apenas números.")

        tarefa = {
            "Nome": nome,
            "Concluida": False,
            "Importancia": importancia
        }

        tarefas.append(tarefa)
        salvar_tarefas()
        print("Tarefa criada com sucesso!")

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa disponível.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                status = "✔" if tarefa["Concluida"] else "✘"
                print(f"\nTarefa {i}")
                print("Nome:", tarefa["Nome"])
                print("Status:", status)
                print("Importância:", tarefa["Importancia"])

    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa disponível.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(i, "-", tarefa["Nome"])

            try:
                numero = int(input("Digite o número da tarefa: "))
                indice = numero - 1

                if 0 <= indice < len(tarefas):
                    tarefas[indice]["Concluida"] = True
                    salvar_tarefas()
                    print("Tarefa concluída!")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Digite apenas números.")

    elif opcao == "4":
        if not tarefas:
            print("Nenhuma tarefa disponível.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(i, "-", tarefa["Nome"])

            try:
                numero = int(input("Digite o número da tarefa: "))
                indice = numero - 1

                if 0 <= indice < len(tarefas):
                    removida = tarefas.pop(indice)
                    salvar_tarefas()
                    print("Tarefa removida:", removida["Nome"])
                else:
                    print("Número inválido.")
            except ValueError:
                print("Digite apenas números.")

    elif opcao == "5":
        if not tarefas:
            print("Nenhuma tarefa disponível.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(i, "-", tarefa["Nome"])

            try:
                numero = int(input("Digite o número da tarefa: "))
                indice = numero - 1

                if 0 <= indice < len(tarefas):

                    print("\n1 - Editar nome")
                    print("2 - Editar importância")
                    escolha = input("Escolha: ")

                    if escolha == "1":
                        novo_nome = input("Novo nome: ")
                        tarefas[indice]["Nome"] = novo_nome
                        salvar_tarefas()
                        print("Nome atualizado!")

                    elif escolha == "2":
                        while True:
                            try:
                                nova_importancia = int(input("Nova importância (1 a 5): "))
                                if 1 <= nova_importancia <= 5:
                                    tarefas[indice]["Importancia"] = nova_importancia
                                    salvar_tarefas()
                                    print("Importância atualizada!")
                                    break
                                else:
                                    print("Digite entre 1 e 5.")
                            except ValueError:
                                print("Digite apenas números.")
                    else:
                        print("Opção inválida.")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Digite apenas números.")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")