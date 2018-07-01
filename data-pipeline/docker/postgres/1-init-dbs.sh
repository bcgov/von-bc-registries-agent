#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER mara_db;
    CREATE DATABASE mara_db;
    GRANT ALL PRIVILEGES ON DATABASE mara_db TO mara_db;
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER bc_reg_db;
    CREATE DATABASE bc_reg_db;
    GRANT ALL PRIVILEGES ON DATABASE bc_reg_db TO bc_reg_db;
EOSQL

