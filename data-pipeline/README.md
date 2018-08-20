# BC Registries Event Processor

This project contains a data pipeline for pulling data related to BC Registries events (Registries updates to the records of incorporated entities), using that data to generated Verifiable Credentials, and then delivering those Credentials to [TheOrgBook]((https://github.com/bcgov/TheOrgBook)). The project uses [VON-X](https://github.com/PSPC-SPAC-buyandsell/von-x) as it's Agent to communicate with a [Hyperledger Indy network](https://github.com/hyperledger/indy-node) (eventually [Sovrin](sovrin.org)) and TheOrgBook.

The data pipeline is implemented using the [mara-app](https://github.com/mara/mara-app) framework.

## Mara Example Data Warehouse Project

This project is based on a data warehouse example using the mara framework (https://github.com/mara/mara-example-project).

> A runnable app that demonstrates how to build a data warehouse with mara. Combines the [data-integration](https://github.com/mara/data-integration) and [bigquery-downloader](https://github.com/mara/bigquery-downloader) libraries with the [mara-app](https://github.com/mara/mara-app) framework into a project.

The documentation in this fork of the project describes how to install and run the application.

## Dependencies

The dependencies for the core framework are described in the root Mara project.  This project is setup to use Docker so it doesn't require local setup unless you want to run the application on your local host.

Generated credentials are submitted using bcreg-x, a configured instance of VON-X, to TheOrgBook.  Currently the versions used are:

* VON-Network = https://github.com/bcgov/von-network.git, branch origin/v1.1.2
* TheOrgBook = https://github.com/nrempel/TheOrgBook.git, branch origin/v1.1.2
* BCReg-X = https://github.com/bcgov/con-bc-registries-agent/bcreg-x, master branch

## Running the Event Processor using docker

See the instructions in the [docker folder README](docker/README.MD).

## Runnning the Event Processor using OpenShift

Instructions will be added when the OpenShift integration is implemented.

## The Data Pipelines

Pipeline processes are available through the Mara console, and via bash scripts (for scheduled processing).

![Event Processor Dashboard](https://raw.githubusercontent.com/bcgov/von-bc-registries-agent/master/data-pipeline/docs/bc_registries_dashboard.png "Event Processor Dashboard")

bc_reg_migrate.py
bc_reg_pipeline_initial_load.py
bc_reg_pipeline_post_credentials.py

bc_reg_pipeline.py

There are four data processing pipelines defined:

1. bc_reg_db_init - initializes the BC Registries database and populates initial configuration data
2. bc_reg_event_processor - runs the pipeline to extract data from BC Registries, generate credentials, and submit them to VON
3. test/bc_reg_find_test_clients - loads 12 test clients for processing
4. test/bc_reg_event_processor_json_transform_demo - as above, this version illustrates the use of a JSONBender transform

You need to run the bc_reg_db_init pipeline once, to initialize the database. You can re-run the event processor multiple times.

## Running Pipelines from the Command Line

Note that these scripts depend on the database running under docker, based on the  instructions in the [docker README](docker/README.md).

Use the fifth command shell (or open another - why not?) and run two pipelines:

```
cd mara-example-project/scripts
API_USER=X API_PASSWORD=y ./run-step.sh bcreg/bc_reg_migrate.py
API_USER=X API_PASSWORD=y ./run-step.sh bcreg/bc_reg_pipeline.py
```

The logs and run stats can be viewed in the UI.

NOTE: When you run the pipeline using the user interface, it uses a copy of the code in the docker image.  If you run the pipeline for the command line, it uses the code on your local machine. As such, you can edit the code locally and run it from the command line to test things WITHOUT building it into the docker image.

## Extending Event Processor

The mara setup itself is generic, as long as you run from the provided docker scripts.

There is a single dependency in the following script that references the BC Reg pipelines:

* data-pipeline/app/data_integration/__init__.py

This script initializes the pipelines that are displayed in the UI, so must be customized to include any necessary pipelines.

The BC Registries specific code is all in the data-pipeline/bcreg directory.  Since the pipelines are setup to run Python commands from the command line, there are no code dependencies between the two projects (other than dependencies on the data_integration framework itself).
