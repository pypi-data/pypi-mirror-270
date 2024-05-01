import asyncio
import boto3
import hypersync
import polars as pl
import os
import time

from botocore.exceptions import NoCredentialsError
from hypersync import ColumnMapping, DataType, TransactionField, BlockField

# TODO 4/30/24 - Wait for KANT to give me credentials...
ACCESS_KEY = os.environ(['AWS_ACCESS_KEY'])
SECRET_KEY = os.environ(['AWS_SECRET_KEY'])
REGION = os.environ(['AWS_REGION'])


def upload_file_to_s3(file_name, bucket, object_name=None):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """
    if object_name is None:
        object_name = file_name

    # Create an S3 client
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                             aws_secret_access_key=SECRET_KEY,
                             region_name=REGION)

    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print('file uploaded successfully')
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    return True


async def collect_blocks_txs():
    """
    Uses the HypersyncClient to collect blocks and transactions from the Ethereum network. This data is stored in a parquet sink.
    """

    client = hypersync.HypersyncClient("https://eth.hypersync.xyz")

    to_block = await client.get_height()
    from_block = to_block - (7200 * 14) 
    batch_size = 10_000  # Define the number of blocks to process per batch

    while from_block < to_block:
        current_to_block = min(from_block + batch_size, to_block)
        print(
            f"Processing blocks {from_block} to {current_to_block}")

        query = client.preset_query_blocks_and_transactions(
            from_block, current_to_block)
        query.max_num_transactions = 1000  # for troubleshooting

        config = hypersync.ParquetConfig(
            path="data",
            hex_output=True,
            batch_size=5000,
            concurrency=10,
            retry=True,
            column_mapping=ColumnMapping(
                transaction={
                    TransactionField.GAS_USED: DataType.FLOAT64,
                    TransactionField.MAX_FEE_PER_BLOB_GAS: DataType.FLOAT64,
                    TransactionField.MAX_PRIORITY_FEE_PER_GAS: DataType.FLOAT64,
                    TransactionField.GAS_PRICE: DataType.FLOAT64,
                    TransactionField.CUMULATIVE_GAS_USED: DataType.FLOAT64,
                    TransactionField.EFFECTIVE_GAS_PRICE: DataType.FLOAT64,
                    TransactionField.NONCE: DataType.INT64,
                    TransactionField.GAS: DataType.FLOAT64,
                },
                block={
                    BlockField.GAS_LIMIT: DataType.FLOAT64,
                    BlockField.GAS_USED: DataType.FLOAT64,
                    BlockField.SIZE: DataType.FLOAT64,
                    BlockField.BLOB_GAS_USED: DataType.FLOAT64,
                    BlockField.EXCESS_BLOB_GAS: DataType.FLOAT64,
                    BlockField.BASE_FEE_PER_GAS: DataType.FLOAT64
                },
            )
        )

        await client.create_parquet_folder(query, config)
        from_block = current_to_block + 1  # Update from_block for the next batch



        # write the parquet file to s3 bucket
        directory = 'data/'
        file_name = 'blocks.parquet'
        bucket_name = 'ethanalytics'

        upload_file_to_s3(directory + file_name, bucket_name)
        # for filename in os.listdir(directory):
        #     if filename.endswith(".parquet"):
        #         file_path = os.path.join(directory, filename)
        #         upload_file_to_s3(file_path, bucket_name)


start_time = time.time()
asyncio.run(collect_blocks_txs())
end_time = time.time()

print(f"Time taken: {end_time - start_time}")
