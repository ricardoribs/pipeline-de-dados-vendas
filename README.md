# 🚀 Projeto de Pipeline de Dados de Vendas

Este projeto demonstra a construção de um pipeline de dados completo, desde a ingestão de dados de um arquivo CSV até a visualização em um dashboard interativo. É um exemplo prático de um fluxo de trabalho de ETL (Extract, Transform, Load) utilizando ferramentas modernas de engenharia de dados.

## 📊 Dashboard Final

https://imgur.com/a/HNYuVSH
---

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal para scripts de ingestão e orquestração.
* **Pandas:** Para manipulação e leitura de dados do arquivo CSV.
* **SQLite:** Banco de dados relacional leve para armazenamento dos dados.
* **dbt (Data Build Tool):** Para a etapa de transformação dos dados (T), aplicando as regras de negócio via SQL.
* **Streamlit:** Para a criação do dashboard interativo de visualização dos resultados.
* **Orquestração:** Um script Python (`run_pipeline.py`) controla o fluxo de execução das etapas de ingestão e transformação.

---

## ⚙️ Como Executar o Projeto

**Pré-requisitos:**
* Python 3.11

**1. Clone o Repositório**
```bash
git clone [https://github.com/ricardoribs/pipeline-de-dados-vendas.git](https://github.com/ricardoribs/pipeline-de-dados-vendas.git)
cd pipeline-de-dados-vendas
```

**2. Crie e Ative o Ambiente Virtual**
```bash
# Crie o ambiente
py -3.11 -m venv venv

# Ative o ambiente (Windows)
.\venv\Scripts\activate
```

**3. Instale as Dependências**
```bash
pip install pandas dbt-core dbt-sqlite streamlit SQLAlchemy==1.4.46
```

**4. Execute o Pipeline de Dados**
Este comando executa a ingestão do CSV para o SQLite e a transformação com dbt.
```bash
python run_pipeline.py
```

**5. Visualize o Dashboard**
Após a execução do pipeline, inicie o dashboard com o comando:
```bash
streamlit run streamlit_app/dashboard.py
```
O dashboard estará disponível em seu navegador.

---

## 📂 Estrutura do Projeto
```
pipeline-de-dados-vendas/
|
├── data/
│   └── vendas_exemplo.csv      # Dados brutos
|
├── dbt_project/                # Projeto de transformação com dbt
│   └── models/
│       ├── faturamento_por_estado.sql
│       └── sources.yml
|
├── streamlit_app/
│   └── dashboard.py            # Script do dashboard
|
└── scripts/
│   └── ingestao.py             # Script para carregar dados no banco
|
└── run_pipeline.py             # Script orquestrador principal
```
