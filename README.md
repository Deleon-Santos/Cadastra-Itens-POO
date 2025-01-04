## Gerenciador de Produtos em Python
![Descrição da imagem].(POO.png)
### Descrição
Este projeto Python cria uma aplicação desktop simples para gerenciar um cadastro de produtos. A interface gráfica é desenvolvida utilizando a biblioteca CustomTkinter, facilitando a criação de interfaces modernas e personalizadas. A persistência dos dados é realizada através de um banco de dados (implementação específica no módulo `Conexao_bd`).

### Tecnologias Utilizadas
* **Python:** Linguagem de programação principal.   
* **CustomTkinter:** Biblioteca Python para criação de interfaces gráficas.   
* **Tkinter:** Biblioteca padrão do Python para criar interfaces gráficas.  
* **SQL (através de Conexao_bd):** Linguagem de consulta para interagir com o banco de dados.

### Estrutura do Projeto
* **Produto:** Classe que representa um produto com seus atributos (ID, descrição, preço, quantidade).
* **Pedido:** Classe que representa um pedido, contendo uma lista de produtos.
* **App:** Classe principal que cria a interface gráfica e gerencia as interações do usuário.
* **Conexao_bd:** Módulo responsável pela conexão com o banco de dados e as operações de CRUD.

