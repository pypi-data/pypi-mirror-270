![Rabbit in a Blender](resources/img/rabbitinablenderlogo.png)
===========

**Rabbit in a Blender (RiaB)** is an [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) pipeline [CLI](https://nl.wikipedia.org/wiki/Command-line-interface) to transform your [EMR](https://en.wikipedia.org/wiki/Electronic_health_record) data to [OMOP](https://www.ohdsi.org/data-standardization/the-common-data-model/).

Why the name 'Rabbit in a Blender'? It stays in the rabbit theme of the [OHDSI](https://www.ohdsi.org) tools, and an ETL pipeline is like putting all your data in a blender. 

No rabbits were harmed during the development of this tool!

# Introduction

Extract-Transform-Load (ETL) processes are very complex and are mainly crafted by highly skilled data engineers. The process of transforming the electronic medical record (EMR) data into the observational medical outcomes partnership (OMOP) common data model (CDM) is no exception. The mapping process of the source values to standard concepts is mostly done by subject matter experts, who lack the knowledge of programming the ETL process. Wouldn’t it be nice if we could drastically simplify the ETL process, so that you don’t need seasoned data engineers to start the OMOP CDM journey. Imagine that you just save your queries, Usagi comma separated value (CSV) text files and custom concept CSV’s on disk, and run a command line interface (CLI) tool that does all the ETL magic automatically. 


# Concept

The main strength of the CDM is its simplified scheme. This scheme is a relational data model, where each table has a primary key and can have foreign keys to other tables. Because of the relational data model, we can extract the dependencies of the tables from the scheme. For example, the provider table is dependent on the care_site table, which is in its turn dependent on the location table. If we flatten that dependency graph, we have a sequence of ETL steps that we need to follow to have consistent data in our OMOP CDM. These ETL steps can be automated, so a hospital can focus its resources on the queries and the mapping of the concepts. The automated ETL consists of multiple tasks. It needs to execute queries, add custom concepts, apply the Usagi source to concept mapping, and do a lot of housekeeping. An example of that housekeeping is the autonumbering of the OMOP CDM primary keys, for which the ETL process needs to maintain a swap table that holds the key of the source table and the generated sequential number of the CDM table’s primary key. Another example of the housekeeping is the upload and processing of the Usagi CSV’s and also the upload and parsing of the custom concept CSV’s. In an ETL process data is divided in zones (cfr. the [zones in a data lake](https://www.oreilly.com/library/view/the-enterprise-big/9781491931547/ch01.html#zones_of_a_typical_data_lake)). The raw zone holds the source data (for example the data from the EMR), the work zone holds all the house keeping tables of the ETL process and the gold zone holds our final OMOP CDM.
After designing the architecture, the implementation needs to be developed. We have two options to choose from: configuration and convention as design paradigm. We choose convention over configuration, because it decreases the number of decisions the user has to make and eliminates the complexity. As convention a specific folder structure is adopted (see [our mappings as example](https://github.com/RADar-AZDelta/AZDelta-OMOP-CDM)). A folder is created for each OMOP CDM table, where the SQL queries are stored to fill up the specific CDM table. In the table folders we also have for each concept column a sub folder. Those concept column sub folders hold our Usagi CSV’s (files ending with _usagi.csv). We also have a custom folder in the concept column sub folder, that holds the custom concept CSV’s (files ending with _concept.csv). With this convention in place, our ETL CLI tool has everything it needs to do its magic.
One final requirement we want to build in the ETL CLI tool, is that each ETL step is an atomic operation, it either fails or succeeds, so that there is no possibility to corrupt the final OMOP CDM data.

# Notes on Use

You will need to run the cleanup command when concept mappings change in your existing Usagi CSV's. The cleanup is not necessary when you add new queries or add additional Usagi mappings.

The measurement table has the **measurement_event_id** field, the observation table has the **observation_event_id** field, the cost table has the **cost_event_id** field, the episode_event table has the **event_id** field and the fact_relationship table has the **fact_id_1** and **fact_id_2** fields. All those fields are foreign keys to almost all OMOP CMD tables. Put the source id in the event_id field and the reffered table in the field_concept_id field. An example of how to implement this in the sql-file:
- Linking two people with a personal relationship in the fact_relationship table:
```sql
select distinct
  'person' as domain_concept_id_1  -- foreign table name as string
  ,pr.person_nr_1 as fact_id_1	-- same key as used as when adding the person to the person table
  ,'person' as domain_concept_id_2  -- foreign table name as string	
  ,pr.person_nr_1 as fact_id_2	-- same key as used as when adding the person to the person table
  ,pr.relationship as relationship_concept_id  -- column with sourceCodes specifying the relationship and mapped in a _usagi.csv file in the relationship_concept_id folder
from person_relationships pr
```

The **custom concepts** get added to the **source_to_concept_map** table. The concept_code is used as the source_code, the newly assigned (>2.000.000.000) concept_id is used as the target_concept_id. The custom concepts are also added to the **usagi table**, using the concept_code as sourceCode and the newly assigned concept_id as the conceptId. The custom concepts can be used **as mapping targets** in two ways:
- No explicit mapping in usagi table: the source code (as assigned in your ETL sql file) is mapped to the custom concept where it equals the concept_code
- Explicit mapping in usagi: map a sourceCode in the usagi table to a custom concept by setting its targetConceptId equal to the concept_code of the custom concept.

Examples:

* mapping "Cemiplimab", with source_code *M1*:
    - Add custom concept for cemiplimab with concept_code = *M1*, it gets a assigned a concept_id automatically, no usagi-entry required
    - Optionally add an usagi-entry for clarity, mapping sourceCode = *M1* to targetConceptId = *M1*, the concept_id gets filled in automatically
* mapping "Atezolizumab + Cemiplimab", with source_code *C12*:
    - Add custom concept for cemiplimab with concept_code = *M1*, it gets a assigned a concept_id automatically
    - Add two usagi-entries: mapping sourceCode *C12* to targetConceptId = *1792776* (standard code for atezolizumab) and to targetConceptId = *M1*
    
    ALTERNATIVELY:

    - Add custom concept for cemiplimab with concept_code = *C12*, it gets a assigned a concept_id automatically, no usagi-entry required
    - Add only one usagi-entry, mapping sourceCode *C12* to targetConceptId = *1792776* (standard code for atezolizumab), the second mapping of *C12* to custom concept with concept_code = *C12* is done automatically.

# ETL flow

Most CDM tables have foreign keys (FKs) to other tables. Some tables can be processed in parallel by the ETL engine, because they have no FKs dependencies between them, others have to be processed in a specific order.

The ETL flow for v5.4 is as follows:

```
└──vocabulary                                 # custom concepts must have a vocabulary
  └──cdm_source
  ├──metadata
  ├──cost
  ├──fact_relationship
  └──location
    └──care_site
      └──provider
        └──person
          ├──condition_era
          ├──death
          ├──dose_era
          ├──drug_era
          ├──episode
          ├──observation_period
          ├──payer_plan_period
          ├──specimen
          └──visit_occurrence
            ├──episode_event
            └──visit_detail
              ├──condition_occurrence
              ├──device_exposure
              ├──drug_exposure
              ├──measurement
              ├──note
              ├──observation
              └──procedure_occurrence
                └──note_nlp
```

Because the event FKs (e.g. observation_event_id, cost_event_id, measurement_event_id, etc.), can point to almost any table, the event FK's are processed in a second, seperate ETL step.

# Installation

see [installation](docs/installation.md)

# Database engines

For the moment we only implemented a **BigQuery** and **SQL Server** backend for the ETL process, because this is what our hospital uses. Other database technologies as ETL backend can be implemented.

see [database engines](docs/database_engines.md)


Config
========

With the addition of additional database engines, we switched to a [ini](https://en.wikipedia.org/wiki/INI_file) config file for database specific configurations.
This makes the CLI arguments less cumbersome.

RiaB searches for the ini config file by using the following cascade:
1. CLI --config argument
2. RIAB_CONFIG environment variable (the RIAB_CONFIG environment variable can also be placed in a .env file in the current folder)
3. riab.ini in the current folder

Below an example of a config:

```ini
[riab]
db_engine=bigquery
; Required
; What database are you using? (bigquery or sql_server)
max_parallel_tables=9
; Optional
; The number of tables, that RiaB will process in parallel. On a server with a performant db_engine (like BigQuery), this number can be high. On slower machines/database set this to a low number to avoid overwhelming the database or server. (if you have problems importing the vocabularies, try lowering this number to 1 or 2)
; The default value is 9
max_worker_threads_per_table=16
; Optional
; The number of worker threads that RiaB will use, per table, to run stuff in parallel. On a server with a performant db_engine (like BigQuery), this number can be high. On slower machines/database set this to a low number to avoid overwhelming the database or server.
; The default value is 16

[bigquery]
credentials_file=service_account.json
; Optional
; The credentials file must be a service account key, stored authorized user credentials, external account credentials, or impersonated service account credentials. (see https://google-auth.readthedocs.io/en/master/reference/google.auth.html#google.auth.load_credentials_from_file)
; Alternatively, you can also use 'Application Default Credentials' (ADC) (see https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login)
location=EU
; Location where to run the BigQuery jobs. Must match the location of the datasets used in the query. (important for GDPR)
project_raw=my_omop_project
; Optional
; Can be handy if you use jinja templates for your ETL queries (ex if you are using development-staging-production environments). Must have the following format: PROJECT_ID
dataset_work=my_omop_project.work
; The dataset that will hold RiaB's housekeeping tables. Must have the following format: PROJECT_ID.DATASET_ID
dataset_omop=my_omop_project.omop
; The dataset that will hold the OMOP tables. Must have the following format: PROJECT_ID.DATASET_ID
dataset_dqd=my_omop_project.dqd
; The dataset that will hold the data quality tables. Must have the following format: PROJECT_ID.DATASET_ID
dataset_achilles=my_omop_project.achilles
; The dataset that will hold the data achilles tables. Must have the following format: PROJECT_ID.DATASET_ID
bucket=gs://my_omop_bucket/upload
; The Cloud Storage bucket uri, that will hold the uploaded Usagi and custom concept files. (the uri has format 'gs://{bucket_name}/{bucket_path}')

[sql_server]
server=127.0.0.1
; The SQL Server host
port=1433
; The SQL Server port (defaults to 1433)
user=riab
; The SQL Server user
password=?????
; The SQL Server password
omop_database_catalog=omop
; The SQL Server database catalog that holds the OMOP tables
omop_database_schema=dbo
; The SQL Server database schema that holds the OMOP tables
work_database_catalog=work
; The SQL Server database catalog that holds the RiaB's housekeeping tables
work_database_schema=dbo
; The SQL Server database schema that holds the RiaB's housekeeping tables
dqd_database_catalog=dqd
; The SQL Server database catalog that holds the data quality tables
dqd_database_schema=dbo
; The SQL Server database schema that holds the data quality tables
achilles_database_catalog=achilles
; The SQL Server database catalog that holds the data achilles tables
achilles_database_schema=dbo
; The SQL Server database schema that holds the data achilles tables
raw_database_catalog=raw
; Optional
; The SQL Server database catalog that holds the raw tables
raw_database_schema=dbo
; Optional
; The SQL Server database schema that holds the raw tables
; Changing this flag requires that you re-run the following commands: --create-db, --cleanup and --import-vocabularies
; Default value is false
; Set to false for better data quality
disable_fk_constraints=false
; Optional
; By default foreign key constraints are disabled, because they are very resource consuming. (true or false are allowes as value)
bcp_code_page=ACP
; Optional
; Default value is ACP. For more info see https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver16#-c--acp--oem--raw--code_page-
```

CLI Usage
========

* **Options**:
    |  command | help  
    |---|---
    | -h, --help | Show help message and exit
    | -v, --verbose | Verbose logging (logs are also writen to a log file in the systems tmp folder)
    | -V, --version | The current installed version
    | --config | Optional path to the ini config file that holds the database engine configuration. Alternatively set the RIAB_CONFIG environment variable, pointing to the ini file. Or place a riab.ini file in the current directory.

* **ETL Commands**:
    |  command | help  
    |---|---    
    | -tdc, --test-db-connection | Test the database connection
    | -cd, --create-db | Create the OMOP CDM tables
    | -cf, --create-folders [PATH] | Create the ETL folder structure that will hold your queries, Usagi CSV's an custom concept CSV's.
    | -i, --import-vocabularies [VOCABULARIES_ZIP_FILE] | Extracts the vocabulary zip file (downloaded from the Athena website) and imports it into the OMOP CDM database.
    | -r [PATH], --run-etl [PATH] | Runs the ETL, pass the path to ETL folder structure that holds your queries, Usagi CSV's an custom concept CSV's.
    | -c, --cleanup [TABLE] | Cleanup all the OMOP tables, or just one. Be aware that the cleanup of a single table can screw up foreign keys! For instance cleaning up only the 'Person' table, will result in clicical results being mapped to the wrong persons!!!!
    | -dq, --data-quality | Check the data quality and store the results.
    | -dqd, --data-quality-dashnoard | View the results of the data quality checks.
    | --print-etl-flow | Print the sequence in which the ETL tables that will be processed

* **Run ETL specific command options (-r [PATH], --run-etl [PATH]):**
    |  command | help  
    |---|---  
    | -t [TABLE], --table [TABLE] | Do only ETL on this specific OMOP CDM table (this argument can be used multiple times). (ex: --run-etl ~/git/omop-cdm/ -t cdm_source -t metadata -t vocabulary -t location). This option is only usefull while developing the ETL queries or testing Usagi mappings, to speed up the ETL process. Do not use in production.
    | -q [PATH], --only-query [PATH] | Do ETL for a specified sql file in the CDM folder structure (this argument can be used multiple times). (ex: measurement/lab_measurements.sql). This option is only usefull while developing a specific ETL query, to speed up the ETL process. Do not use in production.
    | -s, --skip-usagi-and-custom-concept-upload | Skips the parsing and uploading of the Usagi and custom concept CSV's. Skipping results in a significant speed boost.
    | -sa, --process-semi-approved-mappings | In addition to 'APPROVED' as mapping status, 'SEMI-APPROVED' will be processed as valid Usagi concept mappings.
    | -se, --skip-event-fks-step | Skip the event foreign keys ETL step.

* **Data quality specific command options (-dq, --data-quality):**
    |  command | help  
    |---|---  
    | --json [PATH] | Save the data quality result as [JSON file](https://ohdsi.github.io/DataQualityDashboard/articles/DataQualityDashboard.html#viewing-results) for use in the OHDSI [Data Quality Dashboard](https://ohdsi.github.io/DataQualityDashboard/).

* **Data quality dashboard specific command options (-dqd, --data-quality-check):**
    |  command | help  
    |---|---  
    | --port [PORT] | The port the dashboard schould listen on.

CLI Examples
========

Create the OMOP CDM database:
```bash
riab --create-db
```

Import your downloaded vocabularies (from [Athena](https://athena.ohdsi.org/vocabulary/list)) zip file:
```bash
riab --import-vocabularies ./vocabulary_20240329.zip
```

Create the ETL folder structure:
```bash
riab --create-folders ./OMOP_CDM
```     

Run full ETL:
```bash
riab --run-etl ./OMOP-CDM
```

Run ETL on one table:
```bash
riab --run-etl ./OMOP-CDM \
  --table provider
```

Run ETL without re-upload of Usagi CSV's and custom concept CSV's:
```bash
riab --run-etl ./OMOP-CDM \
  --skip-usagi-and-custom-concept-upload
```

Run ETL for a specified sql file in the CDM folder structure. (ex: measurement/lab_measurements.sql)
```bash
riab --run-etl ./OMOP-CDM \
  --skip-usagi-and-custom-concept-upload \
  --skip-event-fks-step \
  --only-query measurement/lab_measurements.sql
```

Run ETL with SEMI-APPROVED concepts during ETL testing in dev branch
```bash
riab --run-etl ./OMOP-CDM \
  --process-semi-approved-mappings
```

Cleanup all tables:
```bash
riab --cleanup
```

Cleanup one table (example provider table):
```bash
riab --cleanup provider
```

Data quality check:
```bash
riab --data-quality
```

Data quality check (export result to JSON):
```bash
riab --data-quality
  --json dqd_result.json
```

Data quality dashboard (default port = 8050):
```bash
riab --data-quality-dashboard
  --port 8888
```


BigQuery
========

There are 2 ways to [authenticate](https://cloud.google.com/docs/authentication/getting-started) with GCP:
* Use a [Service Account key file](https://cloud.google.com/docs/authentication/production) with **--google-credentials-file** cli option
* When developing or testing you can use [Application Default Credentials (ADC)](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login)

    [Install](https://cloud.google.com/sdk/docs/install-sdk#installing_the_latest_version) the gcloud CLI!

    For example for windows run the folowing powershell script:
    ```powershell
    (New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")
    & $env:Temp\GoogleCloudSDKInstaller.exe
    ```

    Authenticate:
    ```bash
    # login
    gcloud auth application-default login
    # set our project
    PROJECT_ID="our_omop_etl_project_id_on_GCP" #you need to change this
    gcloud config set project ${PROJECT_ID}
    # you can alternatively set the project_id with a environment variable
    export GOOGLE_CLOUD_PROJECT=${PROJECT_ID}
    ```

    More info can also be found in the [Python API for GCP authentication](https://googleapis.dev/python/google-api-core/1.19.1/auth.html#overview)

The creation of different datasets in needed before config settings.

SQL Server
==========

Difference between [catalogue, schema](https://medium.com/@diehardankush/catalogue-schema-and-table-understanding-database-structures-ec54347f85c7) in the riab.ini.

### Prerequisites

Only SQL Server 2017 or later are supported.

RiaB has a dependency on the [BCP utility](https://learn.microsoft.com/en-us/sql/tools/bcp-utility) to upload the CSV's to SQL Server.

Add the BCP dependency to the PATH environment variable.

Install bcp on machine that will run RIAB:

1. Go to website [bcp utility](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver16)
2. Download ODBC driver (x64) and command line util (x64) for windows
3. Install both
4. Restart machine, to update PATH environment variables

Validate that you can run the BCP command: 
```
bcp.exe --version
```

**Warning**: Under linux, the bcp command uses the current [locale](https://www.tecmint.com/set-system-locales-in-linux/) to convert floats. So make sure your current locale has a . as decimal sepertor!

```bash
sudo localectl set-locale LC_NUMERIC=en_IN.UTF-8
```

### SQL Server rights

The SQL user (configured in the riab.ini configuration file) requires the [db_ddladmin](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/database-level-roles?view=sql-server-ver16) role (see line user=riab). Ask your Database Adminstrator (DBA), to create the user and grant the required rights.


```sql
CREATE USER riab WITH password='?????';
EXEC sp_addrolemember 'db_datareader', 'riab';
EXEC sp_addrolemember 'db_datawriter', 'riab';
EXEC sp_addrolemember 'db_ddladmin', 'riab';
```

### SQL Server databases and schemes


The creation of different database [schemas](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-database-schema) or [databases](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-database-transact-sql) (work, omop, dqd, achilles) is needed.

```sql
CREATE DATABASE omop; 
--dbo is default schema for a new database
CREATE DATABASE work;
CREATE DATABASE dqd;
CREATE DATABASE achilles;
```

or

```sql
CREATE DATABASE omop;
USE omop;
CREATE SCHEMA omop;
CREATE SCHEMA work;
CREATE SCHEMA dqd;
CREATE SCHEMA achilles;
```

Change the recovery mode to Simple. (ask your DBA for best practices)

```sql
ALTER DATABASE omop SET RECOVERY SIMPLE;
ALTER DATABASE work SET RECOVERY SIMPLE;
ALTER DATABASE dqd SET RECOVERY SIMPLE;
ALTER DATABASE achilles SET RECOVERY SIMPLE;
```

or

```sql
ALTER DATABASE omop SET RECOVERY SIMPLE;
```

**Tip**: Make sure you've chosen the right [collation](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-database-transact-sql?view=azuresqldb-current&preserve-view=true&tabs=sqlpool#collation_name), that is compatible with your raw data.

### Linked server to the raw data

If the raw EMR data is not on the same server defined in the riab.ini file, you will need to ask your database administrator, to add it as linked server.

Example:

```sql
USE master;  
GO  
EXEC sp_addlinkedserver   
   N'raw-emr-database-server,1433',  
   N'SQL Server';
GO

EXEC sp_addlinkedsrvlogin
   @rmtsrvname = N'raw-emr-database-server,1433',
   @useself = N'False',
   @locallogin = N'sa',
   @rmtuser = N'remote_user',
   @rmtpassword = N'???';
GO

sp_testlinkedserver N'raw-emr-database-server,1433';
```

### Azure SQL Server

Ensure SQL allows non- Entra ID users
   1. Open Azure portal
   2. Go to SQL **server** instance (not database)
   3. Under settings, make sure "Support only Microsoft Entra authentication for this server" is **NOT** checked.
   4. You might need to [scale up](https://learn.microsoft.com/en-us/azure/azure-sql/database/scale-resources?view=azuresql) the number of max vCores to speed up for instance the import of the vocabularies. Especially with a high **max_parallel_tables** value, setting max vCores to 16 or more is recommended.

![image](https://github.com/RADar-AZDelta/Rabbit-in-a-Blender/assets/1187178/1ac67835-b467-4278-8c9a-171af0a98aa8)

   5. You need to use the same database catalog for omop, work, dqd and achilles. Because of the following limitation: To change database context to a different database in Azure SQL Database, you must create a new connection to that database. (see [T-SQL differences between SQL Server and Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/transact-sql-tsql-differences-sql-server?view=azuresql)). So the omop_database_catalog, work_database_catalog, dqd_database_catalog and achilles_database_catalog must have the same value in the riab.ini!
   6. It is best practices to avoid the usage of special characters (ex: the minus sign) in the name of the database catalog and schemes. 

Windows
========

Use a terminal that supports colors (like [Hyper](https://hyper.is/))

Container
========

The container holds all the necessary components (Python, Java, BCP, ...)

```bash
docker run \
  --rm \
  -it \
  -v ./riab.ini:/riab.ini \
  -v .:/cdm_folder \
  -e RIAB_CONFIG=/riab.ini \
  ghcr.io/radar-azdelta/rabbit-in-a-blender:latest --version
```

You can create an alias for this command, an put it in your .bashrc file. For example:

```bash
alias riab='docker run \
  --rm \
  -it \
  -v ./riab.ini:/riab.ini \
  -v .:/cdm_folder \
  -e RIAB_CONFIG=/riab.ini \
  ghcr.io/radar-azdelta/rabbit-in-a-blender:latest'

riab --version
riab -r /cdm_folder -v
```

Authors
========

* [Lammertyn Pieter-Jan](https://github.com/pjlammertyn)
* [De Jaeger Peter](https://github.com/peterdejaeger)

License
========

Copyright © 2024, [RADar-AZDelta](mailto:radar@azdelta.be).
Released under the [GNU General Public License v3.0](LICENSE).

***
