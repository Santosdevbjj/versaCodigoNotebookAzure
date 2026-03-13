### Controle e Versionamento de Código no Notebook da Azure Databricks 

![Azure_Databricks01](https://github.com/user-attachments/assets/d30d3cd1-7b30-4247-8f19-a9d9941c9c8b) 


**Bootcamp Microsoft AI for Tech - Azure Databricks**  


---

**Azure Databricks — Engenharia de Dados e Governança de Notebooks em Cloud**

📋 **Visão Geral**

Este projeto estabelece um padrão corporativo para organização, versionamento e execução de pipelines de dados no ambiente Azure Databricks.

Mais do que executar notebooks, a solução demonstra como aplicar Governança de Dados, DataOps e Arquitetura Medalhão (Bronze, Silver e Gold), simulando um ambiente de missão crítica, onde rastreabilidade, automação e confiabilidade são requisitos essenciais.

O projeto foi estruturado para refletir boas práticas reais de mercado, comuns em instituições financeiras e ambientes regulados.

> Este projeto não tem como foco apenas executar dados, mas demonstrar como dados devem ser tratados em ambientes corporativos modernos.


---

🎯 **Problema que o Projeto Resolve**

Em grandes organizações, é comum encontrar:

• Notebooks sem versionamento claro

• Lógicas de negócio espalhadas em células

• Execuções manuais e pouco rastreáveis

• Baixa testabilidade e reutilização de código


Esse cenário, conhecido informalmente como “caos de notebooks”, dificulta manutenção, auditoria e evolução das soluções de dados.

Este projeto demonstra como tratar código de dados com o mesmo rigor de um software corporativo, reduzindo riscos operacionais e aumentando a confiabilidade dos pipelines.


---

🎯 **Objetivo do Projeto**

Com base na minha experiência de mais de 15 anos em sistemas críticos bancários, desenvolvi este projeto com os seguintes objetivos:

• Consolidar a atuação prática como profissional de dados em cloud

• Demonstrar engenharia de dados estruturada em Azure Databricks

• Aplicar governança e rastreabilidade em pipelines analíticos

• Implementar práticas de DataOps e CI/CD

• Diferenciar notebooks exploratórios de notebooks corporativos

• Explorar o uso de IA Generativa integrada ao Databricks como apoio técnico



---

🛠 **Decisões Técnicas**

Algumas decisões foram fundamentais para a qualidade do projeto:

**Arquitetura Medalhão (Bronze, Silver, Gold)**
Utilizada para garantir linhagem dos dados, separação de responsabilidades e evolução controlada.

**Separação de Lógica (Notebooks vs. Libs)**
A lógica de negócio foi extraída para bibliotecas Python reutilizáveis (libs/), deixando os notebooks responsáveis apenas pela orquestração.
Isso facilita testes unitários, manutenção e reutilização.

**CI/CD com GitHub Actions**
Implementado para garantir que apenas códigos validados por lint e testes sejam promovidos, aproximando o projeto de um ambiente produtivo real.

**Integração com Azure Storage (Data Lake)**
Simula um cenário real de Big Data, garantindo escalabilidade e aderência a arquiteturas modernas.


Essas escolhas priorizam clareza, qualidade, rastreabilidade e escalabilidade, mesmo em um projeto educacional.


---

🚀 **Tecnologias Utilizadas**

**Plataforma Cloud:** Azure Databricks, Azure Storage

**Linguagem & Processamento:** Python 3.12+, PySpark

**Arquitetura de Dados:** Arquitetura Medalhão, Delta Lake

**Qualidade & DevOps:**

• GitHub Actions (CI/CD)

• Pytest

• Docker e Docker Compose

• Black e Flake8


**IA Aplicada:** Uso de IA para otimização de funções PySpark e geração de documentação técnica dinâmica.





---

💻 **Requisitos de Hardware e Software**

**Hardware mínimo recomendado**

• CPU: 4 cores

• Memória RAM: 8 GB

• Armazenamento: 10 GB livres


**Software**

• Python 3.12 ou superior

• Docker e Docker Compose

• Git

• Conta ativa no Azure Databricks



---

📂 **Estrutura do Repositório**

O repositório foi organizado para facilitar auditoria técnica, manutenção e escalabilidade:



<img width="609" height="1411" alt="Screenshot_20251115-143245" src="https://github.com/user-attachments/assets/03b247ec-efce-4555-9c18-ea187cd50dd5" />




📒 **notebooks/**

Fluxos principais do pipeline:

Provisionamento de clusters

Ingestão de dados (Bronze)

Transformação e limpeza (Silver)

Análises e agregações (Gold)


📚 **libs/**

Bibliotecas Python reutilizáveis:

Inicialização da Spark Session

Funções de leitura e escrita

Validações de schema e qualidade de dados


⚙️ **jobs/**

Definições de Jobs do Azure Databricks para execução automatizada dos pipelines


🧪 **tests/**

Testes automatizados das bibliotecas e validações

Garantia de confiabilidade dos cálculos e transformações


☁️ **databricks/**

Templates de cluster

Templates de jobs

Exportação de notebooks do workspace


🔄 **.github/workflows/**

Pipelines de CI (lint, testes)

Pipelines de CD (deploy automatizado)


📄 **docs/**

Guias de nomenclatura

Diagramas e documentação técnica



---

▶️ **Como Executar o Projeto**

**Execução resumida**

O pipeline é executado via Jobs do Azure Databricks, utilizando notebooks organizados por camada (Bronze, Silver e Gold), com suporte a automação via CI/CD.

**Execução local**

```
git clone https://github.com/seu-org/seu-repo.git
cd seu-repo
pip install -r requirements-dev.txt
docker-compose up -d
```


> A execução local tem como objetivo validar bibliotecas, testes e pipelines de CI.


**A execução pode ocorrer:**

• via Job configurado no Databricks

• ou via script orquestrador de notebooks



---

🧠 **Aprendizados e Desafios**

O maior desafio foi adaptar a mentalidade de sistemas críticos, onde o erro não é aceitável, à flexibilidade dos notebooks.

**Os principais aprendizados foram:**

• A importância da separação entre lógica de negócio e orquestração

• Como notebooks podem ser parte de uma arquitetura robusta

• Aplicação real de CI/CD em projetos de dados

• Uso consciente de IA Generativa como acelerador técnico, e não como substituto do raciocínio



---

🔮 **Próximos Passos**

• Orquestração externa com Azure Data Factory

• Observabilidade e monitoramento da qualidade dos dados

• Inclusão de modelos de Machine Learning na camada Gold

• Execução totalmente automatizada e agendada



---


**Conclusão**

Este projeto representa um laboratório prático de engenharia de dados em Azure, estruturado com mentalidade corporativa e foco em governança, qualidade e automação.

Embora tenha sido desenvolvido em contexto educacional, o projeto foi estruturado para refletir cenários reais de mercado, aproximando estudos acadêmicos da prática profissional.





---

**Autor:**
Sergio Santos 

---
**Contato:**

[![Portfólio Sérgio Santos](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://portfoliosantossergio.vercel.app)

[![LinkedIn Sérgio Santos](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz)

---



