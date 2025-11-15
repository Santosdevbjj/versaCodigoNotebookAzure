import pytest
from pyspark.sql import SparkSession
from pyspark.sql import Row
from libs import validation

@pytest.fixture(scope="module")
def spark():
    return SparkSession.builder.appName("TestValidation").getOrCreate()

def test_validate_schema_success(spark):
    df = spark.createDataFrame([Row(id=1, name="Sergio")])
    assert validation.validate_schema(df, ["id", "name"]) is True

def test_validate_schema_missing_column(spark):
    df = spark.createDataFrame([Row(id=1)])
    with pytest.raises(ValueError) as excinfo:
        validation.validate_schema(df, ["id", "name"])
    assert "Colunas ausentes" in str(excinfo.value)
