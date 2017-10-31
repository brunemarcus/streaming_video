#interface_usuario

def entrada_usuario():
    nome=[]
    idade=[]
    cpf=[]
    assinatura=[]
    senha=[]
    A=1
    while A==1:
        print("Digite '1' para se cadastrar:")
        print("Digite '0' para sair:")
        opcao=int(input("Digite uma opção:"))
        if opcao==1:
            A==1
            N1=input("Digite seu nome completo:")
            nome.append(N1)
            N2=input("Digite sua data de nascimento:")
            idade.append(N2)
            N3=int(input("Digite seu cpf:"))
            cpf.append(N3)
            print("Digite '1' para assinatura 'Premium': você tem direito a todos os filmes e filmes exclusivos/lançamentos na mesma semana.")
            print("Digite '2' para assinatura 'Padrão': você tem direito a todos os filmes e 1 filme por vez.")
            print("Digite '3' para assinatura 'Família': você tem direito a todos os filmes e compartilhamento de tela com até 4 pessoas ao mesmo tempo.")
            print("Digite '4' para assinatura 'Kids': você terá acesso a filmes abaixo de 16 anos.")
            print("Digite '5' para assinatura 'Gratuita': você terá acesso a 7 dias gratis para testar.")

            N4=int(input("Digite qual pacote de assinatura:"))
            if N4==1:
                assinatura.append(N4)
            if N4==2:
                assinatura.append(N4)
            if N4==3:
                assinatura.append(N4)
            if N4==4:
                assinatura.append(N4)
            if N4==5:
                assinatura.append(N4)
            N5=input("Digite sua senha:")
            senha.append(N5)
        else:
            A+=1
   
        
    


        
        

                 
                      
        
