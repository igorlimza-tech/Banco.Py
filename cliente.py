from utilidades import validar_cpf, validar_tel

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