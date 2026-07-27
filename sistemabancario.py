import itertools

# Gerador simples de IDs sequenciais (começa em 1 e vai incrementando em memória)
gerar_novo_id = itertools.count(start=1).__next__

def cadastrar(nome):
    # Usa vírgula pra separar os campos, então dá pra salvar nome completo sem quebrar o formato
    with open("salvadados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{gerar_novo_id()},{nome},0.0\n")

def excluir(id_usuario):
    try:
        with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        linhas = []

    usuarios = []

    for linha in linhas:
        linha = linha.strip()
        if linha:
            usuarios.append(linha.split(",", 2))

    encontrado = False
    for usuario in usuarios:
        if usuario[0] == id_usuario:
            usuarios.remove(usuario)
            encontrado = True
            print("Dados removidos com sucesso")
            break

    if not encontrado:
        print("Não há nenhum usuário com o id cadastrado")

    with open("salvadados.txt", "w", encoding="utf-8") as arquivo:
            for usuario in usuarios:
                arquivo.write(f"{usuario[0]},{usuario[1]},{usuario[2]}\n")


def fazopix(id_remetente, id_destinatario):
    try:
        with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        linhas = []

    usuarios = []
    for linha in linhas:
        linha = linha.strip()
        if linha:
            # Separa por vírgula em exatamente 3 partes: [ID, Nome, Saldo]
            usuarios.append(linha.split(",", 2))

    valor = float(input(f"Digite o valor a transferir: "))

    for usuario in usuarios:
        if usuario[0] == id_remetente:
            saldo_atual = float(usuario[2])
            if valor > saldo_atual:
                print("Saldo insuficiente!")
                return
            usuario[2] = str(saldo_atual - valor)

        if usuario[0] == id_destinatario:
            saldo_atual = float(usuario[2])
            usuario[2] = str(saldo_atual + valor)

    with open("salvadados.txt", "w", encoding="utf-8") as arquivo:
        for usuario in usuarios:
            arquivo.write(f"{usuario[0]},{usuario[1]},{usuario[2]}\n")

    print("Pix realizado com sucesso!")

def recebimento(id_beneficiario):
    try:
        with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        linhas = []

    usuarios = []
    for linha in linhas:
        linha = linha.strip()
        if linha:
            usuarios.append(linha.split(",", 2))

    salario = float(input(f"Digite o valor que o id vai receber: "))
    
    if salario >= 0:
        for usuario in usuarios:
            if usuario[0] == id_beneficiario:
                # Converte o saldo para float antes de somar
                usuario[2] = str(float(usuario[2]) + salario)
    else:
        print("Valor do salário insuficiente ou negativo.")
        return

    with open("salvadados.txt", "w", encoding="utf-8") as arquivo:
        for usuario in usuarios:
            arquivo.write(f"{usuario[0]},{usuario[1]},{usuario[2]}\n")

    print("Transação realizada.")

def exiba_saldo(id_consulta):
    try:
        with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        linhas = []
    
    usuarios = []
    for linha in linhas:
        linha = linha.strip()
        if linha:
            usuarios.append(linha.split(",", 2))

    for usuario in usuarios:
        if usuario[0] == id_consulta:
            print("O salário desse id é: R$", usuario[2])

def editar_nome(id_usuario, novo_nome):
    try:
        with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        linhas = []

    usuarios = []
    for linha in linhas:
        linha = linha.strip()
        if linha:
            usuarios.append(linha.split(",", 2))

    encontrado = False
    for usuario in usuarios:
        if usuario[0] == id_usuario:
            usuario[1] = novo_nome
            encontrado = True
            break

    if not encontrado:
        print("Não há nenhum usuário com o id cadastrado")
        return

    with open("salvadados.txt", "w", encoding="utf-8") as arquivo:
        for usuario in usuarios:
            arquivo.write(f"{usuario[0]},{usuario[1]},{usuario[2]}\n")

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

    opcao = input()
    if opcao.isdigit():
        opcao_num = int(opcao)
        if opcao_num == 1:
            nome = input("Digite o nome da pessoa que deseja realizar o cadastramento em nosso sistema bancário: ")
            if nome.strip() and not any(c in "0123456789_=+[]'~.,;/?:><^}{`|" for c in nome):
                cadastrar(nome)
            else:
                print("Digite um nome válido!")
                continue
        elif opcao_num == 2:
             try:
                 with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
                     linhas = arquivo.readlines()
             except FileNotFoundError:
                 linhas = []
             usuarios = []
             for linha in linhas:
                 linha = linha.strip()
                 if linha:
                     usuarios.append(linha.split(",", 2))

             id_remetente = (input("Digite o id de cadastro do usuário que vai realizar o pix:"))
             if id_remetente.isdigit():
                for usuario in usuarios:
                    if usuario[0] == id_remetente:
                        id_destinatario = (input("Digite o id de cadastro do usuário que vai receber o pix: "))
                        if id_destinatario.isdigit():
                            for outro_usuario in usuarios:
                                if outro_usuario[0] == id_destinatario:
                                    fazopix(id_remetente, id_destinatario)
                        else:
                            print("O id digitado não corresponde a noção padrão, tente novamente.")
                            continue
             else:
                 print("O id digitado não corresponde a noção padrão, tente novamente.")
                 continue
        elif opcao_num == 3:
            try:
                with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
                    linhas = arquivo.readlines()
            except FileNotFoundError:
                linhas = []
            usuarios = []
            for linha in linhas:
                linha = linha.strip()
                if linha:
                    usuarios.append(linha.split(",", 2))

            id_pagamento = (input("Digite o id para realizar o pagamento."))
            if id_pagamento.isdigit():
                for usuario in usuarios:
                    if usuario[0] == id_pagamento:
                        recebimento(id_pagamento)
            else:
                print("O id digitado não corresponde a noção padrão, tente novamente.")
                continue
        elif opcao_num == 4:
            try:
                with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
                    linhas = arquivo.readlines()
            except FileNotFoundError:
                linhas = []
            usuarios = []
            for linha in linhas:
                linha = linha.strip()
                if linha:
                    usuarios.append(linha.split(",", 2))

            id_exclusao = (input("Digite o id para realizar a exclusão:"))
            if id_exclusao.isdigit():
                for usuario in usuarios:
                    if usuario[0] == id_exclusao:
                        excluir(id_exclusao)
            else:
                print("O id digitado não corresponde a noção padrão, tente novamente.")
                continue
        elif opcao_num == 5:
            try:
                with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
                    linhas = arquivo.readlines()
            except FileNotFoundError:
                linhas = []
            usuarios = []
            for linha in linhas:
                linha = linha.strip()
                if linha:
                    usuarios.append(linha.split(",", 2))

            id_consulta = (input("Digite o id para realizar o exibimento:"))
            if id_consulta.isdigit():
                for usuario in usuarios:
                    if usuario[0] == id_consulta:
                        exiba_saldo(id_consulta)
            else:
                print("O id digitado não corresponde a noção padrão, tente novamente.")
                continue
        elif opcao_num == 6:
            try:
                with open("salvadados.txt", "r", encoding="utf-8") as arquivo:
                    linhas = arquivo.readlines()
            except FileNotFoundError:
                linhas = []
            usuarios = []
            for linha in linhas:
                linha = linha.strip()
                if linha:
                    usuarios.append(linha.split(",", 2))

            id_edicao = (input("Digite o id para editar o nome:"))
            if id_edicao.isdigit():
                for usuario in usuarios:
                    if usuario[0] == id_edicao:
                        novo_nome = input("Digite o novo nome: ")
                        if novo_nome.strip() and not any(c in "0123456789_=+[]'~.,;/?:><^}{`|" for c in novo_nome):
                            editar_nome(id_edicao, novo_nome)
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
