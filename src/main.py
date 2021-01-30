import boto3
import json
import uuid
import os


def say_hello() -> None:
    print('Hello askanna!')


if __name__ == "__main__":
    describe = {'some file': 'some string content'}
    policy = json.dumps(describe)
    s3 = boto3.client('s3')
    uuid_key = str(uuid.uuid4())
    _ = s3.put_object(Body=policy,
                      Bucket='voldemort-test',
                      Key='ask-anna-uploaded' + uuid_key)
    var_job = os.getenv("example")
    print(f'var job is = {var_job}')
