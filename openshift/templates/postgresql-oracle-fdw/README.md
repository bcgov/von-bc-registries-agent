# BC Registries Database

## Overview

Internally the connector connects to an instance of the BC registries database (Oracle) via an a PostgreSQl database via oracle_fdw.

Refer to [Oracle-fdw-Testing](oracle-fdw-testing.md) for information on configuration and testing the connection.

## Credentials

Database credentials are randomly generated as OpenShift secrets when the deployment configuration is first created.

All of the credentials are listed under a single secrete named `postgresql-oracle-fdw`.  The `fdw-user` and `fdw-password` are mounted as `FDW_USER` and `FDW_PASS` and used as the credentials for the foreign (Oracle) database.  You should update these credentials with the ones provided for your Oracle database connection before tagging any images for deployment, as all of the credentials are used when the pod is first initialized.

If you find you need to change the credentials after the fact (such as if you forgot to set them to the correct values in the first place) the easiest thing to do is drop the persitant data from `/var/lib/pgsql/data` and allow the pod to re-initialize it's environment.

## Connecting a database tool to a database instance

Refer to [Accessing a PostgreSQL Database Hosted in OpenShift](./PortForwardingaDatabase.md) for details on how to connect to an instance of a database hosted in OpenShift using port forwarding.
