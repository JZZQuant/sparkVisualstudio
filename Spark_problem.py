from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
import os
import sys

spark_home = os.environ.get("SPARK_HOME")
sys.path.insert(0, spark_home + "/python")

os.environ["PYSPARK_SUBMIT_ARGS"]='--master local --executor-memory 2g --packages com.databricks:spark-csv_2.10:1.3.0 pyspark-shell'
sys.path.insert(0, os.path.join(spark_home, "python/lib/py4j-0.8.2.1-src.zip"))

# Initialize PySpark to predefine the SparkContext variable 'sc'
execfile(os.path.join(spark_home, "python/pyspark/shell.py"))

train = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load("data/train.csv")
print train.head()
raw_input()
