eleitores = {
    "Ana": 11111111111,
    "Bruno": 22222222222,
    "Carla": 3333333333
}
#oi

candidatos = {
    "Giovana": {"numero": 1608, "votos": 0},
    "Gustavo": {"numero": 3115, "votos": 0},
    "Nulo": {"numero": 0, "votos": 0}
}

print("Bem-vindo ao sistema de votação!")

def menu():
    print("[1] INICIAR VOTAÇÃO\n[2] CADASTRO DE ELEITOR\n[3] CADASTRO DE CANDIDATO\n[4] SAIR")
    while True:
        try:
            opcao = int(input("Qual opção deseja? "))
            if opcao in [1, 2, 3, 4]:
                return opcao
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Digite um número válido.")
while True:
    opcao = menu()
    if opcao == 1:
        while True:
            ja_votou = {}
            print("\n--- Identificação do Eleitor ---")
            nome = input("Digite o seu nome: ").capitalize()
            cpf = int(input("Digite o seu CPF: "))
            ja_votou[nome] = cpf

            if nome not in eleitores or eleitores[nome] != cpf:
                print("Eleitor não cadastrado ou CPF incorreto. Não pode votar.\n"
                    "Realize o pagamento da multa para ter seus direitos regularizados")

                if cpf in ja_votou:
                    print("Voto já computado para este CPF.")

            print("Eleitor localizado. Boa votação")

            print("\nCandidatos:")
            for nome_cand, info in candidatos.items():
                print(f"{nome_cand} - Número: {info['numero']}")

            voto = int(input("Digite o número do seu candidato: "))

            votou = False
            for nome_cand, info in candidatos.items():
                if voto == info["numero"]:
                    info["votos"] += 1
                    votou = True
                    print(f"Voto computado para {nome_cand}!")
                    break

            if not votou:
                print("Número inválido. Voto não computado.")

            sair = input("Deseja encerrar a votação? (s/n): ").lower()
            if sair == "s":
                break
    if opcao == 2:
        while True:
            print("Realizar Novo Cadastro de Eleitor")
            nome_eleitor = input("Digite seu nome: ")
            cpf_eleitor = int(input("Digite seu CPF: "))
            eleitores[nome_eleitor] = cpf_eleitor
            if input("Deseja cadastrar outro eleitor?(s/n): ") == "n":
                break
    
    
    if opcao == 3:
        while True:
            print("Realizar Novo Cadastro de Candidato")
            nome_cand = input("Digite o nome do candidato: ")
            
            while True: 
                numero_cand = int(input("Digite o número do candidato: "))
                numero_ja_cadastrado = False

                for info in candidatos.values():
                     if info["numero"] == numero_cand:
                       numero_ja_cadastrado = True
                       break

                if numero_ja_cadastrado:
                   print("Esse número de eleitor pertence a outro candidato, tente novamente.")
                else:
                 break
                
            candidatos[nome_cand] = {"numero": numero_cand, "votos": 0}

            if input("Deseja cadastrar outro Candidato?(s/n)") == "n":
                break
        for nome_cand, info in candidatos.items():
            print(f"{nome_cand} - Número: {info['numero']}")
         

    if opcao == 4:
        print("\nResultado da votação:")
        for nome_cand, info in candidatos.items():
            print(f"{nome_cand}: {info['votos']} voto(s)")

        print("Saindo do sistema.")
        break