## create a file with name 'requirements.txt' and run below command
```pip install -r ./requirements.txt```


## SPARK DETAILS libs required
```
	org.mongodb.spark#mongo-spark-connector_2.12;3.0.2
	org.mongodb#mongodb-driver-sync;4.0.5
	org.mongodb#bson;4.0.5
	org.mongodb#mongodb-driver-core;4.0.5
```


# Install Spark in local machine:
```
brew install apache-spark
```

## if you want to use Jars instead of packages
```
.config("spark.jars", r"file:///path_to_jars/org.mongodb.spark_mongo-spark-connector_2.12-3.0.2.jar, path_to_jars...., ...")
```

<img width="1248" alt="image" src="https://github.com/user-attachments/assets/a3113205-5f69-465c-8e0e-5398f5d0c072" />


## MongoDB Docker Image:
```
docker run --name mongodb -p 27017:27017 -e MONGODB_USERNAME=test_user -e MONGODB_ROOT_PASSWORD=root_password -e MONGODB_PASSWORD=test_password -e MONGODB_DATABASE=test_database -d bitnami/mongodb:latest
```

##  Create a virtual environment
```python -m venv venv```

## Activate Virtual Environment
- Mac: ```source venv/bin/activate```
- Windows: ```venv\Script\activate```
