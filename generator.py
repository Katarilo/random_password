import random

# caractéres aleatórios para o for ultilizar
caractéres_aleatórios = [
        '1','2','3','4','5','6','7','8','9','0',
        'a','b','c','d','e','f','g','h','i','j','k','l','m'
        ,'n','o','p','q','r','s','t','u','v','w','x','y','z'
        ,'!','@','#','$','%','&','*','(',')','-','_','=',';'
]

def gerar_senha(tamanho):
    senha = ''
    for i in range(tamanho):
        senha += random.choice(caractéres_aleatórios)
    return senha

def main():
    print('Olá, seja bem vindo ao gerador de senha aleatória!')
    
    # escolhe nome de usuário
    nome_usuario = input('Digite um nome de usuário q deseja: ')
    
    try:    
        escolha_tamanho = input('Escolha o tamanho da senha: ')
    except KeyboardInterrupt:
        print('\nPrograma interrompido pelo usuário.')
        return # encerra a função

    # checa se o que foi digitado é um número (digito)
    if escolha_tamanho.isdigit():
            escolha_tamanho = int(escolha_tamanho)   
            
            # gera a senha
            senha_final = gerar_senha(escolha_tamanho).upper()

            print(f'Sua senha aleatória é: {senha_final}')

            # agora salva sua senha como aquivo .txt
            with open("senha_gerada.txt", "w") as arquivo:
                arquivo.write(f'Usuário: {nome_usuario}\n')
                arquivo.write(f'Senha: {senha_final}\n')
    else: 
        print('voce nao digitou um numero, tente novamente')

# garante que só roda se o arquivo for executado diretamente
if __name__ == "__main__":
    main()
