# debug_data.py

import pandas as pd
import sqlite3
import os

def run_debug():
    """Executa uma verificação passo a passo dos dados no pipeline."""
    
    base_dir = os.getcwd()
    csv_path = os.path.join(base_dir, 'data', 'vendas_exemplo.csv')
    db_path = os.path.join(base_dir, 'vendas.db')

    print("--- 1. ANÁLISE DO ARQUIVO CSV ---")
    try:
        df_csv = pd.read_csv(csv_path, sep=';', decimal=',')
        print("CSV lido com sucesso.")
        print("Tipos de dados das colunas lidas do CSV:")
        print(df_csv.dtypes)
        print("\nAmostra da coluna 'preco_produto' no CSV:")
        print(df_csv['preco_produto'].head())
        print("-" * 35)
    except Exception as e:
        print(f"ERRO ao ler o CSV: {e}")
        return

    print("\n--- 2. ANÁLISE DA TABELA 'vendas' NO BANCO DE DADOS (APÓS INGESTÃO) ---")
    if not os.path.exists(db_path):
        print("ERRO: O arquivo de banco de dados 'vendas.db' não foi encontrado.")
        print("Por favor, execute 'python run_pipeline.py' primeiro.")
        return
        
    try:
        conn = sqlite3.connect(db_path)
        df_db_raw = pd.read_sql_query("SELECT * FROM vendas", conn)
        print("Tabela 'vendas' lida do banco com sucesso.")
        print("Tipos de dados das colunas na tabela 'vendas':")
        print(df_db_raw.dtypes)
        print("\nAmostra da coluna 'preco_produto' no banco de dados:")
        print(df_db_raw['preco_produto'].head())
        print("-" * 35)
    except Exception as e:
        print(f"ERRO ao ler a tabela 'vendas': {e}")
        conn.close()
        return

    print("\n--- 3. ANÁLISE DA VIEW 'faturamento_por_estado' (APÓS DBT) ---")
    try:
        df_dbt = pd.read_sql_query("SELECT * FROM faturamento_por_estado", conn)
        print("View 'faturamento_por_estado' lida do banco com sucesso.")
        if df_dbt.empty:
            print("ATENÇÃO: A view 'faturamento_por_estado' está VAZIA.")
        else:
            print("Conteúdo da view 'faturamento_por_estado':")
            print(df_dbt)
        print("-" * 35)
    except Exception as e:
        print(f"ERRO ao ler a view 'faturamento_por_estado': {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    run_debug()