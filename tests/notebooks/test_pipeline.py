# Databricks notebook source
# Notebook de Teste End-to-End
# Objetivo: Demonstrar ingestão (bronze), transformação (silver) e análise (visualização)
# Dataset: tests/data/vendas.csv, clientes.csv, produtos.csv

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Inicializar Spark
spark = SparkSession.builder.appName("TestPipeline").getOrCreate()

# ============================
# Etapa 1 - Ingestão Bronze
# ============================
print(">>> Ingestão Bronze")

df_vendas = (
    spark.read.csv("tests/data/vendas.csv", header=True, inferSchema=True)
    .withColumn("ingestion_ts", F.current_timestamp())
)

df_vendas.createOrReplaceTempView("bronze_vendas")
print("Registros Bronze:", df_vendas.count())
df_vendas.show(5)

# ============================
# Etapa 2 - Transformação Silver
# ============================
print(">>> Transformação Silver")

df_clientes = spark.read.csv("tests/data/clientes.csv", header=True, inferSchema=True)
df_produtos = spark.read.csv("tests/data/produtos.csv", header=True, inferSchema=True)

df_silver = (
    df_vendas
    .join(df_clientes, "id_cliente")
    .join(df_produtos, "id_produto")
    .dropna()
)

df_silver.createOrReplaceTempView("silver_vendas")
print("Registros Silver:", df_silver.count())
df_silver.show(5)

# ============================
# Etapa 3 - Análise e Visualização
# ============================
print(">>> Análise e Visualização")

# Total de vendas por cidade
df_por_cidade = df_silver.groupBy("cidade").agg(F.sum("valor").alias("total_vendas"))
df_por_cidade.show()

# Total de vendas por categoria
df_por_categoria = df_silver.groupBy("categoria").agg(F.sum("valor").alias("total_vendas"))
df_por_categoria.show()

# ============================
# Conclusão
# ============================
print("Pipeline de teste executado com sucesso!")
