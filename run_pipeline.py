# run_pipeline.py

import os
import subprocess

# --- Configuração ---
# Caminho para a pasta do projeto dbt
dbt_project_dir = os.path.join(os.getcwd(), 'dbt_project')

def run_step(command, step_name):
    """Função para executar um comando no terminal e verificar se houve erro."""
    print(f"--- Iniciando Etapa: {step_name} ---")
    try:
        # Usamos o subprocess para ter mais controle e capturar a saída
        process = subprocess.run(command, check=True, shell=True, text=True, capture_output=True)
        print(process.stdout)
        print(f"--- Etapa Concluída com Sucesso: {step_name} ---")
        return True
    except subprocess.CalledProcessError as e:
        print(f"### ERRO na Etapa: {step_name} ###")
        print(f"Comando que falhou: {e.cmd}")
        print(f"Saída do erro:\n{e.stderr}")
        return False

def main():
    """Função principal que orquestra o pipeline."""
    print(">>> Iniciando o Pipeline de Dados de Vendas <<<")

    # Etapa 1: Ingestão de Dados (Executa o script Python)
    # Usamos 'python' para garantir que o interpretador do venv seja usado
    ingestion_command = "python scripts/ingestao.py"
    if not run_step(ingestion_command, "Ingestão de Dados do CSV"):
        print("Pipeline interrompido devido a erro na ingestão.")
        return

    # Etapa 2: Transformação com dbt (Executa o comando dbt run)
    # Navegamos para o diretório do dbt e executamos o 'dbt run'
    dbt_command = f"cd {dbt_project_dir} && dbt run"
    if not run_step(dbt_command, "Transformação com dbt"):
        print("Pipeline interrompido devido a erro na transformação com dbt.")
        return

    print(">>> Pipeline de Dados de Vendas concluído com sucesso! <<<")
    print("\nPara visualizar os resultados, execute o dashboard com o comando:")
    print("streamlit run streamlit_app/dashboard.py")


if __name__ == "__main__":
    main()