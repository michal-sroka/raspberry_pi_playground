import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from  azure.core.exceptions import ResourceNotFoundError, ResourceExistsError
from datetime import datetime

# Below code follows tutorial from: https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python

# Retrieve the connection string for use with the application. The storage
# connection string is stored in an environment variable on the machine
# running the application called AZURE_STORAGE_CONNECTION_STRING. If the environment variable is
# created after the application is launched in a console or with Visual Studio,
# the shell or application needs to be closed and reloaded to take the
# environment variable into account. RASPBERRYPI_
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
sensor_data_file_name = "temperature4"
# printing environment variables
# print(os.environ)

print(f'Got the string: {connect_str}')
# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Create a unique name for the container
# "quickstart" + str(uuid.uuid4())
container_name = "sensors"

# Create the container
try:
    container_client = blob_service_client.create_container(container_name)
except ResourceExistsError:
    print(f"Container name: {container_name} Already exists.")
except Exception as ex:
    print(f"Container cannot be created due to: {ex}")

# Create a blob client using the local file name as the name for the blob
blob_client = blob_service_client.get_blob_client(container=container_name, blob=sensor_data_file_name)


print("\nUploading to Azure Storage as blob:\n\t" + sensor_data_file_name)


current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
try:
    blob_client.append_block(f"sensor1,{current_time},32\n")
except ResourceNotFoundError as ex:
    print(f" Cannot Write to Blob that doesn't exist. \n {ex} \n Attempting to create it.")
    # This needs to be done only once, and it overrides the blob:
    blob_client.create_append_blob()
    blob_client.append_block(f"sensor1,{current_time},32\n")







