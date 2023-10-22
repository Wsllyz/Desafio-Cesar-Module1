class Estudante:
    def __init__(self, nome, aidi, notas=[]):
        self.nome = nome
        self.aidi = aidi
        self.notas = notas

    def __repr__(self):
        print(self.nome, self.aidi, self.notas)

listaEstudantes = []
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
            aidi = input("digite o ID do estudante: ")
            notas = input("digite as notas do estudante (separadas por vírgula): ")
            estudante = Estudante(nome, aidi, notas.split(","))
            listaEstudantes.append(estudante)
            
        case "2":
            print(listaEstudantes)
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            break
