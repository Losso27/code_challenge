# Indicium's Code challenge
This folder contains the solution to the technical challenge, submitted as part of the selection process for the Data Engineer role.
To execute follow the steps described bellow. The csv file with the result is inside the data folder as **result.csv**.

## Step 1: install Meltano
```
pip install "meltano"
```

## Step 2: Starting the databases
```
docker-compose up -d
```

## Step 3: Start Airflow
Only start the scheduler:
```
meltano invoke airflow scheduler -D
```
Start airflow with webserver(user and password should be on the logs):
```
meltano invoke airflow webserver
```

## Step 4: Manually trigger the pipeline or a Task

Trigger the hole process for a specific date (Replace \<DATE> with desired date):
```
meltano invoke airflow dags trigger el_indicium -e <DATE>
```

Trigger a part of the pipeline (Replace \<DATE> with desired date and \<TASK> with extract-csv, extract-postgres or load-postgres):
```
meltano invoke airflow tasks run el_indicium <TASK> <DATE> --force
```
