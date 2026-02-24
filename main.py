tarefas = []

executando = True

while executando:
    print("Menu")
    print("\n1 - Criar tarefa")
    print("2 - Listar tarefa")
    print("3 - Concluir tarefa:")
    print("4 - Remover tarefa")
    print("5 - Editar tarefa")
    print("0 - Sair")

    
    opcao = input()

    if opcao == "1":
        nome = str(input("Nome da tarefa: "))
        importancia = int(input("Nivel de importancia (1 a 5): "))
        
        tarefa ={
            "Nome": nome,
            "Concluida": False,
            "Importancia": importancia
        }
        tarefas.append(tarefa)

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa disponível.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"\nTarefa {i}:")
                print("Nome:", tarefa["Nome"])
                print("Concluída:", tarefa["Concluida"])
                print("Importância:", tarefa["Importancia"])
        
    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa disponível.")
        else:  
            for i, tarefa in enumerate(tarefas, start=1):
                print(i, "-", tarefa["Nome"])
            numero = int(input("Digite o número da tarefa que deseja concluir: "))
            indice = numero - 1
            if 0 <= indice < len(tarefas):
                tarefas[indice]["Concluida"] = True
                print("Tarefa concluída.")
            else:
                print("Número inválido.")
    elif opcao == "4":
        if not tarefas:
            print("Nenhuma tarefa disponível.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(i, "-", tarefa["Nome"])
            numero = int(input("Digite o número da tarefa que deseja remover: "))
            indice = numero -1

            if 0 <= indice < len(tarefas):
                removida = tarefas.pop(indice)
                print("Tarefa removida:", removida["Nome"])
            else:
                print("Número inválido.")
    elif opcao == "5":
        if not tarefas:
            print("Nenhuma tarefa disponível.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(i, "-", tarefa["Nome"])
            numero = int(input("Digite o número da tarefa que deseja editar: "))
            indice = numero -1

            if 0 <= indice < len(tarefas):
                editada = tarefas
                print("Tarefa editada:", editada["Nome"])
            else:
                print("Número inválido.")
                
                if len(tarefas) == True:
                    print("\n1 - Editar nome")
                    print("2 - Editar impôrtancia")
                    tarefas[1]["Nome"] = "Novo nome"
                    tarefas[1]["Importancia"] = 5
    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opcao inválida.")

executando = True

while executando:
    print("Menu")
    print("\n1 - Criar tarefa")
    print("2 - Listar tarefa")
    print("3 - Concluir tarefa:")
    print("4 - Remover tarefa")
    print("5 - Editar tarefa")
    print("0 - Sair")

    
    opcao = input()

    if opcao == "1":
        nome = str(input("Nome da tarefa: "))
        
        while True:
            importancia= int(input("Nivel de importância:"))

            if 1<= importancia <= 5:
                break
            else:
                print("Digite um numero de 1 a 5.")
        
        tarefa ={
            "Nome": nome,
            "Concluida": False,
            "Importancia": importancia
        }
        tarefas.append(tarefa)

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa disponível.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"\nTarefa {i}:")
                print("Nome:", tarefa["Nome"])
                print("Concluída:", tarefa["Concluida"])
                print("Importância:", tarefa["Importancia"])
        
    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa disponível.")
        else:  
            for i, tarefa in enumerate(tarefas, start=1):
                print(i, "-", tarefa["Nome"])
            numero = int(input("Digite o número da tarefa que deseja concluir: "))
            indice = numero - 1
            if 0 <= indice < len(tarefas):
                tarefas[indice]["Concluida"] = True
                print("Tarefa concluída.")
            else:
                print("Número inválido.")
    elif opcao == "4":
        if not tarefas:
            print("Nenhuma tarefa disponível.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(i, "-", tarefa["Nome"])
            numero = int(input("Digite o número da tarefa que deseja remover: "))
            indice = numero -1

            if 0 <= indice < len(tarefas):
                removida = tarefas.pop(indice)
                print("Tarefa removida:", removida["Nome"])
            else:
                print("Número inválido.")
    elif opcao == "5":
        if not tarefas:
            print("Nenhuma tarefa disponível.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(i, "-", tarefa["Nome"])
            
            numero = int(input("Digite o número da tarefa que deseja editar: "))
            indice = numero -1

            if 0 <= indice < len(tarefas):
                print("\n1 - Editar nome")
                print("2 - Editar impôrtancia")
                
                escolha = input("EScolha: ")

                if escolha == "1":
                    novo_nome = input("Novo nome: ")
                    tarefa[indice]["Nome"] = novo_nome
                    print("Nome atualizado.")
                elif escolha == "2":
                    nova_importancia = int(input("Nova importância: "))
                    tarefa[indice]["Importancia"] = nova_importancia
                    print("Importância atualizada.")
                else:
                    print("Número inválido.")
    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opcao inválida.")