# Databricks notebook source
# Notebook: Transformação Silver
# Objetivo: Limpeza e transformação dos dados

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
