# Biblioteca: Spark Session
# Inicialização da sessão Spark

from pyspark.sql import SparkSession


def get_spark_session(app_name="DatabricksApp"):
    return SparkSession.builder.appName(app_name).getOrCreate()
