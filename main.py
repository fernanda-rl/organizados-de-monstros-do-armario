# ORGANIZADOR DE MONSTROS DO ARMARIO

class Monstro:
    """
    Classe que representa um monstro.
    """
    def __init__(self, nome, idade, origem, nivelSusto):
        self.nome = nome
        self.idade = idade
        self.origem = origem
        self.nivelSusto = nivelSusto
    
    def definir_classificacao(self):
        if self.nivelSusto <= 3:
            return "Leve"
        elif self.nivelSusto <= 6:
            return "Médio"
        elif self.nivelSusto <= 9:
            return "Forte"
        else:
            return "Pânico"

class ElementoMonstro:
    """
    Classe que representa um elemento da lista de monstros.
    Cada elemento contém um monstro e uma referência para o próximo elemento.
    """
    def __init__(self, monstro):
        self.monstro = monstro  # Objeto da classe Monstro
        self.proximo = None  # Ponteiro para o próximo elemento da lista

class ListaLinear:
    def __init__(self):
        self.inicio = None  # Inicializa a lista como vazia
        self.tamanho = 0  # Define o tamanho inicial como zero
        
    def adicionar_monstro(self, nome, idade, origem, nivelSusto):
        """
        Adiciona um novo monstro ao final da lista.
        """
        novo_monstro = Monstro(nome, idade, origem, nivelSusto)  # Cria o objeto Monstro
        novo_elemento = ElementoMonstro(novo_monstro)  # Cria um elemento dentro da lista armário
        
        if self.inicio is None:
            # Se a lista estiver vazia, o novo monstro será o primeiro
            self.inicio = novo_elemento
        else:
            # Percorre até o final da lista para adicionar o novo monstro
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_elemento
        
        self.tamanho += 1  # Incrementa o tamanho da lista
        print(f"Monstro {nome} adicionado ao armário!")
        
        # Exibir os monstros adicionados, isso é apenas um TESTE para ver se estava inserindo!!!!
        #atual = self.inicio
        #print("\nLista de monstros no armário:")
        #while atual is not None:
        #    monstro = atual.monstro
        #    print(f"Nome: {monstro.nome}, Idade: {monstro.idade}, Origem: {monstro.origem}, Nível de Susto: {monstro.nivelSusto}")
        #    atual = atual.proximo
        
        
    def remover_monstro(self, nome):
        print("Inserir Função")
        """
        Essa função deve procurar na lista o monstro com o nome informado.
        Se encontrar, pergunta se tem certeza que quer remover, arruma o menu,
        atualiza a lista depois de remover e, se não achar o monstro, exibe uma mensagem de erro.
        """
        
    def buscar_por_monstro(self, nivelSusto):
        print("Inserir Função")
        """
        Percorre toda a lista e exibe os monstros com o nível igual ao informado.
        Caso não tenha nenhum monstro com esse nível, informa que não tem.
        """
        
    def ordenar_por_susto(self):
        print("Inserir Função")
        """
        Organiza os monstros na lista do maior para o menor nível de susto.
        Não sei se pode usar o Quick Sort ou Bubble Sort para reorganizar os monstros.
        Quando ordenar, exibir uma mensagem indicando que a organização foi concluída.
        """
        
    def exibir_monstros(self):
        print("Inserir Função")
        # Exibe todos os monstros na lista

armario = ListaLinear()

while True:
    print("\n1. Adicionar Monstro")
    print("2. Remover Monstro")
    print("3. Buscar por nível de susto")
    print("4. Ordenar por susto")
    print("5. Exibir Monstros")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do monstro: ")
        idade = int(input("Idade do monstro: "))
        origem = input("Origem do monstro: ")
        susto = int(input("Nível de susto (1 a 10): "))
        armario.adicionar_monstro(nome, idade, origem, susto)

    elif opcao == "2":
        nome = input("Nome do monstro a remover: ")
        # Arrumar aqui pra perguntar se tem certeza
        armario.remover_monstro(nome)
    elif opcao == "3":
        susto = int(input("Nível de susto para buscar: "))
        armario.buscar_por_susto(susto)
    elif opcao == "4":
        armario.ordenar_por_susto()
    elif opcao == "5":
        armario.exibir_monstros()
    elif opcao == "6":
        break
    else:
        print("Opção inválida!")

