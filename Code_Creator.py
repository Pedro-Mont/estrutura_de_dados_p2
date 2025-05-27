import json
import os

#(Dados principais)
tipos = {}
grupo_personagem = []

print("\n |[CHARACTER CREATOR]|")

#(Caminho do JSON na mesma pasta do script)
CAMINHO_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Json_Creator.json")

#(Função para salvar dados em JSON)
def salvar_dados():
    dados_para_salvar = {
        "tipos": {k: list(v) for k, v in tipos.items()},
        "grupo_personagem": grupo_personagem
    }
    with open(CAMINHO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados_para_salvar, f, ensure_ascii=False, indent=4)

#(Função para carregar dados do JSON)
def carregar_dados():
    global tipos, grupo_personagem
    if os.path.exists(CAMINHO_JSON):
        with open(CAMINHO_JSON, "r", encoding="utf-8") as f:
            dados = json.load(f)
            # Convertemos as listas de volta para conjuntos
            tipos = {k: set(v) for k, v in dados.get("tipos", {}).items()}
            grupo_personagem = dados.get("grupo_personagem", [])

#(Carregamento automático ao iniciar)
carregar_dados()

#FUNÇÃO(1)-cadastrar_tipo.________________________________
def cadastrar_tipo():
    nome = input("Digite o nome do tipo: ").strip().title()
    if not nome:
        print("\n''Tipo não pode ser vazio.''")
        return
    if nome in tipos:
        print("\n''Tipo já cadastrado.''")
    else:
        tipos[nome] = []
        print(f"\n''Tipo ({nome}) cadastrado com sucesso!''")

# FUNÇÃO(2)-registrar_personagem.________________________________
def registrar_personagem():
    if not tipos:
        print("\n''Não é possível cadastrar personagem pois não há um Tipo.''")
        return

    registro_id = input("Informe o ID do personagem: ").strip()
    if not registro_id:
        print("\n''ID não informado.''")
        return
    if any(p["ID"] == registro_id for p in grupo_personagem):
        print("\n''ID já existente.''")
        return

    tipo = input("Informe o Nome do Tipo: ").strip().title()
    if not tipo:
        print("\n''Tipo não pode ser vazio.''")
        return
    if tipo not in tipos:
        print("\n''Tipo não existe.''")
        return

    nome     = input("Informe o Nome Real do personagem: ").strip().title() or "[-Desconhecido-]"
    codinome = input(f"Informe o Nome de {tipo} do personagem: ").strip().title() or "[-Desconhecido-]"
    poder    = input("Informe o Poder do personagem: ").strip().capitalize() or "[-Desconhecido-]"
    idade    = input("Informe a Idade do personagem: ").strip() or "[-Desconhecido-]"
    genero   = input("Informe o Gênero (M/F): ").strip().upper() or "[-Desconhecido-]"
    origem   = input("Informe a Origem do personagem: ").strip().capitalize() or "[-Desconhecido-]"

    personagem = {
        "ID": registro_id,
        "Tipo": tipo,
        "Nome": nome,
        "Codinome": codinome,
        "Poder": poder,
        "Idade": idade,
        "Gênero": genero,
        "Origem": origem
    }

    grupo_personagem.append(personagem)
    tipos[tipo].append(nome)
    print("\n''Personagem cadastrado com sucesso!''")

#FUNÇÃO(3)-info_personagem_id.________________________________
def info_personagem_id():
    if not grupo_personagem:
        print("\n''Nenhum personagem cadastrado.''")
        return

    id_busca = input("Digite o ID do personagem: ")
    for p in grupo_personagem:
        if p["ID"] == id_busca:
            print("\n- Personagem encontrado:")
            dados_tupla = tuple(p.items())
            maior_chave = max(len(k) for k, _ in dados_tupla)
            for chave, valor in dados_tupla:
                print(f"{(chave + ':').ljust(maior_chave + 1)} {valor}")
            return
    print("\n''Personagem não encontrado.''")

#FUNÇÃO(4)-editar_personagem.________________________________
def editar_personagem():
    if not grupo_personagem:
        print("\n''Nenhum personagem cadastrado.''")
        return

    id_atual = input("Digite o ID do personagem a editar: ")
    personagem = next((p for p in grupo_personagem if p["ID"] == id_atual), None)
    if not personagem:
        print("\n''Personagem não encontrado.''")
        return

    novo_id = input("Novo ID: ").strip() or personagem["ID"]
    if not novo_id:
        print("\n''ID não informado.''")
        return
    if novo_id != id_atual and any(p["ID"] == novo_id for p in grupo_personagem):
        print("\n''ID já existente.''")
        return

    novo_tipo = input("Novo Tipo: ").strip().title() or personagem["Tipo"]
    if novo_tipo not in tipos:
        print("\n''Tipo não existe.''")
        return

    # Atualiza o conjunto de nomes no tipo antigo, caso o tipo seja alterado
    tipos[personagem["Tipo"]].discard(personagem["Nome"])
    tipos[novo_tipo].add(personagem["Nome"])

    personagem["ID"]       = novo_id
    personagem["Tipo"]     = novo_tipo
    personagem["Nome"]     = input("Novo Nome: ").strip().title() or "[-Desconhecido-]"
    personagem["Codinome"] = input("Novo Codinome: ").strip().title() or "[-Desconhecido-]"
    personagem["Poder"]    = input("Novo Poder: ").strip().capitalize() or "[-Desconhecido-]"
    personagem["Idade"]    = input("Nova Idade: ").strip() or "[-Desconhecido-]"
    personagem["Gênero"]   = input("Novo Gênero (M/F): ").strip().upper() or "[-Desconhecido-]"
    personagem["Origem"]   = input("Nova Origem: ").strip().capitalize() or "[-Desconhecido-]"

    tipos[novo_tipo].add(personagem["Nome"])

    print("\n''Personagem editado com sucesso!''")

#FUNÇÃO(5)-excluir_personagem.________________________________
def excluir_personagem():
    if not grupo_personagem:
        print("\n''Nenhum personagem cadastrado.''")
        return

    id_excluir = input("Digite o ID do personagem a excluir: ")
    for p in grupo_personagem:
        if p["ID"] == id_excluir:
            grupo_personagem.remove(p)
            tipos[p["Tipo"]].remove(p["Nome"])
            print(f"\nPersonagem ({p['Nome'].title()}/{p['Codinome'].title()}) excluído com sucesso!")
            return
    print("\n''Personagem não encontrado.''")

#FUNÇÃO(6)-mostrar_personagens_do_tipo.___________________________
def mostrar_personagens_do_tipo():
    if not grupo_personagem:
        print("\n''Nenhum personagem cadastrado.''")
        return

    tipo = input("Digite o nome do tipo: ").strip().title()
    if tipo not in tipos:
        print("\n''Tipo não encontrado.''")
        return

    encontrados = [p for p in grupo_personagem if p["Tipo"] == tipo]
    if not encontrados:
        print("\n''Nenhum personagem desse tipo.''")
        return

    print(f"\nPersonagens do tipo ({tipo}):")
    for p in encontrados:
        print(f'({p["ID"]}): {p["Codinome"]}')

#FUNÇÃO(7)-mostrar_tipos.________________________________
def mostrar_tipos():
    if not tipos:
        print("\n''Tipo não cadastrado ainda.''")
        return

    print("\nTipos cadastrados:")
    for t in tipos:
        print(f"- ({t})")

#FUNÇÃO(8)-editar_tipo.________________________________
def editar_tipo():
    if not tipos:
        print("\n''Nenhum tipo cadastrado.''")
        return

    tipo_atual = input("Digite o nome do tipo que deseja editar: ").strip().title()
    if tipo_atual not in tipos:
        print("\n''Tipo não encontrado.''")
        return

    novo_tipo = input("Digite o novo nome do tipo: ").strip().title()
    if not novo_tipo:
        print("\n''Tipo não informado.''")
        return
    if novo_tipo == tipo_atual:
        print("\n''O tipo informado é igual ao atual. Nenhuma alteração feita.''")
        return
    if novo_tipo in tipos:
        print("\n''Tipo já existente.''")
        return

    tipos[novo_tipo] = tipos.pop(tipo_atual)

    for p in grupo_personagem:
        if p["Tipo"] == tipo_atual:
            p["Tipo"] = novo_tipo

    print("\n''Tipo editado com sucesso.''")

#FUNÇÃO(9)-excluir_tipo.________________________________
def excluir_tipo():
    if not tipos:
        print("\n''Nenhum tipo cadastrado.''")
        return

    tipo = input("Digite o nome do tipo a excluir: ").strip().title()
    if tipo not in tipos:
        print("\n''Tipo não encontrado.''")
        return

    grupo_personagem[:] = [p for p in grupo_personagem if p["Tipo"] != tipo]
    del tipos[tipo]
    print(f"\n''Tipo ({tipo}) excluído com sucesso!''")

#FUNÇÃO(10)-main.________________________________
def main():
    while True:
        print("\n--< Menu Principal >--")
        print("1. Cadastrar o Tipo(herói/vilão/etc)")
        print("2. Registrar um Personagem")
        print("3. Informações do Personagem por ID")
        print("4. Editar um Personagem por ID")
        print("5. Excluir um Personagem por ID")
        print("6. Mostrar Personagens de um Tipo")
        print("7. Mostrar todos os Tipos")
        print("8. Editar um Tipo pelo nome")
        print("9. Excluir um Tipo pelo nome")
        print("x. Sair")
        opcao = input("-Escolha uma opção: ")

        match opcao:
            case "1": cadastrar_tipo()
            case "2": registrar_personagem()
            case "3": info_personagem_id()
            case "4": editar_personagem()
            case "5": excluir_personagem()
            case "6": mostrar_personagens_do_tipo()
            case "7": mostrar_tipos()
            case "8": editar_tipo()
            case "9": excluir_tipo()
            case "x" | "X":
                salvar_dados();
                print("\n''Dados Salvos com sucesso!(..saindo..)''")
                break
            case _: print("\n''Opção inválida.''")

if __name__ == "__main__":
    main()
