
# VON Event Processor

## Event Processor Overview

The VON Event Processor connects enterprise data sources to a Sovrin edge agent, monitoring the enterprise data source(s) for changes to enterprise data, and generating credential requests that are sent to the network, using a von-x connector.

![VON Event Processor Proposed Design](https://github.com/ianco/von-bc-registries-agent/raw/master/doc/Event-Processor.png "VON Event Processor Proposed Design")

The Event processor consists of:

* A set of input interfaces - a REST listener, filesystem monitor, database monitor (and potentially others via a plug-in architecture)
* A batch scheduler, to automate the processing of the above interfaces
* An event-mapper, that maps and generates output credentials based on input events
* An output processor, that sends generated credentials to a configured REST endpoint
* A local database, for tracking input events processed and output credentials generated
* An admin interface, for monitoring the overall processing status

The VON Event Processor is built based on the Django framework, and incorporates the following modules:

* Django Background Tasks (http://django-background-tasks.readthedocs.io/en/latest/) - task scheduling for the input interfaces
* Pandas (http://pandas.pydata.org/pandas-docs/stable/) - supports conversion between input Event and output Credential data formats (note under review, other libraries are also being considered, such as https://github.com/fabianvf/schema-transformer)

## BC Registries Event Monitor

VON Event Processor will be implemented as an event publishing tool for BC Registries, to publish credentials relating to filing events for BC Corporations.

For the initial implementation, the following filing events will be published:

| Filing_Typ_Cd | Filing_Typ_Class | Short_Desc | Count |
| ------------- | ---------------- | ---------- | ----: |
| FRREG | FRMFIL | Stmt of Registration of Partnership or Sole Prop | 539,832 |
| ICORP | FILING | Incorporate a Company | 163,726 |
| NOCAD | FILING | Change Address Information | 164,530 |

Note that there are currently over 11 million Events in the BC Registries database, including over 8 million Filings.  The above represents about 10% of BC Registries Events.  The remainder of the Events will be published in subsequent releases of the Event Processor.

For each event, the related company information will be queried from the BC Registries database and sent to the Event Processor for processing.  The following set of BC Registries tables will be included:

| BC Reg. Table | Description |
| ------------- | ----------- |
| CORPORATION | Main corporation table (key is CORP_NUM) |
| BUSINESS_DESCRIPTION | Description of business |
| CORP_FLAG | Various attributes of the corporation |
| CORP_INVOLVED | Jurisdiction |
| CORP_NAME | Company name or doing business as |
| CORP_PARTY, ADDRESS | Officers and link to address |
| CORP_STATE | Company status |
| EMAIL_ADDRESS | Email contact |
| JURISDICTION | Jurisdiction |
| OFFICE, ADDRESS | Company address |
| TILMA_INVOLVED | Related to NUANS name? |

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
