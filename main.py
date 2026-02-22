from random import randint



def menu():

    print("\n==== Bem-Vindo ao Sistema de cadastro Eleitoral ====\n")
    print("Escolha uma das Opções Abaixo:\n")
    print("1 - Cadastra-se")
    print("2 - Visualizar Cadastro")
    print("0 - Sair do Sistema\n")


    while True:
        
        escolha = input("Digite a opção desejada: ")

        if escolha == '1':
            print("Vamos realizar o seu cadastro.\n")
            dados = cadastro()
            dados_eleitoral = titulo_eleitor(dados)
            salvar_dados(dados, dados_eleitoral)
            break
                        
        elif escolha == '2':
            print("Vamos visualizar o seu cadastro.\n")
            visualizar_cadastro()
            break
        
        elif escolha == '0':            
            print("Saindo do Sistema... Até logo!\n")
            break
            
        else:
            print("Opção inválida! Tente novamente.\n")
            break

def cadastro():
    
    nome = input("\nNome Completo: ")
    data_nascimento = input("Digite a sua data de nascimento: ")
    cpf = input("Digite o seu CPF: ")
    endereco = input("Digite seu endereço: ")
    telefone = input("Digite seu telefone: ") 
    ano_nascimento = int(input("Digite o seu ano de nascimento: "))
    idade = 2026 - ano_nascimento

    return nome, data_nascimento, cpf, endereco, telefone, idade 
    

def salvar_dados(dados, dados_eleitoral):

    with open("Banco de Dados - Usuários.txt", "a") as arquivo:

        arquivo.write('---------------------------\n')
        arquivo.write(f'Nome: {dados[0]}\n')
        arquivo.write(f'Data de Nascimento: {dados[1]}\n')
        arquivo.write(f'CPF: {dados[2]}\n')
        arquivo.write(f'Enedereco: {dados[3]}\n')
        arquivo.write(f'Telefone: {dados[4]}\n')
        arquivo.write("\n==== REPUBLICA FEDERATIVA DO BRASIL ====\n")
        arquivo.write(f'Titulo: {dados_eleitoral[0]}\n')
        arquivo.write(f'Data: {dados_eleitoral[1]}\n')
        arquivo.write(f'Zona: {dados_eleitoral[2]}\n')
        arquivo.write(f'Secaoo: {dados_eleitoral[3]}\n')
        arquivo.write('---------------------------\n\n')

def titulo_eleitor(dados):

    if dados[5] < 16:
        print(f"\n{dados[0]}, você tem {dados[5]} anos e ainda não pode emetir Título de Eleitor, Retorne quando tiver 16 anos ou mais.")
        
        return 'Não Elegível', '-', '-', '-'

    elif dados[5] in range(16, 18):
        titulo = input("Deseja emitir o seu Título de eleitor? (S/N): ").upper()

        if titulo == 'N':
            print("\nTudo bem, fica para a próxima. Até logo...\n")

            return 'Não Emitido', '-', '-', '-'
            
        elif titulo == 'S':

            numTitulo = randint(1,1000000)
            data = "20/02/2026"
            zona = randint(1, 1000)
            secao = randint(1, 100)

            return numTitulo, data, zona, secao

    elif dados[5] >= 18:
        print(f"\n{dados[0]}, caso ainda não tenha feito o Título de Eleitor, chegou a sua hora!\n")

        numTitulo = randint(1,1000000)
        data = "20/02/2026"
        zona = randint(1, 1000)
        secao = randint(1, 100)

        return numTitulo, data, zona, secao

def visualizar_cadastro():

    cpf_digitado = input("Digite o seu CPF (ex. 999.999.999-99): ")


    try: 

        with open("Banco de Dados - Usuários.txt", "r") as arquivo:
            

            verificar_linhas = []
            encontrado = False
            
            for linha in arquivo: 

                linha_limpa = linha.strip()

                if linha_limpa == "---------------------------":

                    if verificar_linhas: 

                        texto_bloco = "". join(verificar_linhas)

                        if cpf_digitado in texto_bloco:
                            print("\n--- Cadastro encontrado ---\n")
                            print(texto_bloco)
                            encontrado = True
                            break

                        verificar_linhas = []

                else: 
                    verificar_linhas.append(linha)

            if not encontrado and verificar_linhas:
                texto_bloco = "".join(verificar_linhas)

                if cpf_digitado in texto_bloco:
                    print("\n--- Cadastro encontrado --\n")
                    print(texto_bloco)
                    encontrado = True

            if not encontrado:
                print("CPF não encontrado no sistema.")

    except FileNotFoundError:
        print("O arquivo Banco de Dados - Usuários.txt não foi encontrado.")            

    


menu()