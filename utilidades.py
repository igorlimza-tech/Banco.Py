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