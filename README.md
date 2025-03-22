##  Create a virtual environment
```python -m venv venv```

## Activate Virtual Environment
- Mac: ```source venv/bin/activate```
- Windows: ```venv\Script\activate```


## create a file with name 'requirements.txt' and run below command
```pip install -r ./requirements.txt```


## SPARK DETAILS libs required
```
	org.mongodb.spark#mongo-spark-connector_2.12;3.0.2 in central
	org.mongodb#mongodb-driver-sync;4.0.5 in central
	org.mongodb#bson;4.0.5 in central
	org.mongodb#mongodb-driver-core;4.0.5 in central
```


# Install Spark in local machine:
```
brew install apache-spark
```

## if you want to use Jars instead of packages
```
.config("spark.jars", r"file:///path_to_jars/org.mongodb.spark_mongo-spark-connector_2.12-3.0.2.jar, path_to_jars...., ...")
```
