from postgres:10

# Context is the top of the data-pipeline folder
COPY docker/postgres/1-init-dbs.sh /docker-entrypoint-initdb.d/

# Set permissions on the data folder
RUN mkdir -p /var/lib/pgsql/data \
    && chown -R 1001:0 /var/lib/pgsql/data \
    && chmod -R ug+rw /var/lib/pgsql/data