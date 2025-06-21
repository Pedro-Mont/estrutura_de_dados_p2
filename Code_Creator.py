import json
import os
from collections import deque


stack_ultimos_personagens = []

# (Dados principais)
tipos = {}

# Definição do nó (Node) para a lista encadeada
class PersonagemNode:
    def __init__(self, dados):
        self.dados = dados  # dicionário de informações
        self.next = None

# Início da lista encadeada (cabeça)
personagem_head = None

print("\n |[CHARACTER CREATOR]|")

CAMINHO_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Json_Creator.json")

# Função para salvar dados em JSON
def salvar_dados():
    lista_personagens = []
    atual = personagem_head
    while atual:
        lista_personagens.append(atual.dados)
        atual = atual.next

    with open(CAMINHO_JSON, "w", encoding="utf-8") as f:
        json.dump({"tipos": {k: list(v) for k, v in tipos.items()}, "grupo_personagem": lista_personagens}, f, ensure_ascii=False, indent=4)

# Função para carregar dados do JSON
def carregar_dados():
    global tipos, personagem_head
    if os.path.exists(CAMINHO_JSON):
        with open(CAMINHO_JSON, "r", encoding="utf-8") as f:
            dados = json.load(f)
            tipos.update({k: set(v) for k, v in dados.get("tipos", {}).items()})
            lista_personagens = dados.get("grupo_personagem", [])
            anterior = None
            for p in lista_personagens:
                novo_node = PersonagemNode(p)
                if not personagem_head:
                    personagem_head = novo_node
                else:
                    anterior.next = novo_node
                anterior = novo_node

carregar_dados()

# Função para cadastrar tipo
def cadastrar_tipo():
    nome = input("Digite o nome do tipo: ").strip().title()
    if not nome:
        print("\n''Tipo não pode ser vazio.''")
        return
    if nome in tipos:
        print("\n''Tipo já cadastrado.''")
    else:
        tipos[nome] = set()
        print(f"\n''Tipo ({nome}) cadastrado com sucesso!''")

# Função para registrar personagem
def registrar_personagem():
    global personagem_head
    if not tipos:
        print("\n''Não é possível cadastrar personagem pois não há um Tipo.''")
        return

    registro_id = input("Informe o ID do personagem: ").strip()
    if not registro_id:
        print("\n''ID não informado.''")
        return

    atual = personagem_head
    while atual:
        if atual.dados["ID"] == registro_id:
            print("\n''ID já existente.''")
            return
        atual = atual.next

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

    novo_node = PersonagemNode(personagem)
    if not personagem_head:
        personagem_head = novo_node
    else:
        atual = personagem_head
        while atual.next:
            atual = atual.next
        atual.next = novo_node

    tipos[tipo].add(nome)
    stack_ultimos_personagens.append(personagem)
    print("\n''Personagem cadastrado com sucesso!''")

# Função para exibir informações do personagem pelo ID
def info_personagem_id():
    if not personagem_head:
        print("\n''Nenhum personagem cadastrado.''")
        return

    id_busca = input("Digite o ID do personagem: ")
    atual = personagem_head
    while atual:
        if atual.dados["ID"] == id_busca:
            print("\n- Personagem encontrado:")
            dados_tupla = tuple(atual.dados.items())
            maior_chave = max(len(k) for k, _ in dados_tupla)
            for chave, valor in dados_tupla:
                print(f"{(chave + ':').ljust(maior_chave + 1)} {valor}")
            return
        atual = atual.next
    print("\n''Personagem não encontrado.''")

# Função para editar personagem
def editar_personagem():
    if not personagem_head:
        print("\n''Nenhum personagem cadastrado.''")
        return

    id_atual = input("Digite o ID do personagem a editar: ")
    atual = personagem_head
    while atual:
        if atual.dados["ID"] == id_atual:
            novo_id = input("Novo ID: ").strip() or atual.dados["ID"]
            if not novo_id:
                print("\n''ID não informado.''")
                return

            # Verifica se novo_id já existe
            checar = personagem_head
            while checar:
                if checar.dados["ID"] == novo_id and checar != atual:
                    print("\n''ID já existente.''")
                    return
                checar = checar.next

            novo_tipo = input("Novo Tipo: ").strip().title() or atual.dados["Tipo"]
            if novo_tipo not in tipos:
                print("\n''Tipo não existe.''")
                return

            atual.dados["ID"]       = novo_id
            atual.dados["Tipo"]     = novo_tipo
            atual.dados["Nome"]     = input("Novo Nome: ").strip().title() or "[-Desconhecido-]"
            atual.dados["Codinome"] = input("Novo Codinome: ").strip().title() or "[-Desconhecido-]"
            atual.dados["Poder"]    = input("Novo Poder: ").strip().capitalize() or "[-Desconhecido-]"
            atual.dados["Idade"]    = input("Nova Idade: ").strip() or "[-Desconhecido-]"
            atual.dados["Gênero"]   = input("Novo Gênero (M/F): ").strip().upper() or "[-Desconhecido-]"
            atual.dados["Origem"]   = input("Nova Origem: ").strip().capitalize() or "[-Desconhecido-]"

            print("\n''Personagem editado com sucesso!''")
            return
        atual = atual.next
    print("\n''Personagem não encontrado.''")

# Função para excluir personagem
def excluir_personagem():
    global personagem_head
    if not personagem_head:
        print("\n''Nenhum personagem cadastrado.''")
        return

    id_excluir = input("Digite o ID do personagem a excluir: ")

    atual = personagem_head
    anterior = None
    while atual:
        if atual.dados["ID"] == id_excluir:
            if anterior:
                anterior.next = atual.next
            else:
                personagem_head = atual.next
            tipos[atual.dados["Tipo"]].remove(atual.dados["Nome"])
            print(f"\nPersonagem ({atual.dados['Nome'].title()}/{atual.dados['Codinome'].title()}) excluído com sucesso!")
            return
        anterior = atual
        atual = atual.next
    print("\n''Personagem não encontrado.''")

# Função para mostrar personagens do tipo
def mostrar_personagens_do_tipo():
    if not personagem_head:
        print("\n''Nenhum personagem cadastrado.''")
        return

    tipo = input("Digite o nome do tipo: ").strip().title()
    if tipo not in tipos:
        print("\n''Tipo não encontrado.''")
        return

    atual = personagem_head
    encontrados = []
    while atual:
        if atual.dados["Tipo"] == tipo:
            encontrados.append(atual.dados)
        atual = atual.next

    if not encontrados:
        print("\n''Nenhum personagem desse tipo.''")
        return

    print(f"\nPersonagens do tipo ({tipo}):")
    for p in encontrados:
        print(f'({p["ID"]}): {p["Codinome"]}')


def mostrar_tipos():
    if not tipos:
        print("\n''Tipo não cadastrado ainda.''")
        return
    
    print("\nTipos cadastrados:")
    for t in tipos:
        print(f"- ({t})")


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
    atual = personagem_head
    while atual:
        if atual.dados["Tipo"] == tipo_atual:
            atual.dados["Tipo"] = novo_tipo
        atual = atual.next
    print("\n''Tipo editado com sucesso.''")

def excluir_tipo():
    global personagem_head
    if not tipos:
        print("\n''Nenhum tipo cadastrado.''")
        return
    tipo = input("Digite o nome do tipo a excluir: ").strip().title()
    if tipo not in tipos:
        print("\n''Tipo não encontrado.''")
        return
    # Remove todos os personagens desse tipo
    atual = personagem_head
    anterior = None
    while atual:
        if atual.dados["Tipo"] == tipo:
            if anterior:
                anterior.next = atual.next
            else:
                personagem_head = atual.next
            atual = anterior.next if anterior else personagem_head
        else:
            anterior = atual
            atual = atual.next
    del tipos[tipo]
    print(f"\n''Tipo ({tipo}) excluído com sucesso!''")

# (Fila de Recrutamento)
fila_missão = deque()

#Funçõe de adicionar na fila, mostrar a fila e recrutar pesonagem
def adicionar_na_fila():
    if not personagem_head:
        print("\n''Nenhum personagem cadastrado.''")
        return

    id_personagem = input("Informe o ID do personagem a recrutar para missão: ").strip()
    atual = personagem_head
    while atual:
        if atual.dados["ID"] == id_personagem:
            fila_missão.append(atual.dados)
            print(f"\nPersonagem ({atual.dados['Codinome']}) adicionado à missão.")
            return
        atual = atual.next
    print("\n''Personagem não encontrado.''")

def mostrar_fila():
    if not fila_missão:
        print("\n''A fila de personagens na missão está vazia.''")
        return
    print("\nPersonagens em missão:")
    for i, p in enumerate(fila_missão, 1):
        print(f"{i}. {p['Codinome']} ({p['Tipo']})")

def chamar_primeiro_enviado():
    if not fila_missão:
        print("\n''Fila vazia. Nenhum personagem em missão.''")
        return
    personagem = fila_missão.popleft()
    print(f"\nPersonagem ({personagem['Codinome']}) foi chamado de volta com sucesso!")


#Função com pilha
def mostrar_ultimos_personagens():
    if not stack_ultimos_personagens:
        print("\n''Nenhum personagem cadastrado ainda.''")
        return

    print("\nÚltimos personagens cadastrados (mais recente primeiro):")
    for i, p in enumerate(reversed(stack_ultimos_personagens[-5:]), 1): 
        print(f"{i}. {p['Codinome']} ({p['Tipo']}) - ID: {p['ID']}")


# Função principal
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
        print("10. Adicionar Personagem em uma Missão")
        print("11. Mostrar Personagens em missão")
        print("12. Chamar Primeiro enviado")
        print("13. Mostrar últimos personagens cadastrados")
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
            case "10": adicionar_na_fila()
            case "11": mostrar_fila()
            case "12": chamar_primeiro_enviado()
            case "13": mostrar_ultimos_personagens()
            case "x" | "X":
                salvar_dados()
                print("\n''Dados Salvos com sucesso!(..saindo..)''")
                break
            case _: print("\n''Opção inválida.''")


if __name__ == "__main__":
    main()


