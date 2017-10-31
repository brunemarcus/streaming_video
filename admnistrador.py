#menu_admistrador
 
def sistema(nome,idade,cpf,assinatura,senha):
    A=True
    while A==True:
        print("Digite '1' para ver a lista de cadastros:")
        print("Digite '0' para sair:")
        if opcao==1:
            for i in range (len(nome)):
                print("Nome:", nome[i], " -> ",
                      "Data de nascimento:",idade[i]," -> ",
                      "Cpf:", cpf[i]," -> ",
                      "Assinatura:", assinatura[i]," -> ",
                      "Senha:", senha[i])
