Sys.setenv('SPARKR_SUBMIT_ARGS'='"--packages" "com.databricks:spark-csv_2.10:1.3.0" "sparkr-shell"')

library(SparkR)

sc <- sparkR.init(sparkPackages="com.databricks:spark-csv_2.10:1.3.0",master="yarn-client")
sqlContext <- sparkRSQL.init(sc)

#takes hdfs [path by default]
train<-read.df(sqlContext, "data/train.csv", source = "csv", delimiter=",", header="true", inferSchema="true")

