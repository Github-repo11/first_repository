import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta

default_args = {
    'start_date': airflow.utils.dates.days_ago(0),
    'retries':3,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'airflow_emp',
    default_args=default_args,
    description='btech_File',
    schedule_interval='None',
    max_active_runs=2,
    catchup=False,
    dagrun_timeout=timedelta(minutes=10),
)
t1=BashOperator(
task_id="bucket_creation"
bash_command="gsutil mb gs://airflow_bucket"
dag=dag,
depands_on_past=False
gcs_buckettt/emp.csv  gs://airflow_bucket
t2=BashOperator(
task_id="copy_File"
bash_command='gsutil cp '
dag=dag,
depands_on_past=False)

t3=BashOperator(
task_id="betch_stage"
bash_command='bq mk -d stage'
dag=dag,
depands_on_past=False)

t4=BashOperator(
task_id="betch_table"
bash_command='bq mk -t stage_table id:string,name:string,sal:string,phone:string,
dag=dag,
depands_on_past=False)

t5=BashOperator(
task_id="betch_load"
bash_command='bq load --source_format=CSV --skip_leading_rows=1  betch_stage.betch_table'
dag=dag,
depands_on_past=False)

t6=BashOperator(
task_id="betch_history"
bash_command='bq mk betch_history'
dag=dag,
depands_on_past=False)

t7=BashOperator(
task_id="betch_his_table"
bash_command="bq mk -t betch_history.betch_his_table id:integer,name:string,sal:integer,phone:int64,
dag=dag,
depands_on_past=False)

t8=BashOperator(
task_id=""
bash_command="bq query --use_legacy_sql=false insert into betch.history.betch_his_table select cast(id as integer),name string,cast(sal as integer),cast(phone as int64),
dag=dag,
depands_on_past=False)

t9=BashOperator(
task_id=""
bash_command="bq query --use_legacy_sql=false create view betch_history.betch_viewa as select * from betch_history.betch_his_table"
dag=dag,
depands_on_past=False)

