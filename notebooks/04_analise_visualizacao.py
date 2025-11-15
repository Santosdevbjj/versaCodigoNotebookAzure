# Databricks notebook source
# Notebook: Análise e Visualização
# Objetivo: Criar gráficos e sumarizações

# MAGIC %md
# MAGIC ## Análise e Visualização
# MAGIC Exemplo de agregações e gráficos.

df_silver = spark.table("silver_table")

df_summary = df_silver.groupBy("categoria").count()
display(df_summary) 

df_silver.groupBy("cidade").agg({"valor":"sum"}).show()

# Gráfico de barras
display(df_summary)
