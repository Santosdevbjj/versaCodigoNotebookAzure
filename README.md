### Controle e Versionamento de Código no Notebook da Azure

![Azure_Databricks01](https://github.com/user-attachments/assets/d30d3cd1-7b30-4247-8f19-a9d9941c9c8b) 


**Bootcamp Microsoft AI for Tech - Azure Databricks** 

---

**DESCRIÇÃO:**

Este projeto demonstra como utilizar o Azure Databricks para versionamento e organização de notebooks em ambientes de dados.

A proposta inclui a criação de clusters, importação de arquivos, execução de notebooks com auxílio de inteligência artificial, além da integração com Azure DevOps para controle de código e automação de esteiras de CI/CD.

É apresentado o uso prático da IA integrada ao Databricks para geração de código em Python e Spark, facilitando a criação de notebooks interativos com filtros, sumarizações, visualizações e comentários explicativos.

Também são exploradas boas práticas de organização, exportação e reaproveitamento de notebooks, bem como o uso de recursos do Microsoft Learn, que oferecem exercícios guiados e roteiros de aprendizado.

A abordagem permite trabalhar de forma colaborativa, segura e com versionamento estruturado em ambientes de análise, engenharia de dados e machine learning dentro da plataforma Azure.


---


📘 **Projeto VersaCódigo Notebook Azure + Databricks**

Este repositório contém um pipeline completo de engenharia de dados utilizando Azure Databricks, PySpark, CI/CD com GitHub Actions e boas práticas de desenvolvimento Python (lint, testes, formatação automática).  

O objetivo é provisionar clusters, ingerir dados em camadas (bronze, silver, gold), aplicar transformações e análises, além de garantir qualidade e automação via testes e pipelines.

---

🚀 **Tecnologias Utilizadas**

- Python 3.12  
- PySpark para processamento distribuído  
- Databricks para execução de notebooks e jobs  
- Azure Storage para persistência de dados  
- GitHub Actions para CI/CD  
- Docker + Docker Compose para containerização  
- Pre-commit hooks (Black, Isort, Flake8) para padronização de código  
- Pytest para testes automatizados  

---

💻 **Requisitos de Hardware e Software**

- **Hardware mínimo:**
  - CPU: 4 cores
  - RAM: 8 GB
  - Armazenamento: 10 GB livres

- **Software:**
  - Python 3.12+
  - Docker e Docker Compose
  - Git
  - Conta no Azure Databricks configurada

---

⚙️ **Configurações Necessárias**

**1. Instalar dependências de produção:**
   `bash
   pip install -r requirements.txt
   `

**2. Instalar dependências de desenvolvimento:**
   `bash
   pip install -r requirements-dev.txt
   `

**3. Configurar pre-commit hooks:**
   `bash
   pre-commit install
   `

**4. Executar localmente com Docker:**
   `bash
   docker-compose up -d
   `

**5. Rodar testes:**
   `bash
   pytest
   `

---

📂 **Estrutura do Repositório**



<img width="609" height="1411" alt="Screenshot_20251115-143245" src="https://github.com/user-attachments/assets/03b247ec-efce-4555-9c18-ea187cd50dd5" />



---

📖 **Explicação Detalhada das Pastas e Arquivos**

📒 **Notebooks**
- **01provisionamentocluster.py** → script para provisionar cluster Databricks.  
- **02ingestaobronze.py** → ingestão inicial dos dados na camada bronze.  
- **03transformacaosilver.py** → transformação e limpeza dos dados para camada silver.  
- **04analisevisualizacao.py** → análises exploratórias e visualizações.  
- **runner_pipeline.py** → orquestra execução sequencial dos notebooks.  

📚 **Libs**
- **io_utils.py** → funções utilitárias de leitura/escrita de dados.  
- **spark_session.py** → inicialização e configuração da sessão Spark.  
- **validation.py** → funções de validação de dados e schemas.  
- **__init__.py** → torna a pasta um pacote Python.  

⚙️ **Jobs**
- **job_pipeline.json** → definição de job Databricks para rodar o pipeline.  

☁️ **Databricks**
- **pipelines/ci.yml** → pipeline de integração contínua no Databricks.  
- **pipelines/cd.yml** → pipeline de entrega contínua no Databricks.  
- **workspace_export/notebooks.dbc** → exportação dos notebooks em formato Databricks.  
- **config/cluster_template.json** → template de configuração de cluster.  
- **config/job_template.json** → template de configuração de job.  

🔄 **GitHub Actions**
- **.github/workflows/ci.yml** → pipeline de CI (lint, testes, build).  
- **.github/workflows/cd.yml** → pipeline de CD (deploy).  

📑 **Documentação**
- **guianomenclaturaazure.md** → guia de boas práticas de nomenclatura no Azure.  
- **imagens/** → diagramas e prints do portal Azure e Databricks.  

🧪 **Testes**
- **testioutils.py** → testa funções de leitura/escrita.  
- **testsparksession.py** → testa inicialização da sessão Spark.  
- **test_validation.py** → testa funções de validação.  
- **notebooks/test_pipeline.py** → testa execução do pipeline de notebooks.  
- **data/** → arquivos CSV de exemplo (vendas, clientes, produtos).  

🛠️ **Configuração e Build**
- **.gitignore** → arquivos ignorados pelo Git.  
- **.flake8** → configuração de lint.  
- pyproject.toml → configurações unificadas (Black, Isort, Flake8).  
- **setup.cfg** → configurações adicionais do Flake8.  
- **requirements.txt** → dependências de produção.  
- **requirements-dev.txt** → dependências de desenvolvimento.  
- **Makefile** → comandos automatizados (formatar, lint, testes).  
- **format.sh** → script para rodar Black, Isort e Flake8.  
- **.git/hooks/pre-commit** → hook local para rodar format.sh antes do commit.  
- **.pre-commit-config.yaml** → configuração do pre-commit framework.  

🐳 **Containerização**
- **Dockerfile** → imagem otimizada de produção.  
- **docker-compose.yml** → orquestração de app + banco + cache em produção.  
- **docker-compose.override.yml** → configuração extra para desenvolvimento (hot-reload, debug).  

---

🎯 **Como Executar o Projeto**

**1. Clonar repositório:**
   `bash
   git clone https://github.com/seu-org/seu-repo.git
   cd seu-repo
   `

**2. Instalar dependências:**
   `bash
   pip install -r requirements-dev.txt
   `

**3. Rodar pre-commit hooks:**
   `bash
   pre-commit run --all-files
   `

**4. Subir ambiente com Docker Compose:**
   `bash
   docker-compose up -d
   `

**5. Executar pipeline:**
   - Via Databricks job (jobs/job_pipeline.json).  
   - Ou localmente com:
     `bash
     python notebooks/runner_pipeline.py
     `

---

✅ **Conclusão**

Este repositório fornece uma solução completa de Data Engineering com Databricks, CI/CD e boas práticas de desenvolvimento Python.

Ele está pronto para ser usado tanto em produção quanto em desenvolvimento, com suporte a testes, lint, formatação automática e containerização.

---

**Autor:**
Sergio Santos 

---
**Contato:**

[![Portfólio Sérgio Santos](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://santosdevbjj.github.io/portfolio/)
[![LinkedIn Sérgio Santos](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz) 


---



