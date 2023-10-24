listaEstudantes = {}

while True:
    print("Sistema de gerenciamento de registros de estudantes")
    print("---")
    print("1. Adicionar registro de estudante")
    print("2. Exibir registros de estudantes")
    print("3. Procurar por um estudante")
    print("4. Calcular média das notas")
    print("5. Salvar registros em arquivo")
    print("6. Carregar registros de arquivo")
    print("7. Sair")
    print("---")
    escolha = input("Digite sua escolha: ")

    match escolha:
        case "1":
            nome = input("digite o nome do estudante: ")
            notas = input("digite as notas do estudante (separadas por vírgula): ")
            listaEstudantes[len(listaEstudantes)] = [nome, notas.split(", ")]
            
        case "2":
            print(listaEstudantes)
        case "3":
            try:
                idEstudante = int(input("Digite o ID do estudante: "))
                print(listaEstudantes[idEstudante])
            except KeyError:
                print("ID inválido: Este estudante não existe.")
            except ValueError:
                print(f"ID inválido: apenas números inteiros são aceitos como ID.")
        case "4":
            try:
                acumulator = 0
                for x in listaEstudantes.values():
                    for y in x:
                        if y == list(y):
                            for z in y:
                                z = int(z)
                                acumulator += z
                print(f" A média é: {acumulator / len(listaEstudantes)}")
            except ZeroDivisionError:
                print("Não há nenhum estudante.")
        case "5":
            pass
        case "6":
            pass
        case "7":
            break
