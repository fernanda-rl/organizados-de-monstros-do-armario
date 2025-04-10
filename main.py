# ORGANIZADOR DE MONSTROS DO ARMARIO

class Monstro:
    def __init__(self, nome, idade, origem, susto):
        self.nome = nome
        self.idade = idade
        self.origem = origem
        self.susto = susto

class ElementoMonstro:
    """
    Classe que constroi a lista encadeada
    Cada monstro está ligado com o próximo, pelo .proximo
    """
    def __init__(self, monstro):
        self.monstro = monstro  # Objeto da classe Monstro
        self.proximo = None  # Ponteiro para o próximo elemento da lista

class ListaLinear:
    def __init__(self):
        self.inicio = None  # Inicializa a lista como vazia, apontando para o primeiro monstro
        self.tamanho = 0  # Define o tamanho inicial como zero
        
    def adicionar_monstro(self, nome, idade, origem, susto): 
        # Adiciona um novo monstro ao final da lista.
        novo_monstro = Monstro(nome, idade, origem, susto)  # Cria o objeto Monstro
        novo_elemento = ElementoMonstro(novo_monstro)  # Cria um elemento dentro da lista armário
        
        if self.inicio is None:
            # Se a lista estiver vazia, o novo monstro será o primeiro
            self.inicio = novo_elemento
        else:
            # Percorre até o final da lista para adicionar o novo monstro
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_elemento # Adiciona o novo elemento ao final da lista
        
        self.tamanho += 1  # Incrementa o tamanho da lista
        print(f"\nMonstro {nome} adicionado ao armário!")
        
    def alterar_monstro(self, nome): #altera atributos do monstro
        atual = self.inicio

        while atual is not None and atual.monstro.nome != nome:
            atual = atual.proximo

        if atual is None:
            print("\nMonstro não encontrado.")
            return

        monstro = atual.monstro
        print(f"\nMonstro encontrado! Dados atuais:")
        print(f"Nome: {monstro.nome}")
        print(f"Idade: {monstro.idade}")
        print(f"Origem: {monstro.origem}")
        print(f"Nível de susto: {monstro.susto}")

        print("\nDigite o novo valor ou aperte Enter para manter o mesmo:")

        novo_nome = input("Novo nome: ")
        if novo_nome != "":
            monstro.nome = novo_nome

        nova_idade = input("Nova idade: ")
        if nova_idade != "":
            monstro.idade = int(nova_idade)

        nova_origem = input("Nova origem: ")
        if nova_origem != "":
            monstro.origem = nova_origem

        novo_susto = input("Novo nível de susto (1 a 10): ")
        if novo_susto != "":
            monstro.susto = int(novo_susto)

        print("\nMonstro atualizado com sucesso!")

    def remover_monstro(self, nome): 
        """
        Essa função deve procurar na lista o monstro com o nome informado
        se encontrar, pergunta se tem certeza se quer remover, e se não achar o monstro mensagem de erro
        """ 
        atual = self.inicio
        
        # Procura o monstro na lista
        while atual is not None and atual.monstro.nome != nome:
            atual = atual.proximo
        
        if atual == None:
                print("\nVerifique se digitou o nome corretamente.")
                return

        # Para confirmar se quer realmente excluir o monstro
        confirmacao = input(f"Tem certeza que deseja excluir {atual.monstro.nome} da lista? (s/n)\n")
        if confirmacao != "s" and confirmacao != "S":
            print("Exclusão cancelada.")
            return
        
        # Para guardar o monstro para excluir ele
        monstro_para_excluir = atual.monstro
        novo_prox = atual.proximo
        atual = self.inicio
        
        if atual.monstro is monstro_para_excluir:
            self.inicio = atual.proximo
            del monstro_para_excluir
            self.tamanho -= 1
            print("\nMonstro excluido com sucesso.")
            return
        
        # Caso o monstro esteja no meio ou fim da lista
        while atual.proximo is not None and atual.proximo.monstro is not monstro_para_excluir:
            atual = atual.proximo

        if atual.proximo is not None:
            atual.proximo = novo_prox
            del monstro_para_excluir
            self.tamanho -= 1
            print("\nMonstro excluido com sucesso.")
        else:
            print("Monstro não encontrado.")

    def buscar_por_monstro(self, susto):
        atual = self.inicio
        encontrou = False
        print(f"\nMonstros com nível de susto {susto}:")
        while atual is not None:
            if atual.monstro.susto == susto:
                print(f"Nome: {atual.monstro.nome}, Idade: {atual.monstro.idade}, Origem: {atual.monstro.origem}")
                encontrou = True
            atual = atual.proximo
        if not encontrou:
            print("Nenhum monstro encontrado com esse nível de susto.")
        
    def ordenar_por_susto(self):
        if self.inicio is None or self.inicio.proximo is None:
            return

        def funcao_recursiva(no):
            if no is None or no.proximo is None:
                return False
            trocou = False
            if no.monstro.susto > no.proximo.monstro.susto:
                no.monstro, no.proximo.monstro = no.proximo.monstro, no.monstro
                trocou = True
            if funcao_recursiva(no.proximo):
                trocou = True
            return trocou

        while funcao_recursiva(self.inicio):
            pass

        print("\nOrganização por susto concluída!")
        self.exibir_monstros()
        
    def exibir_monstros(self):
        atual = self.inicio
        print("\nLista de monstros no armário:")
        while atual is not None:
            monstro = atual.monstro
            print(f"Nome: {monstro.nome}, Idade: {monstro.idade}, Origem: {monstro.origem}, Nível de Susto: {monstro.susto}")
            atual = atual.proximo

armario = ListaLinear()

# Inserção direta sem exibir mensagens
monstros_padrao = [
    ("Vampiro", 200, "Pensilvania", 3),
    ("Pé Grande", 33, "EUA", 6),
    ("Enaldinho", 20, "Brasil", 8),
    ("Dracula", 800, "Transilvania", 10),
    ("Lobisomem adolescente", 16, "EUA", 5)
]

for nome, idade, origem, susto in monstros_padrao:
    novo = ElementoMonstro(Monstro(nome, idade, origem, susto))
    if armario.inicio is None:
        armario.inicio = novo
    else:
        atual = armario.inicio
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo
    armario.tamanho += 1

while True:
    print("\n1. Adicionar Monstro")
    print("2. Remover Monstro")
    print("3. Buscar por nível de susto")
    print("4. Ordenar por susto")
    print("5. Exibir Monstros")
    print("6. Alterar Monstro")
    print("7. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do monstro: ")
        idade = int(input("Idade do monstro: "))
        origem = input("Origem do monstro: ")
        susto = int(input("Nível de susto (1 a 10): "))
        armario.adicionar_monstro(nome, idade, origem, susto)

    elif opcao == "2":
        nome = input("\nDigite o nome do monstro que deseja excluir: ")
        armario.remover_monstro(nome)

    elif opcao == "3":
        susto = int(input("Nível de susto para buscar: "))
        armario.buscar_por_monstro(susto)

    elif opcao == "4":
        armario.ordenar_por_susto()

    elif opcao == "5":
        armario.exibir_monstros()

    elif opcao == "6":
        nome = input("\nDigite o nome do monstro que deseja alterar: ")
        armario.alterar_monstro(nome)

    elif opcao == "7":
        break
    else:
        print("Opção inválida!")
