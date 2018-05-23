# Airflow-Pipeline
Data pipeline built on Airflow.

## Summary


## How to use
### Supervisor
Install the supervisor-4.0.0.dev0
`sudo pip install git+https://github.com/Supervisor/supervisor@master`

Put airflow-supervisord.conf under ~/supervisor/
`supervisord -c airflow-supervisord.conf`


Supervisor client
`supervisorctl -c airflow-supervisord.conf status all`

`supervisorctl -c airflow-supervisord.conf stop all`

`supervisorctl -c airflow-supervisord.conf restart all`

Log files
`/tmp/supervisord.log`

PID
`cat /tmp/supervisord.pid`


### Ansible


### Airflow
Access the dags inside ~/airflow/dags
`export AIRFLOW_HOME=~/airflow`

Define python functions elsewhere and import them into dag files
`export PYTHONPATH=~/data-pipeline-zhihu`

`pip install apache-airflow[gcp_api]`


`airflow initdb`

Need to open port 8080 on the instance.
`airflow webserver -p 8080 -D`

`airflow resetdb -y`

`airflow scheduler --daemon`
Screen 28196.pts-4.instance-1

`airflow test zhihu collect_from_topic_19552706 2018-5-12`

Web UI
http://35.232.122.87:8080/admin/

### Postgresql


## Tests

### Dag integity tests
Is the dag valid?

### Task logic tests

### Data quality tests

## References

[Data’s Inferno: 7 Circles of Data Testing Hell with Airflow](https://medium.com/@ingwbaa/datas-inferno-7-circles-of-data-testing-hell-with-airflow-cef4adff58d8)
[TIPS FOR TESTING AIRFLOW DAGS](https://blog.antoine-augusti.fr/2018/01/tips-testing-airflow-dags/)
