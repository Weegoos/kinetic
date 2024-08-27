#!/bin/bash

# Access the environment variables directly
echo "Restoring database ${POSTGRES_DB} using user ${POSTGRES_USER}"

# Define the directory where dumps are stored
DUMP_DIR="/dumps"

# Find the latest dump file based on the timestamp in the filename
LATEST_DUMP=$(ls -t ${DUMP_DIR}/dump_*.sql 2>/dev/null | head -1)

# Check if any dump file is found
if [ -z "$LATEST_DUMP" ]; then
    echo "No dump files found in ${DUMP_DIR}."
    exit 1
fi

# Terminate active connections to the target database
echo "Terminating active connections for database ${POSTGRES_DB}"
psql -U ${POSTGRES_USER} -d postgres -c "SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE datname = '${POSTGRES_DB}' AND pid <> pg_backend_pid();"

# Wait a moment to ensure connections are terminated
sleep 5

# Drop the existing database
echo "Dropping the existing database ${POSTGRES_DB}"
psql -U ${POSTGRES_USER} -c "DROP DATABASE IF EXISTS ${POSTGRES_DB};"

# Create a new database
echo "Creating a new database ${POSTGRES_DB}"
psql -U ${POSTGRES_USER} -c "CREATE DATABASE ${POSTGRES_DB};"

# Restore the database using the latest dump file
echo "Restoring from backup: ${LATEST_DUMP}"
psql -U ${POSTGRES_USER} ${POSTGRES_DB} < ${LATEST_DUMP}

if [ $? -eq 0 ]; then
    echo "Database successfully restored from ${LATEST_DUMP}"
else
    echo "Failed to restore the database."
    exit 1
fi
