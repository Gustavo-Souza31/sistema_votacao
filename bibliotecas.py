import pickle
import plotly.graph_objects as go

# Funções para salvar e carregar dados
def salvar_dados():
    with open("dados_votacao.pkl", "wb") as f:
        pickle.dump({"eleitores": eleitores, "candidatos": candidatos, "votos_computados": votos_computados}, f)

def carregar_dados():
    global eleitores, candidatos, votos_computados
    try:
        with open("dados_votacao.pkl", "rb") as f:
            dados = pickle.load(f)
            eleitores = dados["eleitores"]
            candidatos = dados["candidatos"]
            votos_computados = dados["votos_computados"]
    except FileNotFoundError:
        pass # Se o arquivo não existir, usa os dados iniciais

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

carregar_dados()

print("Bem-vindo ao sistema de votação!")

def menu():
    print("\n[1] INICIAR VOTAÇÃO\n[2] CADASTRO DE ELEITOR\n[3] CADASTRO DE CANDIDATO\n[4] VISUALIZAR RESULTADOS GRÁFICOS\n[5] SAIR")
    while True:
        try:
            opcao = int(input("Qual opção deseja? "))
            if opcao in [1, 2, 3, 4, 5]:
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


        if cpf_eleitor not in eleitores:
            print("Eleitor não cadastrado. Não pode votar.\n" \
                  "Realize o pagamento da multa para ter seus direitos regularizados")


        if cpf_eleitor in votos_computados:
            print("Voto já computado para este CPF.")


        nome_eleitor = eleitores[cpf_eleitor]
        print(f"Eleitor {nome_eleitor} localizado. Boa votação!")

        print("\nCandidatos:")
        for nome_cand, info in candidatos.items():
            print(f"{nome_cand} - Número: {info['numero']}")

        try:
            voto = int(input("Digite o número do seu candidato (0 para NULO/BRANCO): "))
        except ValueError:
            print("Voto inválido. Digite apenas números.")


        votou = False
        for nome_cand, info in candidatos.items():
            if voto == info["numero"]:
                info["votos"] += 1
                votou = True
                print(f"Voto computado para {nome_cand}!")
                votos_computados.add(cpf_eleitor)
                salvar_dados()
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
                salvar_dados() 
            
            continuar = input("Deseja cadastrar outro eleitor? (s/n): ").lower()
            if continuar == "n":
                print("\nEleitores Cadastrados:")
                for cpf, nome in eleitores.items():
                    print(f"Nome: {nome}, CPF: {cpf}")
                break

    elif opcao == 3:
        while True:
            print("Realizar Novo Cadastro de Candidato")
            nome_cand = input("Digite o nome do candidato: ")
            
            while True: 
                try:
                    numero_cand = int(input("Digite o número do candidato: "))
                except ValueError:
                    print("Número inválido. Digite apenas números.")
                    continue

                numero_ja_cadastrado = False

                for info in candidatos.values():
                     if info["numero"] == numero_cand:
                       numero_ja_cadastrado = True
                       break

                if numero_ja_cadastrado:
                   print("Esse número de eleitor pertence a outro candidato, tente novamente.")
                else:
                 break
            
            if nome_cand in candidatos:
                print(f"Candidato {nome_cand} já cadastrado.")
            else:
                candidatos[nome_cand] = {"numero": numero_cand, "votos": 0}
                print("Candidato cadastrado com sucesso!")
                salvar_dados() 

            if input("Deseja cadastrar outro Candidato?(s/n)") == "n":
                break
        for nome_cand, info in candidatos.items():
            print(f"{nome_cand} - Número: {info['numero']}")

    elif opcao == 4:

        nomes = [nome for nome in candidatos.keys()]
        votos = [info["votos"] for info in candidatos.values()]

        fig = go.Figure(data=[go.Bar(x=nomes, y=votos)])
        fig.update_layout(title_text='Resultado da Votação', xaxis_title='Candidato', yaxis_title='Número de Votos')
        fig.write_html('resultado_votacao.html')
        print("Gráfico de resultados gerado em 'resultado_votacao.html'")

    elif opcao == 5:
        print("\n--- Resultado da Votação ---")
        for nome_cand, info in candidatos.items():
            print(f"{nome_cand}: {info['votos']} voto(s)")

        print("Saindo do sistema.")
        break


