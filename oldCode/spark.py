from pyspark import SparkContext, SparkConf, SQLContext
import _mssql

master="local"
conf = SparkConf() \
    .setAppName("pysparkToAzure") \
    .setMaster(master) \
    .set("spark.driver.extraClassPath","sqljdbc_8.2/mssql-jdbc-8.2.0.jre11.jar")\
    .set("spark.executor.extraClassPath","sqljdbc_8.2/mssql-jdbc-8.2.0.jre11.jar")
sc=SparkContext(conf=conf)


import pandas as pd

sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession

database = "Test"
ser="mosaico.database.windows.net:1433"
table = "dbo.DOCENTI"
user = "PanDario"
password = ""

jdbcDF = spark.read.format("jdbc") \
    .option("url", "jdbc:sqlserver://mosaico.database.windows.net:1433/Test")\
    .option("dbtable",table)\
    .option("user", user) \
    .option("password", password) \
    .option("driver",  "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
    .load()