# Databricks notebook source
# Notebook: Ingestão Bronze
# Objetivo: Ingestão de dados brutos na camada Bronze

from pyspark.sql import functions as F

# MAGIC %md
# MAGIC ## Ingestão Bronze
# MAGIC Carregando dados CSV para a camada Bronze.

dbutils.widgets.text("source_path", "/mnt/dados") 
dbutils.widgets.text("source_path", "tests/data/vendas.csv") 
source_path = dbutils.widgets.get("source_path")


df = spark.read.format("csv").option("header", "true").load(source_path)
df_bronze = df.withColumn("ingestion_ts", F.current_timestamp())

display(df_bronze)
