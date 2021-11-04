import findspark
findspark.init('/usr/local/spark')
import pyspark,pyodbc 
from pyspark import SparkContext, SparkConf, SQLContext
import _mssql
import pandas as pd


# DB CREATION
# spark session
from pyspark.sql import SparkSession
spark_session = SparkSession.builder.appName("DataframeFromJson").enableHiveSupport().getOrCreate()
#csv
cases=spark_session.read.csv("assets/COVID-DATA/Case.csv", sep=",", inferSchema="true", header="true")
cases = cases.withColumnRenamed("infection_case","infectionSource")
cases = cases.withColumnRenamed(" case_id","caseID")
regions = spark_session.read.csv("assets/COVID-DATA/Region.csv", sep=",", inferSchema="true", header="true")
cases = cases.withColumnRenamed("elementary_school_count","elementarySchoolCount")
spark_session.sql("create database IF NOT EXISTS COVID")
spark_session.sql("create table IF NOT EXISTS COVID.regions")
spark_session.sql("create table IF NOT EXISTS COVID.cases")
regions.write.insertInto("COVID.regions",overwrite=True)
cases.write.insertInto("COVID.cases",overwrite=True)
cases.write.saveAsTable("COVID.cases")


#HELPER FUNCTIONS
def listTables(res:pd.core.frame.DataFrame):
    obj=res['TABLE_NAME']
    list=[]
    for x in obj:
        list.append(x)
    return list
def listCols(res:pd.core.frame.DataFrame):
    obj=res.columns
    list=[]
    for c in obj:
        list.append(c)
    return list

