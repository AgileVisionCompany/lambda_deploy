import argparse
import tempfile
import zipfile
import boto3
import os
from os.path import basename

from extractors import extract_metadata


def process(files):
    client = boto3.client('lambda')

    for file in files:
        metadata = extract_metadata(file)
        fd, temp_path = tempfile.mkstemp()
        os.close(fd)
        with open(temp_path, 'w') as temp_file:
            zip_archive = zipfile.ZipFile(temp_file, 'w')
            zip_archive.write(file, arcname=basename(file))
            zip_archive.close()

        with open(temp_path, 'rb') as temp_file:
            client.update_function_code(
                FunctionName=metadata['function_name'],
                ZipFile=temp_file.read(),
                Publish=True
            )

        os.remove(temp_path)


def main():
    parser = argparse.ArgumentParser(description="Deploy AWS Lambda Functions")

    parser.add_argument('file_names', metavar='file_name',
                        type=str, nargs='+',
                        help='files with lambda functions to process')

    args = parser.parse_args()
    process(args.file_names)


if __name__ == "__main__":
    main()
