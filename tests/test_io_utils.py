import pytest
from pyspark.sql import SparkSession
from libs import io_utils

@pytest.fixture(scope="module")
def spark():
    return SparkSession.builder.appName("TestIOUtils").getOrCreate()

def test_read_csv_and_write_parquet(tmp_path, spark):
    # Criar CSV temporário
    csv_file = tmp_path / "data.csv"
    csv_file.write_text("id,name\n1,Sergio\n2,Ana")

    # Ler CSV
    df = io_utils.read_csv(spark, str(csv_file))
    assert df.count() == 2
    assert set(df.columns) == {"id", "name"}

    # Escrever Parquet
    parquet_path = tmp_path / "out.parquet"
    io_utils.write_parquet(df, str(parquet_path))

    # Ler Parquet e validar
    df_parquet = spark.read.parquet(str(parquet_path))
    assert df_parquet.count() == 2
