from snowflake.snowpark_connect.server import init_spark_session

def main():
    print("Hello from snowpark-connect-template-python!")



if __name__ == "__main__":
    SparkSession = init_spark_session()
    main()
