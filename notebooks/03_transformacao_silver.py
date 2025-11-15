# Databricks notebook source
# Notebook: Transformação Silver
# Objetivo: Limpeza e transformação dos dados
# Use vendas.csv
# Use clientes.csv
# Use produtos.csv

from pyspark.sql import functions as F

# MAGIC %md
# MAGIC ## Transformação Silver
# MAGIC Aplicando regras de limpeza e normalização.

df_bronze = spark.table("bronze_table")

df_silver = (
    df_bronze
    .dropna()
    .withColumn("valor_normalizado", F.col("valor") * 1.0)
)

df_silver.createOrReplaceTempView("silver_table")
display(df_silver)

df_vendas = spark.read.csv("tests/data/vendas.csv", header=True, inferSchema=True)
df_clientes = spark.read.csv("tests/data/clientes.csv", header=True, inferSchema=True)
df_produtos = spark.read.csv("tests/data/produtos.csv", header=True, inferSchema=True)

df_silver = (
    df_vendas
    .join(df_clientes, "id_cliente")
    .join(df_produtos, "id_produto")
)
display(df_silver) 
