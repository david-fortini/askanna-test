import boto3
import json
import uuid


def say_hello() -> None:
    print('Hello askanna!')


if __name__ == "__main__":
    describe = {'some file': 'some string content'}
    policy = json.dumps(describe)
    s3 = boto3.client('s3')
    uuid_key = str(uuid.uuid4())
    s3.put_object(Body=policy,
                  Bucket='voldemort-test',
                  Key='ask-anna-uploaded' + uuid_key)
