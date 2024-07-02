from pyspark.sql import SparkSession
## Create a Spark Session
## To connect to PsotgresSQL
## Import to HIVE
def connect():
    spark = SparkSession.builder \
        .appName("PostgreSQL to Hive with PySpark") \
        .config("spark.jars", "postgresql-42.6.0.jar") \
        .config("spark.logConf", "true") \
        .config("spark.sql.warehouse.dir", "/tmp/catbd125/emanuel/spark/") \
        .enableHiveSupport() \
        .getOrCreate()

    # JDBC connection parameters
    url = "jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb"
    properties = {
    "user": "consultants",
    "password": "WelcomeItc@2022",
    "driver": "org.postgresql.Driver"
    }
    return spark, url, properties 

def createDataFrame(spark,url,properties):
    try:
    # Load data from PostgreSQL into DataFrame
        df = spark.read.jdbc(url=url, table="raplyrics", properties=properties)
        
    #Transformations
        df = df.withColumnRenamed("entry", "id")
    
    # Print schema and show sample data
        df.printSchema()
        df.show(5, truncate=False)
    
    #Load data into Hive Database emanuel
    
    # Define Hive table schema based on DataFrame schema fetched from PostgreSQL
        hive_table_name = "raplyrics"  # Replace with desired Hive table name
        df.write.mode("overwrite").saveAsTable(hive_table_name)

        print("Data saved successfully to Hive table: ", hive_table_name)
    except Exception as e:
        print("Error reading data from PostgreSQL or saving to Hive:", e)
    finally:
        spark.stop()
        
if __name__ == '__main__':
    [spark, url,properties] = connect()
    createDataFrame(spark,url,properties)
