# ORGANIZADOR DE MONSTROS DO ARMARIO

class Monstro:
    """
    self em é a referência à própria instância
    da classe, vamos usalo para acessar atributos
    e metodos dentro da classe
    ex: self.nome = nome, armazena o nome do
    monstro na instância
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
        
class ListaLinear:
    def __init__(self):
        print("Inserir Função")
        
    def adicionar_monstro(self, nome, idade, origem, nivelSusto):
        print("Inserir Função")
        """
        essa função deve armazenar os monstros na estrutura de lista linear, como o prof pediu
        deve verificar se ainda há espaço para adicionar o monstro
        incrementa o tamanho da lista
        as duas ultimas o python faz automatico, porém ele frizou em aula que é importante entendermos essa teoria
        """
        
    def remover_monstro(self, nome):
        print("Inserir Função")
        """
        esse função deve procurar na lista o monstro com o nome informado
        se encontrar, pergunta se tem certeza q quer remover, arrumar o menu
        atualizar a lista dps de remover
        e se não achar o monstro msg de erro
        """
        
    def buscar_por_monstro(self, nivelSusto):
        print("Inserir Função")
        """
        olhar toda a lista e exibir os monstros com o nível igual ao informado
        caso não tenha nenhum monstro com esse nível, informa que nn tem
        """
        
    def ordenar_por_susto(self):
        print("Inserir Função")
        """
        organizar os monstros na lista do maior para o menor nível de susto
        nn sei se pode usar o Quick Sort ou Bubble Sort, para reorganizar os monstros
        quando ordenar exibir uma mensagem indicando que a organização foi concluída
        """
        
    def exibir_monstros(self):
        print("Inserir Função")
        # exibe tudo

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
        armario.adicionar_monstro(nome, susto)
    elif opcao == "2":
        nome = input("Nome do monstro a remover: ")
        #arrumar aqui pra perguntar se tem certeza
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
