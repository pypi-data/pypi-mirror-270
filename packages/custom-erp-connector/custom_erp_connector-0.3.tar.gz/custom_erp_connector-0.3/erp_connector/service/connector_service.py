import json
import os

from erp_connector.clients.one_integration_client import OneIntegrationClient
from erp_connector.db.db_loader import ConnectionLoader
from erp_connector.utils.file_utils import zip_folder
from erp_connector.service.sqlite_service import insert_data, update_data
from erp_connector.config.config_loader import CustomErpConnectorConfig, ConfigLoader


def process_connector(config_path):
    print("running process connector")
    row_id = insert_data()
    status = 'DATA_INITIATED'
    command = None
    command_id = None
    try:
        config_loader = ConfigLoader(config_path)
        custom_erp_connector_config = config_loader.load()
        db_connector = ConnectionLoader.load_connector(custom_erp_connector_config)
        db_connector.connect_db()
        one_integration_client = OneIntegrationClient(custom_erp_connector_config)
        get_command_response = one_integration_client.get_command()
        get_command_result = get_command_response['result']
        command = get_command_result['command']
        command_id = get_command_result['commandId']
        update_data(row_id,command,command_id,status)

        if command == 'DATA_EXTRACTION':
            command_id = get_command_result['commandId']
            json_data = get_command_result['metadata']['erpConfig']['tables']
            query_metadata_list = db_connector.generate_query(None)

            current_path = os.getcwd()
            output_folder_path = os.path.join(current_path, 'output')
            zip_folder_path = os.path.join(current_path, 'output_zip')
            for query_metadata in query_metadata_list:
                table_name = query_metadata["tableName"]
                select_query = query_metadata["query"]
                print(f"select_query: {select_query}")
                json_data = db_connector.fetch_data(select_query)
                local_file_path = f"{output_folder_path}/{table_name}.json"
                os.makedirs(output_folder_path, exist_ok=True)
                os.makedirs(zip_folder_path, exist_ok=True)
                with open(local_file_path, 'w') as json_file:
                    json.dump(json_data, json_file, indent=4)

            zip_file_path = zip_folder(output_folder_path, zip_folder_path, "data.zip")

            presigned_response = one_integration_client.get_presign("data.zip", command_id)
            presigned_url = presigned_response['result']['payload']
            one_integration_client.upload_to_s3(presigned_url, zip_file_path)
            post_response = one_integration_client.post_command(presigned_url, command_id)
            print(f"{post_response['message']}")
        status = 'PROCESSED'
    except Exception as e:
        print(f"An error occurred: {e}")
        status = 'ERROR'
    finally:
        update_data(row_id,command,command_id,status)
        db_connector.close_connection()

