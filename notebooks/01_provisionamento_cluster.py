# Databricks notebook source
# Notebook: Provisionamento de Cluster
# Objetivo: Demonstrar como criar e configurar um cluster no Azure Databricks

# MAGIC %md
# MAGIC ## Provisionamento de Cluster
# MAGIC Este notebook descreve como configurar um cluster básico para desenvolvimento.

# Configuração inicial
cluster_config = {
    "cluster_name": "cl-dbx-dev-br",
    "spark_version": "14.3.x-scala2.12",
    "node_type_id": "Standard_DS3_v2",
    "autotermination_minutes": 20,
    "num_workers": 1
}

print("Cluster configurado:", cluster_config)
