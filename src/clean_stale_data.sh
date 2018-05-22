#!/bin/bash
#clean_stale_data.sh
DIRECTORY=$(pwd)/../data/weebly/out
if [ -d "$DIRECTORY" ]; then
  rmdir "$DIRECTORY"
fi
mkdir "$DIRECTORY"
