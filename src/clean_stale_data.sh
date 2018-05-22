#!/bin/bash
#clean_stale_data.sh
DIRECTORY=$AIRFLOW_HOME/data/weebly/out
if [ -d "$DIRECTORY" ]; then
  rmdir "$DIRECTORY"
fi
mkdir "$DIRECTORY"
