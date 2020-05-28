
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from  azure.core.exceptions import ResourceNotFoundError, ResourceExistsError
from datetime import datetime


class AzureBlobAccessor:
    """ Class helping access blobs in Azure for the purpose of writing and reading Sensor information.

    """

    def __init__(self, blob_container_name: str, connection_string: str):
        """ initialize the class.
        """
        self._blob_container_name = blob_container_name
        # Create the BlobServiceClient object which will be used to create a container client
        self._blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # Create the container if it doesn't exist.
        try:
            self._container_client = self._blob_service_client.create_container(blob_container_name)
        except ResourceExistsError:
            print(f"Container name: {blob_container_name} Already exists.")
        except Exception as ex:
            print(f"Container cannot be created due to: {ex}")

    def write_sensor_measurement(self, sensor_name: str, measurement: str):
        # Create a blob client using the local file name as the name for the blob
        blob_client = self._blob_service_client.get_blob_client(
            container=self._blob_container_name,
            blob=sensor_name)

        print("Uploading to Azure Storage as blob:\n\t" + sensor_name)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            blob_client.append_block(f"{sensor_name},{current_time},{measurement}\n")
        except ResourceNotFoundError as ex:
            print(f" Cannot Write to Blob that doesn't exist. \n {ex} \n Attempting to create it.")
            # This needs to be done only once, and it overrides the blob:
            blob_client.create_append_blob()
            blob_client.append_block(f"SensorName,CurrentTime,Measurement\n")
            blob_client.append_block(f"{sensor_name},{current_time},{measurement}\n")
