##  Create a virtual environment
```python -m venv venv```

## Activate Virtual Environment
- Mac: ```source venv/bin/activate```
- Windows: ```vnev\Script\activate.bat```


## create a file with name 'requirements.txt' and run below command
```pip install -r ./requirements.txt```


## Docker Commands

- ```docker build -t test-python .```
- ```docker run --name test-python -p 8080:8080 -d test-python```

## SPARK DETAILS libs required
```
	org.mongodb.spark#mongo-spark-connector_2.12;3.0.2 in central
	org.mongodb#mongodb-driver-sync;4.0.5 in central
	org.mongodb#bson;4.0.5 in central
	org.mongodb#mongodb-driver-core;4.0.5 in central
```