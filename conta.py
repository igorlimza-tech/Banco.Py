from utilidades import verifica_num, ler_int

class ContaBancaria:
    def __init__(self, cliente, conta, saldo):
        self.cliente = cliente
        self.conta = conta
        self.saldo = saldo
        self.extrato = []

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append(f"Deposito: R${valor:.2f}")
        print("Depósito concluído com sucesso!")

    def sacar(self, saque):
        if saque > self.saldo:
            print("Você não pode sacar um valor maior que o saldo.")
        else:
            self.saldo -= saque
            self.extrato.append(f"Saque: R${saque:.2f}")
            print("Saque concluído com sucesso!")

    def mostra_saldo(self):
        print(f"Conta: {self.conta}")
        print(f"Titular: {self.cliente.nome}")
        print(f"Saldo: R$ {self.saldo:.2f}")

    def mostrar_extrato(self):
        if len(self.extrato) == 0:
            print("Nenhuma operação realizada!")
        else:
            print("\n" + "=" * 12)
            print("EXTRATO")
            print("=" * 12)

        for operacao in self.extrato:
            print(operacao)


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