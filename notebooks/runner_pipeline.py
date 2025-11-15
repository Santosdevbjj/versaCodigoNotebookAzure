# Databricks notebook source
# Notebook: Runner Pipeline
# Objetivo: Orquestrar execução dos notebooks

# MAGIC %run ./01_provisionamento_cluster
# MAGIC %run ./02_ingestao_bronze
# MAGIC %run ./03_transformacao_silver
# MAGIC %run ./04_analise_visualizacao

print("Pipeline executado com sucesso!")
