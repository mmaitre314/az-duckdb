"""Various utility functions shared across notebooks."""

from datetime import datetime, timezone, timedelta
from azure.core.credentials import TokenCredential
from azure.storage.blob import BlobServiceClient, generate_container_sas

def get_connection_string(credential:TokenCredential, account_name: str, container_name: str) -> str:
    """Generates a connection string for accessing a Storage Container using a user-delegation SAS."""

    start_time = datetime.now(timezone.utc)
    expiry_time = start_time + timedelta(days=1)

    client = BlobServiceClient(f"https://{account_name}.blob.core.windows.net", credential=credential)

    user_delegation_key = client.get_user_delegation_key(start_time, expiry_time)

    sas_token = generate_container_sas(
        account_name = account_name,
        container_name = container_name,
        user_delegation_key = user_delegation_key,
        resource_types = "sco",
        permission = "rl",
        start = start_time,
        expiry = expiry_time,
    )

    return f'DefaultEndpointsProtocol=https;AccountName={account_name};EndpointSuffix=core.windows.net;SharedAccessSignature={sas_token}'
