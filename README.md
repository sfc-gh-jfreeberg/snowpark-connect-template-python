# snowpark-connect-template-python
A reference Python project template for **Snowpark Connect for Apache Spark**.

## Setup

### Prerequisites
First, install uv if you don't have it:
```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or via Homebrew on macOS
brew install uv

# Or via pip
pip install uv
```

### Set Up Python Environment
```bash
# Clone the repo
git clone https://github.com/sfc-gh-jfreeberg/snowpark-connect-template-python # Will move this
cd snowpark-connect-template-python

uv python pin 3.12  # Sets Python version for the project
uv sync             # Creates venv and installs all dependencies
```

### Install CLI Tools
Install the Snowflake CLI and `snowpark-submit`.

```bash
uv tool install snowpark-submit
uv tool install snowflake-cli
```

If you haven't used the Snowflake CLI before, run `snow connection add` and `snow connection set-default` to create a connection entry and set it as the default connection. The `snowpark-connect` library will use this default connection entry.

## Local Development


```bash
uv run src/main.py
```

## Job Submission

```bash
export POOL_NAME="spark_pool"

snow spcs compute-pool create $POOL_NAME \
    --min-nodes 2 \
    --max-nodes 2 \
    --family "CPU_X64_XS"
```

```bash
snowpark-submit @{$STAGE_NAME}/main.py \
    --snowflake-workload-name my_name \
    --compute-pool $POOL_NAME \
    --snowflake-connection-name $CONNECTION_NAME 
```

https://docs.snowflake.com/en/developer-guide/snowpark-connect/snowpark-submit-reference