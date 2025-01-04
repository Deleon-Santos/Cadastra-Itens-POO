import customtkinter as ctk
from tkinter import ttk
import Conexao_bd as bd

class Produto:
    def __init__(self, id, descricao, preco, qtd_cx):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.qtd_cx = qtd_cx

class Pedido:
    def __init__(self):
        self.listaPedido = []
        

    def adicionar(self, produto):
        #try:
           
        bd.criar_tabela(produto)   
        self.listaPedido.append(bd.ler_bd().copy())
        
          
        
class App:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Gerenciador de Produtos")
        self.pedido = Pedido()
        self.id_counter = 0

        # Configurações da interface
        self.frame = ctk.CTkFrame(janela)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label_descricao = ctk.CTkLabel(self.frame, text="Descrição do Produto",font=('helvetica', 10,'bold'))
        self.label_descricao.grid(row=0, column=0, padx=10, pady=0,sticky="w")
        self.entry_descricao = ctk.CTkEntry(self.frame, width=300)
        self.entry_descricao.grid(row=1, column=0, padx=10, pady=0)

        self.label_preco = ctk.CTkLabel(self.frame, text="Preço",font=('helvetica',10,'bold'))
        self.label_preco.grid(row=2, column=0, padx=10, pady=0,sticky='w')
        self.entry_preco = ctk.CTkEntry(self.frame)
        self.entry_preco.grid(row=3, column=0, padx=10, pady=0, sticky='w')

        self.label_qtd = ctk.CTkLabel(self.frame, text="Quantidade na Caixa",font=('helvetica',10, 'bold'))
        self.label_qtd.grid(row=2, column=1, padx=10, pady=0, sticky = 'w')
        self.entry_qtd = ctk.CTkEntry(self.frame)
        self.entry_qtd.grid(row=3, column=1, padx=10, pady=0, sticky= 'e')

        self.btn_adicionar = ctk.CTkButton(self.frame, text="Adicionar Produto", command=self.adicionar_produto)
        self.btn_adicionar.grid(row=4, column=0, columnspan=1, pady=10, padx=10 ,sticky='w')

        self.btn_listar = ctk.CTkButton(self.frame, text="Listar Produtos", command=self.exibir_tabela)
        self.btn_listar.grid(row=4, column=1, columnspan=1, pady=10)

        # Frame para tabela
        self.tabela_frame = ctk.CTkFrame(self.frame)
        self.tabela_frame.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")

        self.tabela = ttk.Treeview(self.tabela_frame, columns=("ID", "Descrição", "Preço", "Qtd/Caixa"), show="headings")
        self.tabela.heading("ID", text="ID")
        self.tabela.heading("Descrição", text="Descrição")
        self.tabela.heading("Preço", text="Preço")
        self.tabela.heading("Qtd/Caixa", text="Qtd/Caixa")

        self.tabela.column("ID", width=50, anchor="center")
        self.tabela.column("Descrição", width=150, anchor="center")
        self.tabela.column("Preço", width=100, anchor="center")
        self.tabela.column("Qtd/Caixa", width=100, anchor="center")

        self.tabela.pack(fill="both", expand=True)

    def adicionar_produto(self):
        descricao = self.entry_descricao.get()
        preco = self.entry_preco.get()
        qtd = self.entry_qtd.get()
        
        #conexao = self.conector()
        
        if descricao and preco and qtd:
            
            try:
                preco = float(preco)
                qtd = int(qtd)
                id = bd.pega_id()+1
                

                produto = Produto(id, descricao, preco, qtd)
                self.pedido.listaPedido.append(produto)

                self.limpar_campos()

            except ValueError:
                self.exibir_erro("Erro: Preço ou quantidade inválidos.")
        else:
            self.exibir_erro("Erro: Todos os campos devem ser preenchidos.")

    def exibir_tabela(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for produto in self.pedido.listaPedido:
            self.tabela.insert("", "end", values=(produto.id, produto.descricao, f"R${produto.preco:.2f}", produto.qtd_cx))

    def exibir_erro(self, mensagem):
        erro_popup = ctk.CTkToplevel(self.janela)
        erro_popup.title("Erro")
        ctk.CTkLabel(erro_popup, text=mensagem, padx=20, pady=20).pack()
        ctk.CTkButton(erro_popup, text="OK", command=erro_popup.destroy).pack(pady=10)

    def limpar_campos(self):
        self.entry_descricao.delete(0, "end")
        self.entry_preco.delete(0, "end")
        self.entry_qtd.delete(0, "end")

    
            
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    janela = ctk.CTk()
    app = App(janela)
    janela.mainloop()
#cd C:/Users/Leon/OneDrive/Área\ de\ Trabalho/Cadastra\ Itens\ POO
