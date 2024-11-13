import textwrap
from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    "el_indicium",
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
) as dag:


    t1 = BashOperator(
        task_id="extract-postgres",
        bash_command="""
            export DATE={{ds}}
            meltano el tap-postgres target-csv-postgres""",
    )

    t2 = BashOperator(
        task_id="extract-csv",
        bash_command= """ 
            export DATE={{ds}}
            meltano el tap-csv-csv target-csv-csv""",
    )

    t3 = BashOperator(
        task_id="load-postgres",
        bash_command="""
            export DATE={{ds}}
            meltano el tap-csv-postgres target-postgres""",
    )

    [t1, t2] >> t3