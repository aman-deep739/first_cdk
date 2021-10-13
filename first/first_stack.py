from aws_cdk import (
    aws_s3 as _s3,
    core
)

class FirstStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="myfirstcdkproject010203",
            versioned=True,
            encryption=_s3.BucketEncryption.KMS_MANAGED
        )
