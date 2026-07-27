import itertools

# Contador de IDs na memória
geraid = itertools.count(start=1).__next__

def cadastrar(nome):
    # Usa vírgula para separar os dados com segurança, mesmo com nome completo
    with open("salvadados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{geraid()},{nome},0.0\n")

def excluir(id):
    try:
        with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        linhas = []

    dados = []

    for linha in linhas:
        linha = linha.strip()
        if linha:
            dados.append(linha.split(",", 2))

    encontrado = False
    for i in dados:
        if i[0] == id:
            dados.remove(i)
            encontrado = True
            print("Dados removidos com sucesso")
            break

    if not encontrado:
        print("Não há nenhum usuário com o id cadastrado")

    with open("salvadados.txt", "w", encoding="utf-8") as arquivo:
            for pessoa in dados:
                arquivo.write(f"{pessoa[0]},{pessoa[1]},{pessoa[2]}\n")


def fazopix(id1, id2):
    try:
        with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        linhas = []

    dados = []
    for linha in linhas:
        linha = linha.strip()
        if linha:
            # Separa por vírgula em exatamente 3 partes: [ID, Nome, Saldo]
            dados.append(linha.split(",", 2))

    valor = float(input(f"Digite o valor a transferir: "))

    for ids in dados:
        if ids[0] == id1:
            saldo_atual = float(ids[2])
            if valor > saldo_atual:
                print("Saldo insuficiente!")
                return
            ids[2] = str(saldo_atual - valor)

        if ids[0] == id2:
            saldo_atual = float(ids[2])
            ids[2] = str(saldo_atual + valor)

    with open("salvadados.txt", "w", encoding="utf-8") as arquivo:
        for pessoa in dados:
            arquivo.write(f"{pessoa[0]},{pessoa[1]},{pessoa[2]}\n")

    print("Pix realizado com sucesso!")

def recebimento(id3):
    try:
        with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        linhas = []

    dados = []
    for linha in linhas:
        linha = linha.strip()
        if linha:
            dados.append(linha.split(",", 2))

    salario = float(input(f"Digite o valor que o id vai receber: "))
    
    if salario >= 0:
        for p in dados:
            if p[0] == id3:
                # Converte o saldo para float antes de somar
                p[2] = str(float(p[2]) + salario)
    else:
        print("Valor do salário insuficiente ou negativo.")
        return

    with open("salvadados.txt", "w", encoding="utf-8") as arquivo:
        for pessoa in dados:
            arquivo.write(f"{pessoa[0]},{pessoa[1]},{pessoa[2]}\n")

    print("Transação realizada.")

def exiba_saldo(id4):
    try:
        with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        linhas = []
    
    dados = []
    for linha in linhas:
        linha = linha.strip()
        if linha:
            dados.append(linha.split(",", 2))

    for i in dados:
        if i[0] == id4:
            print("O salário desse id é: R$", i[2])

def editar_nome(id5, novo_nome):
    try:
        with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        linhas = []

    dados = []
    for linha in linhas:
        linha = linha.strip()
        if linha:
            dados.append(linha.split(",", 2))

    encontrado = False
    for p in dados:
        if p[0] == id5:
            p[1] = novo_nome
            encontrado = True
            break

    if not encontrado:
        print("Não há nenhum usuário com o id cadastrado")
        return

    with open("salvadados.txt", "w", encoding="utf-8") as arquivo:
        for pessoa in dados:
            arquivo.write(f"{pessoa[0]},{pessoa[1]},{pessoa[2]}\n")

    print("Nome atualizado com sucesso!")


while True:
    print("BEM-VINDO AO SISTEMA BANCÁRIO DESENVOLVIDO POR GABRIEL")
    print("FAÇA ALGUMA DAS OPERAÇÕES ABAIXO")
    print("1 - CADASTRAMENTO DE USUÁRIO")
    print("2 - REALIZE O PIX PARA ALGUÉM")
    print("3 - REALIZE O PAGAMENTO/SALÁRIO DE ALGUÉM")
    print("4 - DELETE O USUÁRIO")
    print("5 - EXIBA O SALDO DO ID/USUÁRIO CADASTRADO")
    print("6 - EDITE O NOME DO ID/USUÁRIO CADASTRADO")
    print("PARA SAIR DO PROGRAMA, BASTA CLICAR EM QUALQUER OUTRA TECLA")

    numero = input()
    if numero.isdigit():
        numero_alterado = int(numero)
        if numero_alterado == 1:
            nome = input("Digite o nome da pessoa que deseja realizar o cadastramento em nosso sistema bancário: ")
            if nome.strip() and not any(c in "0123456789_=+[]'~.,;/?:><^}{`|" for c in nome):
                cadastrar(nome)
            else:
                print("Digite um nome válido!")
                continue
        elif numero_alterado == 2:
             try:
                 with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
                     linhas = arquivo.readlines()
             except FileNotFoundError:
                 linhas = []
             dados = []
             for linha in linhas:
                 linha = linha.strip()
                 if linha:
                     dados.append(linha.split(",", 2))

             id1 = (input("Digite o id de cadastro do usuário que vai realizar o pix:"))
             if id1.isdigit():
                for i in dados:
                    if i[0] == id1:
                        id2 = (input("Digite o id de cadastro do usuário que vai receber o pix: "))
                        if id2.isdigit():
                            for j in dados:
                                if j[0] == id2:
                                    fazopix(id1,id2)
                        else:
                            print("O id digitado não corresponde a noção padrão, tente novamente.")
                            continue
             else:
                 print("O id digitado não corresponde a noção padrão, tente novamente.")
                 continue
        elif numero_alterado == 3:
            try:
                with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
                    linhas = arquivo.readlines()
            except FileNotFoundError:
                linhas = []
            dados = []
            for linha in linhas:
                linha = linha.strip()
                if linha:
                    dados.append(linha.split(",", 2))

            id3 = (input("Digite o id para realizar o pagamento."))
            if id3.isdigit():
                for i in dados:
                    if i[0] == id3:
                        recebimento(id3)
            else:
                print("O id digitado não corresponde a noção padrão, tente novamente.")
                continue
        elif numero_alterado == 4:
            try:
                with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
                    linhas = arquivo.readlines()
            except FileNotFoundError:
                linhas = []
            dados = []
            for linha in linhas:
                linha = linha.strip()
                if linha:
                    dados.append(linha.split(",", 2))

            id = (input("Digite o id para realizar a exclusão:"))
            if id.isdigit():
                for i in dados:
                    if i[0] == id:
                        excluir(id)
            else:
                print("O id digitado não corresponde a noção padrão, tente novamente.")
                continue
        elif numero_alterado == 5:
            try:
                with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
                    linhas = arquivo.readlines()
            except FileNotFoundError:
                linhas = []
            dados = []
            for linha in linhas:
                linha = linha.strip()
                if linha:
                    dados.append(linha.split(",", 2))

            id4 = (input("Digite o id para realizar o exibimento:"))
            if id4.isdigit():
                for i in dados:
                    if i[0] == id4:
                        exiba_saldo(id4)
            else:
                print("O id digitado não corresponde a noção padrão, tente novamente.")
                continue
        elif numero_alterado == 6:
            try:
                with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
                    linhas = arquivo.readlines()
            except FileNotFoundError:
                linhas = []
            dados = []
            for linha in linhas:
                linha = linha.strip()
                if linha:
                    dados.append(linha.split(",", 2))

            id5 = (input("Digite o id para editar o nome:"))
            if id5.isdigit():
                for i in dados:
                    if i[0] == id5:
                        novo_nome = input("Digite o novo nome: ")
                        if novo_nome.strip() and not any(c in "0123456789_=+[]'~.,;/?:><^}{`|" for c in novo_nome):
                            editar_nome(id5, novo_nome)
                        else:
                            print("Digite um nome válido!")
            else:
                print("O id digitado não corresponde a noção padrão, tente novamente.")
                continue
        else:
            print("Programa encerrado.")
            break
    else:
        print("Programa encerrado")
        break