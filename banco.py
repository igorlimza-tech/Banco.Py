lista_clientes = []
lista_contas = []


class Cliente:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")


def cadastrar_cliente(lista_clientes):
    nome = input("Nome: ")
    while True:
        cpf = input("CPF:")
        if validar_cpf(cpf):
            break
        else:
            print("CPF inválido tente novamente!")
    while True:
        telefone = input("Telefone: ")
        if validar_tel(telefone):
            break
        else:
            print("Telefone inválido tente novamente!")

    novo_cliente = Cliente(nome, cpf, telefone)
    lista_clientes.append(novo_cliente)

    print("Cliente cadastrado com sucesso!")


def listar_clientes(lista_clientes):
    if len(lista_clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in lista_clientes:
            cliente.mostrar_dados()
            print()


class ContaBancaria:
    def __init__(self, cliente, conta, saldo):
        self.cliente = cliente
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito concluído com sucesso!")

    def sacar(self, saque):
        if saque > self.saldo:
            print("Você não pode sacar um valor maior que o saldo.")
        else:
            self.saldo -= saque
            print("Saque concluído com sucesso!")

    def mostra_saldo(self):
        print(f"Conta: {self.conta}")
        print(f"Titular: {self.cliente.nome}")
        print(f"Saldo: R$ {self.saldo:.2f}")


def criar_conta(lista_clientes, lista_contas):
    if len(lista_clientes) == 0:
        print("Nenhum cliente cadstrado. Cadastre um cliente primeiro")
        return
    for i, cliente in enumerate(lista_clientes,start=1):
        print(f"{i} - {cliente.nome}")
    escolha = ler_int("Qual cliente deseja escolher: ")
    while escolha < 1 or escolha > len(lista_clientes):
        print("Cliente inválido")
        escolha = ler_int("Escolha uma cliente válido: ")
    i_real = escolha-1
    cliente_escolhido = lista_clientes[i_real]  
    conta = len(lista_contas) + 1
    saldo = verifica_num("Saldo inicial: ")

    nova_conta = ContaBancaria(cliente_escolhido, conta, saldo)
    lista_contas.append(nova_conta)

    print("Conta criada com sucesso!")


def listar_contas(lista_contas):
    if len(lista_contas) == 0:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in lista_contas:
            conta.mostra_saldo()
            print()


def escolher_conta(lista_contas):
    if len(lista_contas) == 0:
        print("Nenhuma conta cadastrada")
        return
    for i, conta in enumerate(lista_contas, start=1):
        print(f"{i} - {conta.cliente.nome}")
    escolha = ler_int("Qual conta deseja escolher: ")
    while escolha <1 or escolha>len(lista_contas):
        print("Conta inválida")
        escolha = ler_int("Escolha uma conta válida: ")
    i_real = escolha - 1
    conta_escolhida = lista_contas[i_real]
    return conta_escolhida

def menu_opcoes():
    print("\n" + "-=" * 10 + " BANCO PY " + "-=" * 10)
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Criar conta")
    print("4. Listar contas")
    print("5. Depositar")
    print("6. Sacar")
    print("7. Mostrar saldo")
    print("8. Sair")


def ler_int(mensagem):
    while True:
            try:
                numero = int(input(mensagem))
                return numero
            except:
                print("Digite apenas números! ")
    

def ler_float(mensagem):
    while True:
            try:
                numero = float(input(mensagem))
                return numero
            except:
                print("Digite apenas números! ")

    
def verifica_num(mensagem):
    while True:
            num = ler_float(mensagem)
            if num >0:
                return num
            else:
                print("O valor tem que ser maior que R$0,00! ")


def validar_cpf(cpf):      
    cpf_limpo = ""
    for caractere in cpf:
        if caractere.isdigit():
            cpf_limpo += caractere 
    if len(cpf_limpo) == 11:
        return True
    else:
        return False


def validar_tel(telefone):
    tel_limpo = ""
    for caractere in telefone:
        if caractere.isdigit():
            tel_limpo += caractere 
    if len(tel_limpo) == 10 or len(tel_limpo) == 11:
            return True
    else:
        return False    
          

while True:
    menu_opcoes()

    opcao = ler_int("Qual opção deseja escolher: ")
      

    if opcao == 1:
        cadastrar_cliente(lista_clientes)

    elif opcao == 2:
        listar_clientes(lista_clientes)

    elif opcao == 3:
        criar_conta(lista_clientes, lista_contas)

    elif opcao == 4:
        listar_contas(lista_contas)

    elif opcao == 5:
        conta = escolher_conta(lista_contas)
        if conta is not None:
            valor = verifica_num("Insira o valor do depósito: R$ ")
            conta.depositar(valor)
        
    elif opcao == 6:
        conta = escolher_conta(lista_contas)
        if conta is not None:
            valor = verifica_num("Insira o valor do saque: R$ ")
            conta.sacar(valor)
         
    elif opcao == 7:
        conta = escolher_conta(lista_contas)
        if conta is not None:
           conta.mostra_saldo()

    elif opcao == 8:
        print("Saindo do programa...")
        break

    else:
        print("Digite uma opção existente")