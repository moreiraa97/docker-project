import psycopg2

try:
    # Conectar ao banco de dados PostgreSQL
    conn = psycopg2.connect(
        user="postgres",
        password="bd123",
        host="localhost",
        port="5440",
        database="master"
    )

    # Abrir um cursor para executar comandos SQL
    cur = conn.cursor()

    print('Digite qual email você quer excluir [lembre de adicionar o %]:')
    mensagem = input(str())

    # Comando SQL para deletar dados de uma tabela
    query = f"DELETE FROM usuarios WHERE email ilike '{mensagem}'"

    # Executar o comando SQL
    cur.execute(query)

    # Commit da transação para efetivar a deleção
    conn.commit()

    print("Deleção realizada com sucesso!")

except psycopg2.Error as e:
    print("Erro ao deletar os dados:", e)

finally:
    # Fechar o cursor e a conexão com o banco de dados
    if cur:
        cur.close()
    if conn:
        conn.close()