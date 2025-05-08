dicionario=[]
while True:
    print("\\\\\\\\\\\\\\\DICIONARIO EM INGLÊS\\\\\\\\\\\\\\\\\\")
    opcao=int(input("1. digite um para adicionar uma palavra\n2. digite dois para ver a lista\n3. digite três para filtar\n4. digite quatro para filtar:"))
    if opcao==1:
        add_dic=str(input("digite a palavra que vc quer adiciona")).strip()
        add_tipo=str(input("digite o tipo da palavra"))
        add_traducao=str(input("digite a traduçâo dessa palavra"))
        add_primeira=str(input("digite a primeira letra dessa palavra"))
        suruba={"nome": add_dic, "tipo": add_tipo, "traduçâo": add_traducao, "letra": add_primeira}
        dicionario.append(suruba)
    elif opcao==2:
        print(dicionario)
    elif opcao==3:
        letra=str(input("digite uma letra para filtra as palavras"))
        for suruba in dicionario:
            if suruba['letra']==letra:
                print(f"palavras filtradas nome: {suruba['nome']} tipo: {suruba['tipo']} traduçâo: {suruba['traduçâo']} letra: {suruba['letra']}")
    else:
        print("saindo...")
        break
