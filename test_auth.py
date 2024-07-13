"""Test DuckDB auth to Azure Storage Account with Azure SDK logging enabled to debug auth issues"""

import os
import duckdb

os.environ['AZURE_LOG_LEVEL'] = 'verbose'

duckdb.sql("CREATE SECRET azduckdb (TYPE AZURE, PROVIDER CREDENTIAL_CHAIN, SCOPE 'az://azduckdb.blob.core.windows.net/')")
duckdb.sql("SELECT count(*) FROM 'az://azduckdb.blob.core.windows.net/data/HuggingFaceFW/fineweb/CC-MAIN-2013-20/000_00000.parquet'")
