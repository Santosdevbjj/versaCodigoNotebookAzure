from libs import spark_session

def test_get_spark_session():
    spark = spark_session.get_spark_session("TestSparkSession")
    assert spark is not None
    assert spark.sparkContext.appName == "TestSparkSession"
