eleitores = {
    11111111111: "Ana",
    22222222222: "Bruno",
    33333333333: "Carla"
}

candidatos = {
    "Giovana": {"numero": 1608, "votos": 0},
    "Gustavo": {"numero": 3115, "votos": 0},
    "Nulo": {"numero": 0, "votos": 0}
}

votos_computados = set()

print("Bem-vindo ao sistema de votação!")

def menu():
    print("\n[1] INICIAR VOTAÇÃO\n[2] CADASTRO DE ELEITOR\n[3] CADASTRO DE CANDIDATO\n[4] SAIR")
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
        print("\n--- Identificação do Eleitor ---")
        try:
            cpf_eleitor = int(input("Digite o seu CPF: "))
        except ValueError:
            print("CPF inválido. Digite apenas números.")
            continue

        if cpf_eleitor not in eleitores:
            print("Eleitor não cadastrado. Não pode votar.\n" \
                  "Realize o pagamento da multa para ter seus direitos regularizados")
            continue

        if cpf_eleitor in votos_computados:
            print("Voto já computado para este CPF.")
            continue
        
        nome_eleitor = eleitores[cpf_eleitor]
        print(f"Eleitor {nome_eleitor} localizado. Boa votação!")

        print("\nCandidatos:")
        for nome_cand, info in candidatos.items():
            print(f"{nome_cand} - Número: {info["numero"]}")

        try:
            voto = int(input("Digite o número do seu candidato (0 para NULO/BRANCO): "))
        except ValueError:
            print("Voto inválido. Digite apenas números.")
            continue

        votou = False
        for nome_cand, info in candidatos.items():
            if voto == info["numero"]:
                info["votos"] += 1
                votou = True
                print(f"Voto computado para {nome_cand}!")
                votos_computados.add(cpf_eleitor)
                break

        if not votou:
            print("Número inválido. Voto não computado.")

        sair = input("Deseja encerrar a votação? (s/n): ").lower()
        if sair == "s":
            break

    elif opcao == 2:
        while True:
            print("\n--- Realizar Novo Cadastro de Eleitor ---")
            try:
                cpf_eleitor = int(input("Digite o CPF do eleitor: "))
            except ValueError:
                print("CPF inválido. Digite apenas números.")
                continue

            if cpf_eleitor in eleitores:
                print("CPF já cadastrado.")
            else:
                nome_eleitor = input("Digite o nome do eleitor: ").strip().capitalize()
                if not nome_eleitor:
                    print("Nome do eleitor não pode ser vazio.")
                    continue
                eleitores[cpf_eleitor] = nome_eleitor
                print("Eleitor cadastrado com sucesso!")
            
            continuar = input("Deseja cadastrar outro eleitor? (s/n): ").lower()
            if continuar == "n":
                print("\nEleitores Cadastrados:")
                for cpf, nome in eleitores.items():
                    print(f"Nome: {nome}, CPF: {cpf}")
                break

    elif opcao == 3:
        while True:
            print("\n--- Realizar Novo Cadastro de Candidato ---")
            nome_cand = input("Digite o nome do candidato: ").strip().capitalize()
            if not nome_cand:
                print("Nome do candidato não pode ser vazio.")
                continue

            try:
                numero_cand = int(input("Digite o número do candidato: "))
            except ValueError:
                print("Número do candidato inválido. Digite apenas números.")
                continue
            
            numero_existente = False
            for cand_info in candidatos.values():
                if numero_cand == cand_info["numero"]:
                    numero_existente = True
                    break

            if numero_existente:
                print(f"Número {numero_cand} já está em uso por outro candidato.")
            elif nome_cand in candidatos:
                print(f"Candidato {nome_cand} já cadastrado.")
            else:
                candidatos[nome_cand] = {"numero": numero_cand, "votos": 0}
                print("Candidato cadastrado com sucesso!")
            
            continuar = input("Deseja cadastrar outro candidato? (s/n): ").lower()
            if continuar == "n":
                print("\nCandidatos Cadastrados:")
                for nome_cand, info in candidatos.items():
                    print(f"{nome_cand} - Número: {info["numero"]}")
                break

    elif opcao == 4:
        print("\n--- Resultado da Votação ---")
        for nome_cand, info in candidatos.items():
            print(f"{nome_cand}: {info["votos"]} voto(s)")

        print("Saindo do sistema.")
        break


