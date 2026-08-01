from cliente import cadastrar_cliente, listar_clientes
from conta import  criar_conta, listar_contas, escolher_conta
from utilidades import ler_int, verifica_num

lista_clientes = []
lista_contas = []


def menu_opcoes():
    print("\n" + "-=" * 10 + " BANCO PY " + "-=" * 10)
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Criar conta")
    print("4. Listar contas")
    print("5. Depositar")
    print("6. Sacar")
    print("7. Mostrar saldo")
    print("8. Mostrar extrato")
    print("9. Sair")
    
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
        conta = escolher_conta(lista_contas)
        if conta is not None:
            conta.mostrar_extrato()

    elif opcao == 9:
        print("Saindo do programa...")
        break

    else:
        print("Digite uma opção existente")