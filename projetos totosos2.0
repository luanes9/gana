def imprimir_animes (animes):
    print("Animes cadastrados: ")
    for i, desenho in enumerate(animes):
        print(f"[{i+1}] - {desenho}")

animes = ["Nanatsu no taizai", "Naruto", "Nana", "Dorohedoro", "Beastars"]

while True:
    imprimir_animes(animes)
    escolha = int(input("""Digite o que você quer escolher:
    [1] Adiciona item a lista 
    [2] Alterar item a lista 
    [3] Remover item a lista
    [4] Sair
    => """))

    if escolha == 1:
        itens = int(input("Quantos itens você quer adicionar? "))
        if itens <= 0:
            print("Faz direito.")
            
        novos = ''
        for a in range(itens):
            novos = input("Escreva os animes que quer adicionar: ")
            animes.append (novos)
        imprimir_animes(animes)

    elif escolha == 2:
        imprimir_animes(animes)
        indice = int(input("Digite um indice para alterar: "))
        if indice <=0:
            print("Esta opção não está disponível")
            break 

        elif indice > len(animes):
        print(f"Esta opção não está disponível")
        break
        
        animados = input("Digite o novo anime: ")
        animes[indice-1] = animados

    elif escolha == 3:
        imprimir_animes(animes)
        qnt = int(input("Digite um indice para remover: "))
        
        if qnt <= 0:
            print("Esta opção não está disponível")
            break 
            
        elif qnt > len(animes):
         print("Esta opção não está disponível")
         break
        
        argh = qnt - 1
        ainimes = animes.pop(argh)
        
    elif escolha == 4:
        print("Tente novamente!")
        break

    else:
        print("Digite algo valido")

imprimir_animes(animes)
