from datetime import timedelta, datetime
import random
from typing import BinaryIO

import minio
from minio import Minio
from pydantic import BaseModel


class MinioHandler():
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if not MinioHandler.__instance:
            MinioHandler.__instance = MinioHandler()
        return MinioHandler.__instance

    def __init__(self):
        self.minio_url = 'localhost:9000'
        self.access_key = 'admin'
        self.secret_key = '12341234'
        self.bucket_name = 'orpheus'
        self.client = Minio(
            self.minio_url,
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=False,
        )
        self.make_bucket()

    def make_bucket(self) -> str:
        if not self.client.bucket_exists(self.bucket_name):
            self.client.make_bucket(self.bucket_name)
        return self.bucket_name

    def presigned_get_object(self, bucket_name, object_name):
        # Request URL expired after 7 days
        url = self.client.presigned_get_object(
            bucket_name=bucket_name,
            object_name=object_name,
            expires=timedelta(days=7)
        )
        return url

    def check_file_name_exists(self, bucket_name, file_name):
        try:
            self.client.stat_object(bucket_name=bucket_name, object_name=file_name)
            return True
        except Exception as e:
            print(f'[x] Exception: {e}')
            return False

    def put_object(self, file_data, file_name, content_type):
        try:
            datetime_prefix = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            object_name = f"{datetime_prefix}___{file_name}"
            while self.check_file_name_exists(bucket_name=self.bucket_name, file_name=object_name):
                random_prefix = random.randint(1, 1000)
                object_name = f"{datetime_prefix}___{random_prefix}___{file_name}"

            self.client.put_object(
                bucket_name=self.bucket_name,
                object_name=object_name,
                data=file_data,
                content_type=content_type,
                length=-1,
                part_size=10 * 1024 * 1024
            )
            url = self.presigned_get_object(bucket_name=self.bucket_name, object_name=object_name)
            data_file = {
                'bucket_name': self.bucket_name,
                'file_name': object_name,
                'url': url
            }
            return data_file
        except Exception as e:
            raise Exception(e)


class UploadFileResponse(BaseModel):
    bucket_name: str
    file_name: str
    url: str

class CustomException(Exception):
    http_code: int
    code: str
    message: str

    def __init__(self, http_code: int = None, code: str = None, message: str = None):
        self.http_code = http_code if http_code else 500
        self.code = code if code else str(self.http_code)
        self.message = message