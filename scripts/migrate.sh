#!/bin/bash

# Exit script on error, undefined variable or pipefail
set -euo pipefail

# Check if docker compose file is passed as an argument
if [ "$#" -ne 1 ]; then
    DOCKER_COMPOSE_FILE="docker-compose.yml"
else
    DOCKER_COMPOSE_FILE=$1
fi

command -v docker compose >/dev/null 2>&1 || {
    echo >&2 "docker compose is required but it's not installed.  Aborting."
    exit 1
}

DB_NAME="tools"

docker compose -f $DOCKER_COMPOSE_FILE up -d

# Retry logic
MAX_RETRIES=5
RETRY_DELAY=5s

for i in $(seq 1 $MAX_RETRIES); do
    if docker compose -f $DOCKER_COMPOSE_FILE exec db mysql -e "SHOW DATABASES;" 2>/dev/null; then
        break
    elif [ $i -eq $MAX_RETRIES ]; then
        echo "Failed to connect to MySQL server after $MAX_RETRIES attempts. Aborting."
        exit 1
    else
        echo "Failed to connect to MySQL server. Retrying in $RETRY_DELAY..."
        sleep $RETRY_DELAY
    fi
done

# Drop the database
docker compose -f $DOCKER_COMPOSE_FILE exec db mysql -e "DROP DATABASE IF EXISTS ${DB_NAME};"

# Create the database
docker compose -f $DOCKER_COMPOSE_FILE exec db mysql -e "CREATE DATABASE ${DB_NAME};"

# Show the tables in the database
docker compose -f $DOCKER_COMPOSE_FILE exec db mysql -e "SHOW DATABASES;"
docker compose -f $DOCKER_COMPOSE_FILE exec app poetry run python -m src.web_api_tools.infrastructure.internal_services.rds_mysql.migrations.rds_mysql_migrate
docker compose -f $DOCKER_COMPOSE_FILE exec db mysql -e "USE ${DB_NAME}; SHOW TABLES;"
docker compose -f $DOCKER_COMPOSE_FILE down
