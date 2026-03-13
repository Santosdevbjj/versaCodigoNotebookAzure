# Controle e Versionamento de Código em Notebooks Azure Databricks

![Azure_Databricks01](https://github.com/user-attachments/assets/d30d3cd1-7b30-4247-8f19-a9d9941c9c8b)

**Bootcamp Microsoft AI for Tech — Azure Databricks**

---

## 📑 Sumário

- [1. Problema de Negócio](#1-problema-de-negócio)
- [2. Contexto](#2-contexto)
- [3. Premissas da Solução](#3-premissas-da-solução)
- [4. Planejamento da Solução](#4-planejamento-da-solução)
- [5. Arquitetura Medalhão — Bronze, Silver, Gold](#5-arquitetura-medalhão--bronze-silver-gold)
- [6. Engenharia do Pipeline](#6-engenharia-do-pipeline)
- [7. Qualidade de Código e Governança](#7-qualidade-de-código-e-governança)
- [8. CI/CD — Integração e Deploy Contínuo](#8-cicd--integração-e-deploy-contínuo)
- [9. Insights Técnicos e Decisões](#9-insights-técnicos-e-decisões)
- [10. Resultados para o Negócio](#10-resultados-para-o-negócio)
- [11. Estrutura do Repositório](#11-estrutura-do-repositório)
- [12. Stack Tecnológica](#12-stack-tecnológica)
- [13. Como Executar](#13-como-executar)
- [14. Próximos Passos](#14-próximos-passos)
- [Contato](#contato)

---

## 1. Problema de Negócio

**Qual problema este projeto resolve?**

Em grandes organizações, equipes de dados constroem pipelines analíticos diariamente — mas frequentemente os entregam de uma forma que torna impossível auditá-los, mantê-los ou evoluí-los com segurança.

O problema concreto que este projeto resolve é:

> *"Como uma equipe de engenharia de dados pode garantir que notebooks do Azure Databricks sejam rastreáveis, testáveis, versionados e deployados automaticamente — com o mesmo rigor de um sistema bancário crítico — sem depender de execuções manuais ou lógicas espalhadas em células sem estrutura?"*

O cenário que esse projeto combate é conhecido como **"caos de notebooks"**:

- Notebooks sem versionamento claro — não se sabe qual versão está em produção.
- Lógica de negócio espalhada em células executadas manualmente — sem ordem garantida.
- Zero testabilidade — impossível validar transformações de forma isolada.
- Deploy manual — copiar e colar código entre ambientes, sem controle de mudança.
- Ausência de rastreabilidade — em uma auditoria, ninguém sabe o que rodou quando nem quem aprovou.

A resposta está em tratar código de dados com o mesmo rigor de software corporativo: **separação de responsabilidades, bibliotecas reutilizáveis, testes automatizados e CI/CD que bloqueia código sem qualidade**.

---

## 2. Contexto

Instituições financeiras, fintechs e empresas com ambientes regulados operam sob três pressões simultâneas em seus pipelines de dados:

- **Pressão de qualidade:** dados incorretos chegando à camada analítica geram decisões erradas — e em ambientes regulados, podem gerar multas e sanções.
- **Pressão de rastreabilidade:** auditorias exigem saber exatamente qual código processou quais dados, em qual versão, em qual momento.
- **Pressão de escala:** times crescem, notebooks se multiplicam, e sem governança o conhecimento fica preso em indivíduos — se a pessoa sai, o pipeline para.

O cenário antes desta solução:

- Notebooks exploratórios sendo usados diretamente em produção, sem separação de lógica.
- Ausência de camada de bibliotecas reutilizáveis — cada notebook reimplementava as mesmas funções de leitura, escrita e validação.
- Inexistência de testes automatizados — a única validação era visual, pelo analista que executou o notebook.
- Deploy baseado em upload manual para o workspace do Databricks — sem revisão de código, sem aprovação, sem histórico.
- Ausência de padronização de nomenclatura para recursos Azure — clusters, workspaces, storage e key vaults com nomes inconsistentes.

Este projeto constrói do zero um **ambiente corporativo de engenharia de dados**: da organização de notebooks à arquitetura Medalhão, passando por bibliotecas Python testáveis, CI/CD com GitHub Actions e deploy automatizado para o workspace do Databricks.

---

## 3. Premissas da Solução

Para a construção do ambiente, foram adotadas as seguintes premissas:

- **Notebooks são orquestradores, não executores de lógica.** Toda regra de negócio reside nas bibliotecas em `libs/` — os notebooks apenas chamam essas funções. Isso é o que torna o código testável.
- **Data leakage temporal é prevenido na arquitetura.** A separação Bronze → Silver → Gold garante que dados crus nunca chegam diretamente à análise sem passar pelas camadas de limpeza e validação.
- **Qualidade de código é automatizada, não opcional.** Black, Isort e Flake8 rodam via pre-commit e no CI — nenhum push sem formatação e lint passando.
- **O pipeline de CI/CD bloqueia merges com falhas.** Testes unitários falhos, lint quebrado ou notebooks com erro de importação impedem o deploy automaticamente.
- **Nomenclatura de recursos Azure segue padrão corporativo.** Prefixos, ambiente e região são padronizados no `docs/guia_nomenclatura_azure.md` — garantindo consistência e facilitando governança de custos.
- **Docker garante paridade entre local e produção.** O ambiente de desenvolvimento é containerizado — o que roda localmente é o mesmo que roda no CI.

---

## 4. Planejamento da Solução

A solução foi estruturada em quatro camadas independentes e orquestradas:

**Camada 1 — Infraestrutura e Provisionamento**
Configuração de cluster Azure Databricks com templates versionados (`databricks/config/cluster_template.json`). Padrão de nomenclatura corporativa para todos os recursos Azure. Deploy automatizado via CI/CD.

**Camada 2 — Pipeline de Dados (Arquitetura Medalhão)**
Ingestão de dados brutos na camada Bronze com timestamp de ingestão. Limpeza, normalização e join de datasets na camada Silver. Agregações e análises prontas para consumo na camada Gold.

**Camada 3 — Bibliotecas Python Reutilizáveis**
Separação da lógica de negócio em `libs/`: `spark_session.py`, `io_utils.py` e `validation.py`. Cada função é unitariamente testável e independente do contexto de notebook.

**Camada 4 — Qualidade, Testes e Automação**
Pre-commit hooks com Black, Isort e Flake8. Pytest com fixtures Spark para testes unitários das bibliotecas. GitHub Actions para CI (lint + testes) e CD (deploy automatizado para o workspace do Databricks).

**Ferramentas planejadas por camada:**

| Camada | Tecnologia | Justificativa |
|---|---|---|
| Plataforma | Azure Databricks | Ambiente gerenciado de Spark + integração com Azure Storage |
| Processamento | PySpark 3.5, Python 3.12 | Escalabilidade nativa para Big Data |
| Armazenamento | Azure Storage (Data Lake), Delta Lake | Linhagem de dados e time travel |
| Qualidade de código | Black, Isort, Flake8, pre-commit | Padronização automatizada — não depende de disciplina individual |
| Testes | Pytest, pytest-cov | Validação isolada das bibliotecas independente do cluster |
| Containerização | Docker, Docker Compose | Paridade entre ambientes local, CI e produção |
| CI/CD | GitHub Actions | Deploy automatizado com validação obrigatória antes do merge |
| Tipagem | Mypy | Checagem estática de tipos — evita erros em produção |

---

## 5. Arquitetura Medalhão — Bronze, Silver, Gold

A Arquitetura Medalhão é o padrão adotado para garantir linhagem, separação de responsabilidades e evolução controlada dos dados.

```
┌─────────────────────────────────────────────────────────────────┐
│                    FONTE DE DADOS                                │
│              vendas.csv / clientes.csv / produtos.csv            │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  🥉 CAMADA BRONZE — 02_ingestao_bronze.py                        │
│                                                                  │
│  • Ingestão dos dados brutos sem transformação                   │
│  • Adição de timestamp de ingestão (ingestion_ts)                │
│  • Registro em bronze_vendas (TempView)                          │
│  • Dados: exatamente como vieram da fonte — zero alteração       │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  🥈 CAMADA SILVER — 03_transformacao_silver.py                   │
│                                                                  │
│  • Remoção de registros nulos (dropna)                           │
│  • Normalização de valores numéricos                             │
│  • Join: vendas ↔ clientes ↔ produtos (por id_cliente/id_produto)│
│  • Registro em silver_vendas (TempView)                          │
│  • Dados limpos, enriquecidos e prontos para análise             │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  🥇 CAMADA GOLD — 04_analise_visualizacao.py                     │
│                                                                  │
│  • Agregação: total de vendas por cidade                         │
│  • Agregação: total de vendas por categoria                      │
│  • Sumarizações prontas para dashboards e relatórios             │
│  • Dados: visão analítica de negócio — consumo direto            │
└─────────────────────────────────────────────────────────────────┘
```

**Por que essa separação importa?** Em um ambiente sem Arquitetura Medalhão, é comum encontrar transformações aplicadas diretamente sobre dados brutos — sem possibilidade de reprocessar ou auditar. Com o Medalhão, qualquer problema na camada Silver pode ser corrigido e reprocessado a partir do Bronze original, que permanece intacto.

---

## 6. Engenharia do Pipeline

### Notebooks — Responsabilidade única de orquestração

Cada notebook tem uma responsabilidade única e delimitada:

| Notebook | Responsabilidade | Camada |
|---|---|---|
| `01_provisionamento_cluster.py` | Configura e registra o cluster `cl-dbx-dev-br` | Infra |
| `02_ingestao_bronze.py` | Carrega CSV bruto, adiciona `ingestion_ts`, registra TempView | Bronze |
| `03_transformacao_silver.py` | Limpa, normaliza e faz join dos datasets | Silver |
| `04_analise_visualizacao.py` | Agrega por cidade e categoria, gera visualizações | Gold |
| `runner_pipeline.py` | Orquestra todos os notebooks em sequência via `%run` | Pipeline |

### Bibliotecas reutilizáveis — `libs/`

A separação da lógica de negócio em bibliotecas é a decisão técnica mais importante do projeto. **Um notebook não pode ser testado unitariamente — uma função Python sim.**

| Biblioteca | Função | O que resolve |
|---|---|---|
| `libs/spark_session.py` | `get_spark_session(app_name)` | Inicialização padronizada da SparkSession em qualquer contexto |
| `libs/io_utils.py` | `read_csv(spark, path)` / `write_parquet(df, path)` | Leitura e escrita desacopladas do notebook |
| `libs/validation.py` | `validate_schema(df, expected_columns)` | Valida schema antes de qualquer transformação — lança `ValueError` com colunas ausentes identificadas |

### Testes automatizados — `tests/`

Cada biblioteca tem sua suite de testes independente:

| Teste | O que valida |
|---|---|
| `tests/test_spark_session.py` | SparkSession criada corretamente com `appName` esperado |
| `tests/test_io_utils.py` | Leitura de CSV retorna schema e contagem corretos; escrita Parquet preserva dados |
| `tests/test_validation.py` | Schema válido retorna `True`; schema inválido lança `ValueError` com colunas ausentes identificadas |
| `tests/notebooks/test_pipeline.py` | Teste end-to-end: Bronze → Silver → Gold com os datasets reais de teste |

### Dataset de testes — `tests/data/`

O pipeline é validado com um dataset sintético realista:

**`vendas.csv`** — 7 transações com `id_venda`, `id_cliente`, `id_produto`, `quantidade`, `valor`, `categoria` (Eletronico, Alimento, Higiene).

**`clientes.csv`** — 7 clientes com `id_cliente`, `nome`, `idade`, `cidade` (Nova Lima, BH, SP, RJ, Curitiba, Salvador, Fortaleza).

**`produtos.csv`** — 7 produtos com `id_produto`, `nome_produto`, `categoria`, `preco`.

### Job Pipeline — deploy automatizado

O arquivo `jobs/job_pipeline.json` define o Job do Databricks que executa o pipeline em produção com dependência explícita entre tasks:

```json
tasks:
  bronze  →  notebooks/02_ingestao_bronze
  silver  →  notebooks/03_transformacao_silver  (depends_on: bronze)
```

O CI/CD cria o job automaticamente se não existir — ou atualiza se já existir — via `databricks jobs create/update`.

---

## 7. Qualidade de Código e Governança

### Pre-commit hooks — `.pre-commit-config.yaml`

Antes de cada commit, três ferramentas rodam automaticamente:

| Hook | Versão | O que faz |
|---|---|---|
| **Black** | 24.10.0 | Formata o código automaticamente — `line-length = 88` |
| **Isort** | 5.13.2 | Organiza imports por seção e ordem alfabética |
| **Flake8** | 7.1.1 | Valida estilo e detecta padrões problemáticos via `flake8-bugbear` |

**Por que pre-commit e não apenas CI?** Pre-commit bloqueia o commit localmente, antes de qualquer push. Isso evita que o CI rejeite código por problemas de formatação — acelerando o ciclo de desenvolvimento e mantendo o histórico do Git limpo.

### Makefile — comandos padronizados

```bash
make format   # Black + Isort em sequência
make lint     # Flake8 em todo o projeto
make test     # Pytest em tests/
make all      # format → lint → test
```

### Configurações de qualidade — `pyproject.toml`

Todas as ferramentas compartilham a mesma configuração centralizada:

- `line-length = 88` (Black e Flake8 alinhados)
- `F821` ignorado — `dbutils`, `spark`, `display` são globals do Databricks, não variáveis não definidas
- `profile = "black"` no Isort — garante que a organização de imports não conflite com a formatação do Black

### Guia de Nomenclatura Azure — `docs/guia_nomenclatura_azure.md`

Padronização de nomenclatura para todos os recursos criados no Azure:

| Recurso | Padrão | Exemplo |
|---|---|---|
| Resource Group | `rg-{projeto}-{env}-{região}` | `rg-dbx-mlops-dev-br` |
| Workspace Databricks | `dbx-ws-{projeto}-{env}-{região}` | `dbx-ws-mlops-dev-br` |
| Cluster | `cl-dbx-{env}-{região}` | `cl-dbx-dev-br` |
| Storage | `st{projeto}{env}{região}` | `stmlopsdevbr` |
| Key Vault | `kv-{projeto}-{env}-{região}` | `kv-mlops-dev-br` |

Tags obrigatórias em todos os recursos: `dono`, `projeto`, `ambiente`, `custo-centro`.

---

## 8. CI/CD — Integração e Deploy Contínuo

### Pipeline CI — `.github/workflows/ci.yml`

Acionado em todo push e pull request para `main`. Bloqueia merges que não passem em todos os passos:

```
1. Checkout do repositório
2. Setup Python 3.12
3. Instalação de dependências (pre-commit, pytest)
4. Pre-commit --all-files (Black, Isort, Flake8)
5. Pytest tests/
```

**Regra:** nenhum código chega à `main` sem ter passado em lint, formatação e testes.

### Pipeline CD — `.github/workflows/cd.yml`

Acionado em push para `main` (após CI aprovado) ou manualmente via `workflow_dispatch`:

```
1. Validação de secrets (DATABRICKS_HOST, DATABRICKS_TOKEN)
2. Deploy de notebooks → /Projects/versaCodigoNotebookAzure/notebooks/
3. Deploy de libs     → /Projects/versaCodigoNotebookAzure/libs/
4. Deploy de cluster  → cria cl-dbx-dev-br se não existir
5. Deploy de job      → cria ou atualiza job-pipeline-versaCodigo
```

**O CD é idempotente:** rodar múltiplas vezes produz o mesmo resultado — clusters e jobs não são duplicados, apenas criados na primeira vez ou atualizados nas seguintes.

### Configuração de secrets necessária

| Secret | Onde configurar | Descrição |
|---|---|---|
| `DATABRICKS_HOST` | GitHub → Settings → Secrets | URL do workspace Databricks (ex: `https://adb-xxx.azuredatabricks.net`) |
| `DATABRICKS_TOKEN` | GitHub → Settings → Secrets | Token de acesso pessoal ou service principal |

---

## 9. Insights Técnicos e Decisões

### Decisão 1 — Separar lógica de negócio em `libs/` (a mais importante)

**O problema:** notebooks não são testáveis unitariamente. Uma célula que faz leitura, transformação e escrita ao mesmo tempo é impossível de validar de forma isolada.

**A decisão:** toda função que pode ser isolada — leitura, escrita, validação de schema — reside em `libs/`. Os notebooks chamam essas funções; não as reimplementam.

**O resultado:** `test_io_utils.py`, `test_spark_session.py` e `test_validation.py` rodam em segundos, sem precisar de um cluster Databricks ativo. O CI pode validar a lógica completamente localmente.

### Decisão 2 — Docker multi-stage para imagem enxuta

O `Dockerfile` usa build em dois estágios: o primeiro instala dependências de compilação, o segundo copia apenas o resultado — sem `gcc` e `build-essential` na imagem final. Isso reduz o tamanho da imagem e a superfície de ataque em produção.

### Decisão 3 — `F821` ignorado no Flake8

`dbutils`, `spark` e `display` são variáveis globais injetadas pelo runtime do Databricks — não existem no escopo local. Ignorar `F821` evita falsos positivos no lint sem comprometer a detecção de variáveis genuinamente indefinidas.

### Decisão 4 — Docker Compose com hot-reload em desenvolvimento

O `docker-compose.override.yml` monta o código local como volume e usa `watchmedo` para reiniciar automaticamente o processo quando arquivos `.py` mudam. Em produção, o `docker-compose.yml` base é usado sem override — sem hot-reload, sem código local montado.

### Decisão 5 — CI/CD com verificação de existência antes de criar

O pipeline CD não falha se o cluster ou job já existir — ele verifica a existência via `databricks clusters list` e `databricks jobs list` antes de decidir entre criar ou atualizar. Isso torna o deploy seguro para reexecução.

---

## 10. Resultados para o Negócio

### O que este projeto entrega operacionalmente

| Problema | Antes | Depois |
|---|---|---|
| Versionamento de notebooks | Manual — arquivo renomeado com data | Git — histórico completo, diff por linha, rollback em segundos |
| Deploy em produção | Upload manual no workspace | CI/CD automático — todo push aprovado vai para o workspace |
| Testabilidade | Zero — validação visual manual | Pytest com 3 suites unitárias + 1 teste end-to-end |
| Qualidade de código | Inconsistente por desenvolvedor | Padronizada e automatizada — Black, Isort, Flake8 via pre-commit |
| Rastreabilidade | Impossível saber o que rodou quando | Cada deploy registrado no GitHub Actions com hash de commit |
| Lógica de negócio | Espalhada em células de notebooks | Centralizada em `libs/` — reutilizável e testável |
| Nomenclatura de recursos | Ad-hoc e inconsistente | Padronizada no guia de nomenclatura — governança de custos habilitada |

### Impacto em um ambiente regulado

Em instituições financeiras, esse tipo de estrutura é pré-requisito para:

- **Auditoria interna e externa:** cada versão de código que processou dados é rastreável por commit hash.
- **Incident response:** quando um pipeline falha, o histórico de deploys mostra exatamente qual mudança foi a última — facilitando rollback.
- **Onboarding de novos engenheiros:** um desenvolvedor novo pode rodar `make all` e ter lint, testes e validação funcionando em minutos — sem depender de documentação oral.

---

## 11. Estrutura do Repositório

```text
versaCodigoNotebookAzure/
│
├── notebooks/
│   ├── 01_provisionamento_cluster.py   # Configura cluster cl-dbx-dev-br com Spark 14.3
│   ├── 02_ingestao_bronze.py           # Ingestão de CSV bruto + ingestion_ts → bronze_vendas
│   ├── 03_transformacao_silver.py      # Limpeza, normalização e join vendas+clientes+produtos
│   ├── 04_analise_visualizacao.py      # Agregações por cidade e categoria → visualizações Gold
│   └── runner_pipeline.py             # Orquestrador: executa 01→02→03→04 via %run
│
├── libs/
│   ├── __init__.py
│   ├── spark_session.py               # get_spark_session(app_name) — inicialização padronizada
│   ├── io_utils.py                    # read_csv(spark, path) / write_parquet(df, path)
│   └── validation.py                  # validate_schema(df, expected_columns) — lança ValueError
│
├── jobs/
│   └── job_pipeline.json              # Job Databricks: bronze → silver (com depends_on explícito)
│
├── tests/
│   ├── data/
│   │   ├── vendas.csv                 # 7 transações: id_venda, id_cliente, id_produto, valor
│   │   ├── clientes.csv               # 7 clientes: id_cliente, nome, idade, cidade
│   │   └── produtos.csv               # 7 produtos: id_produto, nome_produto, categoria, preco
│   ├── notebooks/
│   │   └── test_pipeline.py           # Teste end-to-end: Bronze→Silver→Gold com datasets reais
│   ├── test_io_utils.py               # Testa read_csv e write_parquet com fixture Spark
│   ├── test_spark_session.py          # Valida criação e appName da SparkSession
│   └── test_validation.py             # Testa validate_schema: sucesso e ValueError esperado
│
├── databricks/
│   ├── config/
│   │   ├── cluster_template.json      # Template: cl-dbx-dev-br, Standard_DS3_v2, 1 worker
│   │   └── job_template.json          # Template base para criação de jobs
│   ├── pipelines/
│   │   ├── ci.yml                     # Pipeline CI (Azure DevOps): lint + testes
│   │   └── cd.yml                     # Pipeline CD (Azure DevOps): deploy de notebooks
│   └── workspace_export/
│       └── notebooks.dbc              # Export do workspace Databricks
│
├── docs/
│   ├── imagens/
│   │   ├── databricks_cluster.png     # Captura: cluster configurado no workspace
│   │   ├── jobs_pipeline.png          # Captura: job pipeline com tasks e dependências
│   │   ├── portal_azure_workspace.png # Captura: workspace no portal Azure
│   │   └── repositorio_git_config.png # Captura: repositório Git configurado no Databricks
│   └── guia_nomenclatura_azure.md     # Padrões: rg-, dbx-, cl-, st-, kv- + tags obrigatórias
│
├── .github/
│   └── workflows/
│       ├── ci.yml                     # CI: checkout → Python 3.12 → pre-commit → pytest
│       └── cd.yml                     # CD: secrets → deploy notebooks/libs → cluster → job
│
├── Dockerfile                         # Multi-stage: builder com gcc → imagem final enxuta
├── docker-compose.yml                 # Produção: app + postgres:16 + redis:7
├── docker-compose.override.yml        # Desenvolvimento: hot-reload via watchmedo
├── pyproject.toml                     # Config centralizada: Black, Isort, Flake8 (py312)
├── .flake8                            # Flake8: max-line-length=88, F821/W391/E203/W503 ignorados
├── setup.cfg                          # Flake8 legado + select E,F,W,B
├── .pre-commit-config.yaml            # Hooks: Black 24.10.0, Isort 5.13.2, Flake8 7.1.1
├── Makefile                           # make format / make lint / make test / make all
├── requirements.txt                   # Produção: pyspark, databricks-cli, azure-storage-blob
├── requirements-dev.txt               # Dev: black, isort, flake8, pre-commit, pytest, mypy
└── format.sh                          # Script bash: black → isort → flake8 em sequência
```

### Estrutura visual do repositório

<img width="609" height="1411" alt="Screenshot_20251115-143245" src="https://github.com/user-attachments/assets/03b247ec-efce-4555-9c18-ea187cd50dd5" />

---

## 12. Stack Tecnológica

| Camada | Tecnologia | Versão | Papel |
|---|---|---|---|
| **Plataforma** | Azure Databricks | Workspace managed | Runtime Spark + orquestração de Jobs |
| **Armazenamento** | Azure Storage (Data Lake) | — | Fonte de dados e camadas Bronze/Silver/Gold |
| **Runtime** | Apache Spark | 14.3.x-scala2.12 | Processamento distribuído |
| **Linguagem** | Python | 3.12 | Lógica de pipeline e bibliotecas |
| **Processamento** | PySpark | 3.5.1 | API Python para Spark |
| **Formatação** | Black | 24.10.0 | Formatação automática de código |
| **Imports** | Isort | 5.13.2 | Organização automática de imports |
| **Lint** | Flake8 + bugbear | 7.1.1 | Validação de estilo e padrões problemáticos |
| **Hooks** | pre-commit | 4.0.1 | Automação de qualidade antes do commit |
| **Testes** | Pytest + cov | 8.3.3 | Testes unitários e end-to-end |
| **Tipagem** | Mypy | 1.11.2 | Checagem estática de tipos |
| **Container** | Docker + Compose | — | Paridade entre ambientes |
| **CI/CD** | GitHub Actions | — | Lint → testes → deploy automatizado |
| **CLI Deploy** | Databricks CLI | 0.18.0 | Deploy de notebooks, clusters e jobs |
| **SDK Azure** | azure-storage-blob | 12.23.1 | Integração com Azure Storage |

---

## 13. Como Executar

### Pré-requisitos

**Hardware mínimo:**
- CPU: 4 cores | RAM: 8 GB | Armazenamento: 10 GB livres (SSD recomendado)

**Software:**
- Python 3.12+
- Docker e Docker Compose
- Git e GNU Make
- Conta ativa no Azure Databricks (com token de acesso)

---

### Passo 1 — Clonar o repositório

```bash
git clone https://github.com/Santosdevbjj/versaCodigoNotebookAzure.git
cd versaCodigoNotebookAzure
```

---

### Passo 2 — Instalar dependências de desenvolvimento

```bash
pip install -r requirements-dev.txt
pre-commit install
```

O `pre-commit install` registra os hooks localmente — a partir desse momento, Black, Isort e Flake8 rodam automaticamente antes de cada commit.

---

### Passo 3 — Subir ambiente local com Docker

```bash
# Ambiente de desenvolvimento com hot-reload
docker-compose up -d

# Para derrubar
docker-compose down
```

O `docker-compose.override.yml` é aplicado automaticamente em desenvolvimento, habilitando hot-reload e montando o código local como volume.

---

### Passo 4 — Verificar qualidade do código

```bash
# Todos os passos em sequência
make all

# Ou individualmente
make format   # Black + Isort
make lint     # Flake8
make test     # Pytest
```

Ou via script:

```bash
bash format.sh
```

---

### Passo 5 — Executar testes

```bash
pytest tests/ -v
```

Os testes cobrem: SparkSession, leitura/escrita de dados e validação de schema. O teste end-to-end em `tests/notebooks/test_pipeline.py` executa o pipeline completo Bronze → Silver → Gold.

---

### Passo 6 — Configurar secrets para CI/CD

No GitHub, navegue até **Settings → Secrets and variables → Actions** e adicione:

```
DATABRICKS_HOST  →  https://adb-<workspace-id>.azuredatabricks.net
DATABRICKS_TOKEN →  dapi<seu-token-de-acesso>
```

---

### Passo 7 — Executar o pipeline no Databricks

**Via Job (automatizado pelo CD):**

O job `job-pipeline-versaCodigo` é criado/atualizado automaticamente pelo pipeline CD. Para disparar manualmente no workspace do Databricks: **Jobs → job-pipeline-versaCodigo → Run now**.

**Via notebook runner (execução direta):**

No workspace do Databricks, abrir e executar `notebooks/runner_pipeline.py` — ele orquestra todos os notebooks em sequência via `%run`.

---

## 14. Próximos Passos

Com base na estrutura construída, os próximos passos recomendados são:

- **Orquestração com Azure Data Factory:** integrar o pipeline ao ADF para agendamento, monitoramento e alertas de falha centralizados.
- **Observabilidade de dados:** implementar monitoramento de qualidade de dados nas camadas Silver e Gold — alertas quando registros nulos excedem um threshold ou schema diverge do esperado.
- **Delta Lake com time travel:** migrar as camadas Bronze e Silver para Delta format, habilitando auditoria histórica e reprocessamento de versões anteriores dos dados.
- **Machine Learning na camada Gold:** integrar modelos de previsão diretamente sobre os dados agregados da camada Gold, usando MLflow para rastreabilidade de experimentos.
- **Cobertura de testes para 80%+:** expandir as suites de teste para cobrir os notebooks de análise e o runner de pipeline, além das bibliotecas já cobertas.
- **Model Registry:** versionar artefatos de modelos com MLflow ou Azure ML — rastreabilidade completa de qual modelo está em produção.

---

**Autor:** Sergio Santos

[![Portfólio Sérgio Santos](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://portfoliosantossergio.vercel.app)

[![LinkedIn Sérgio Santos](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz)

---


