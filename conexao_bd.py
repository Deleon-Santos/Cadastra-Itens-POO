import sqlite3 as bd

def conectar_bd():
    conn=bd.connect("cadastra_bd")#cria o bd com nome valquiria
    return conn
    
def criar_tabela(produto):
    conn=conectar_bd()
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
    conn=conectar_bd()
    curs=conn.cursor()
    
    curs.execute("""
                    select id, nome, valor,qtd from cadastro 
""")
    produto = curs.fetchall()
    conn.close()
    return produto

def pega_id():
    conn=conectar_bd()
    curs=conn.cursor()
    try:
        curs.execute("""
                        select COUNT(*) id from cadastro 
        """)
        id = curs.fetchone()
        print(id)
        conn.close()
        return id[0]
    except:
        id=1
    finally:
        conn.close()    
    return id