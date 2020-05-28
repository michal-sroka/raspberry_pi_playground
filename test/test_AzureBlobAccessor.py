
import sys
import os, uuid

sys.path.append('c:\\dev\\projects\\raspberry_pi_playground')


from AzureAccess.AzureBlobAccessor import AzureBlobAccessor


connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
sensor_data_file_name = "test"
sensor_name = "TempSensors"

azure_accessor = AzureBlobAccessor(sensor_data_file_name, connect_str)
azure_accessor.write_sensor_measurement(sensor_name, "32.34")
