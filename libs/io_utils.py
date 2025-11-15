# Biblioteca: IO Utils
# Funções auxiliares para leitura e escrita


def read_csv(spark, path):
    return spark.read.format("csv").option("header", "true").load(path)


def write_parquet(df, path):
    df.write.mode("overwrite").parquet(path)
