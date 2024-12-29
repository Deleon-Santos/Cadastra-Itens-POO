import sqlite3 as bd

def conectar_bd(produto):
    conn=bd.connect("cadastra_bd")#cria o bd com nome valquiria
    curs=conn.cursor()
    
    curs.execute("""
                    create table if not exists cadastro(
                        id integer primary key,    
                        nome text,
                        valor real,
                        qtd real)""")
    curs.execute("""
                        insert into cadastro(
                        id, nome, valor, qtd)
                        values(?,?,?,?)""",(produto.id,produto.descricao,produto.preco,produto.qtd_cx) )
    conn.commit()
    print('gravadoo em vendas')
    
    conn.close()
    return
    
def ler_bd():
    conn=bd.connect("cadastra_bd")#cria o bd com nome valquiria
    curs=conn.cursor()
    curs.execute("""
                    select id, nome, valoe,qtd from cadastro 
""")
    produto = curs.fetchall()
    conn.close()
    return produto
    
    