# Database Schema Documentation

Databases are documented using [SchemaSpy](https://github.com/bcgov/SchemaSpy).  The documentation of the Oracle database requires Oracle JDBC drivers.  Due to licensing restrictions the image for the associated pod has been built manually and pushed into the project's tools project.

## BC Registries SchemaSpy Instance (schema-spy-oracle)

This instance is protected by basic authentication.  The credentials are randomly generated for each deployment.

To accomplish this, we use a little bit of OpenShift magic.  We use a combination of config maps and secrets to inject a customized Caddy configuration file into the running SchemaSpy instance and define the set of credentials used for basic authentication.  To orchestrate and automate the process we use features of the [OpenShift Scripts](https://github.com/BCDevOps/openshift-developer-tools/blob/master/bin/README.md) used to setup and maintain OpenShift environments.

The [schema-spy-oracle-deploy](./schema-spy-oracle-deploy.json) template performs most of the heavy lifting.  It defines the nesessary plumbing to mount the custom Caddy configuration into a running SchemaSpy instance and defines the secrets to hold the credentials, along with some additional SchemaSpy settings to redirect the output to the correct folder.

The custom [Caddyfile](./Caddyfile) defines the routes and basic authentication that allow OpenShift to perform health checks while protecting the database documentation.

The [schema-spy-oracle-deploy.overrides.sh](../../schema-spy-oracle-deploy.overrides.sh) script generates the configuration file for the config map which contains the Caddyfile, and generates a set of random credentials for the deployment.

When an instance of the SchemaSpy image is started, it's Caddyfile is replaced with a copy of the one from the config map, and the basic authorization credentials are sourced from environment variables that are retrieving their values from secrets.