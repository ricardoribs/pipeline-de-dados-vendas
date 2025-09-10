# streamlit_app/dashboard.py (VERSÃO FINAL E CORRIGIDA)

import streamlit as st
import pandas as pd
import sqlite3 # Importamos a biblioteca nativa do SQLite
import os

def carregar_dados():
    """Carrega os dados transformados pelo dbt usando uma conexão direta."""
    try:
        # Caminho para o banco de dados
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_path = os.path.join(base_dir, 'vendas.db')
        
        # A CORREÇÃO ESTÁ AQUI: Usamos sqlite3.connect() em vez de create_engine()
        conn = sqlite3.connect(db_path)

        # Carregamos os dados da view criada pelo dbt
        query = "SELECT * FROM faturamento_por_estado"
        df = pd.read_sql_query(query, conn)
        
        # Fechamos a conexão
        conn.close()
        return df
        
    except Exception as e:
        # Mostra um erro mais detalhado no dashboard
        st.error(f"Erro ao carregar os dados do banco: {e}")
        st.error("Verifique se o arquivo 'vendas.db' existe e se o pipeline ('python run_pipeline.py') foi executado com sucesso.")
        return pd.DataFrame() # Retorna um dataframe vazio em caso de erro

# --- Configuração da Página ---
st.set_page_config(layout="wide")
st.title("📊 Dashboard de Vendas")
st.markdown("---")

# --- Carregar e Exibir os Dados ---
df_faturamento = carregar_dados()

if not df_faturamento.empty:
    st.header("Faturamento Total por Estado")

    # Mostrando o gráfico de barras
    st.bar_chart(df_faturamento.set_index('estado_cliente'))

    # Mostrando a tabela de dados
    with st.expander("Ver dados detalhados"):
        st.dataframe(df_faturamento)
else:
    st.warning("Nenhum dado encontrado para exibir. Execute o pipeline com 'python run_pipeline.py' e tente novamente.")