class Produto:
    def __init__(self, id, descricao, preco, qtd_cx):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.qtd_cx = qtd_cx

    def mostra_item(self):
        print(f"Foi adicionado o produto {self.id}: {self.descricao}, Preço: R${self.preco:.2f}, Quantidade por caixa: {self.qtd_cx}")

class Pedido:
    def __init__(self):
        self.listaPedido = []

    def adicionar(self, produto):
        self.listaPedido.append(produto)

    def listar_itens(self):
        for pro in self.listaPedido:
            pro.mostra_item()


adicionar = Pedido()
id = 0

while True:
    id += 1
    descricao = input('Insira a descrição do produto desejado: ')
    preco = float(input('Informe o preço do produto: '))
    qtd = int(input('Informe a quantidade na caixa do item: '))

    produto = Produto(id, descricao, preco, qtd)

    adicionar.adicionar(produto)

    continuar = input("Deseja continuar cadastrando? (1-Sim / 2-Não): ")
    if continuar == '2':
        break
    elif continuar != '1':
        print("Escolha inválida. Considerando como 'Não'.")
        break

print("\nProdutos cadastrados:")
adicionar.listar_itens()
