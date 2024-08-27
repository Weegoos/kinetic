#!/bin/bash

# Access the environment variables directly
echo "Restoring database ${POSTGRES_DB} using user ${POSTGRES_USER}"

# Define the directory where dumps are stored
DUMP_DIR="/dumps"

# Get the current date and time
CURRENT_TIME=$(date +"%Y%m%d_%H%M%S")

# Define the filename with the current timestamp
DUMP_FILE="${DUMP_DIR}/dump_${CURRENT_TIME}.sql"

# Create the database dump with the timestamped filename
pg_dump -U ${POSTGRES_USER} ${POSTGRES_DB} -f ${DUMP_FILE}

echo "Database dump created: ${DUMP_FILE}"
