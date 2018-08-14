
# VON Event Processor

## Event Processor Overview

The VON Event Processor connects enterprise data sources to a Sovrin edge agent, monitoring the enterprise data source(s) for changes to enterprise data, and generating credential requests that are sent to the network, using a von-x connector.

![VON Event Processor Design ](https://github.com/ianco/von-bc-registries-agent/raw/master/doc/Event-Processor.png "VON Event Processor Design")

The Event processor consists of:

* A framework for running batch processes, and recording and displaying batch status (based on the Mara framework - https://github.com/mara/mara-example-project)
* A batch scheduler, to automate the processing of the above interfaces (based on go-crond - https://github.com/webdevops/go-crond)
* An optional JSON mapper, to support a configuration-based approach for generating output credentials (based on JSONbender - https://github.com/Onyo/jsonbender)
* An output processor, that sends generated credentials to a configured REST endpoint
* A local database, for tracking input events processed and output credentials generated
* A local in-memory cache, to improve performance loading and processing BC Registries corporations
* An admin interface (based on Mara), for monitoring the overall processing status

## BC Registries Data Model

VON Event Processor will be implemented as an event publishing tool for BC Registries, to publish credentials relating to filing events for BC Corporations.

The following BC Registries tables provide information for Incorporation and Address credentials:

![BC Registries Corporation Data Model](https://github.com/ianco/von-bc-registries-agent/raw/master/doc/BCReg-Data-Model.png "BC Registries Corporation Data Model")

The following BC Registries tables are used to determine DBA relationships:

![BC Registries DBA Data Model](https://github.com/ianco/von-bc-registries-agent/raw/master/doc/BCReg-DBA-Data-Model.png "BC Registries DBA Data Model")


## BC Registries Initial Data Load

Determine the corporations to process (any corporation with activity since the last run):

```
:prev_event_id = the previously processed max event (will be zero for the initial load)
:max_event_id = SELECT max(event_id) FROM event;
SELECT distinct(corp_num) from event
  where event_id > :prev_event_id and event_id <= :max_event_id
  and corp_num in
  (SELECT corp.corp_num
    from corporation corp, corp_state state, corp_op_state op_state
    where corp.corp_num = state.corp_num
      and state.end_event_id is null
      and state.state_typ_cd = op_state.state_typ_cd
      and op_state.op_state_typ_cd = 'ACT'
      and corp.corp_typ_cd in ('A','LLC','BC','C','CUL','ULC'))
  order by corp_num;
```

This provides a list of Corporations to be processed.

Now determine the most recent event for each active corporation:

```
for each :corp_num (from previous query):
    SELECT max(event_id) from event
    where corp_num = :corp_num
      and event_id > :prev_event_id and event_id <= :max_event_id
```

Note that for the initial data load the event id is not used (credentials are generated based on the corporations's current status).  However for future updates the event id must be saved (in order to differentiate future updates based on event id).

The Incorporation, Address and DBA Credentials are generated per the above data model, based on the corporation's current status.

## BC Registries Event Monitoring

## Event Processor Data Model

The following data model will be implemented within the Event Processor to support conversion of the BC Registries dataset.  The following requirements are supported:

* Publish a sub-set of Event/Filing Types in the initial release, however support inclusion of additional Types in later releases
* Support publishing of specific companies or corporations
* Support re-start if the processing fails (re-start from the point of failure)
* Support for administrative functions (update of configuration, monitoring of event processing)

The Event Processor data model is illustrated as follows:

![VON Event Processor Data Model](https://github.com/ianco/von-bc-registries-agent/raw/master/doc/Event-Processor-Data-Model.png "VON Event Processor Data Model")

Table descriptions are as follows:

Table EVENT_LOG: tracks each processed Event - a record is added for each Event processed:

| Column | Description |
| ------ | ----------- |
| EVENT_ID | Last event id processed |
| FILING_TYPE | Filing type of last event id |
| CORP_NUM | Corporation of last event id |
| FILING_DATA | Json blob with data of interest (may vary based on filing type) |
| CREDS_DATA | Json blob with pointers to any generated credentials |
| EVENT_DATE | Date of the event, from corp reg database |
| PROCESSED_DATE | Date credentials were created and sent |

Table EVENT_BY_FILING_TYP: Last EVENT_ID processed for each FILING_TYPE:

| Column | Description |
| ------ | ----------- |
| EVENT_ID | Last event id processed |
| FILING_TYPE | Filing type of last event id |

Table EVENT_BY_CORP_FILING: Last EVENT_ID processed for each CORP_NUM/FILING_TYPE:

| Column | Description |
| ------ | ----------- |
| EVENT_ID | Last event id processed |
| FILING_TYPE | Filing type of last event id |
| CORP_NUM | Corporation of last event id |

Table CREDENTIAL_SCHEMA: description of each output credential supported:

| Column | Description |
| ------ | ----------- |
| CREDENTIAL_TYP_CD | Identifies credential type |
| CREDENTIAL_NAME | Description of credential |
| CREDENTIAL_SCHEMA | Data format required for credential |

Table EVENT_CREDENTIAL_MAP: mapping between input events and output credentials

| Column | Description |
| ------ | ----------- |
| EVENT_TYP_CD | Input event type |
| FILING_TYP_CD | Input filing type |
| CREDENTIAL_TYP_CD | Output credential type |
| MAPPING_SCRIPT | Mapping between input event and output credential |

Table CREDENTIAL_LOG: generated output credentials generated

| Column | Description |
| ------ | ----------- |
| EVENT_ID | Last event id processed |
| FILING_TYPE | Filing type of last event id |
| CORP_NUM | Corporation of last event id |
| CREDENTIAL_TYP_CD | Identifies credential type |
| CREDS_DATA | Json blob with pointers to any generated credentials |
| PROCESSED_DATE | Date credentials were created and sent |


## BC Registries Event Processing description

The BC Registries event processing will execute the following steps:

* For each supported Filing Type:
    * Find last Event ID processed from the EVENT_BY_FILING_TYP table
    * From BC Reg, select all events with matching filing type and greater Event ID
    * For each event:
         * Get corporation number from event
         * Load all corporation data from BC Reg
         * Construct event data msg
         * Add record to EVENT_LOG table
         * Add records to EVENT_BY_FILING_TYP and EVENT_BY_CORP_FILING recording event id

To process these events and generate output credentials:

* For each unprocessed record in EVENT_LOG:
    * Determine output credentials supported (from EVENT_CREDENTIAL_MAP)
    * For each credential type:
        * Execute mapping to convert input event data to output credential data
        * Save credential data to CREDENTIAL_LOG and update EVENT_LOG

To send credentials to von-x edge agent:

* For each unprocessed credential in CREDENTIAL_LOG:
    * Read credential data and send to von-x
