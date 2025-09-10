# scripts/ingestao.py (VERSÃO FINAL)
import pandas as pd
import sqlite3
import os

def carregar_dados_do_csv():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'data', 'vendas_exemplo.csv')
    db_path = os.path.join(base_dir, 'vendas.db')
    
    # Lendo o CSV. Removemos o 'decimal=',' pois seu arquivo usa '.' que é o padrão.
    df = pd.read_csv(csv_path, sep=';')
    print("CSV lido com sucesso!")

    conn = sqlite3.connect(db_path)
    df.to_sql('vendas', conn, if_exists='replace', index=False)
    print("Dados carregados com sucesso na tabela 'vendas'!")
    conn.close()

if __name__ == "__main__":
    carregar_dados_do_csv()