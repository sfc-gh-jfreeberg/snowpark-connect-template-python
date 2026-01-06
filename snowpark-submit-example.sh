#!/bin/bash
set -x
set -u

# This script provides an example usage of snowpark-submit to run a Python job on Snowflake using Snowpark Connect.

export CONNECTION_NAME="dexqa6" # TODO: Make this a placeholder
export STAGE_NAME="spark_demo"
export POOL_NAME="spark_pool"

snow stage create $STAGE_NAME \
    -c $CONNECTION_NAME

snow stage copy main.py @${STAGE_NAME}/main.py \
    -c $CONNECTION_NAME

snow spcs compute-pool create $POOL_NAME \
    --min-nodes 2 \
    --max-nodes 2 \
    --family "CPU_X64_XS"

snowpark-submit @{$STAGE_NAME}/main.py \
    --snowflake-workload-name my_name \
    --compute-pool $POOL_NAME \
    --snowflake-connection-name $CONNECTION_NAME 