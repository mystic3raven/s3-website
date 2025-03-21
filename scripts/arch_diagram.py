from diagrams import Diagram, Cluster
from diagrams.aws.network import CloudFront, VPC
from diagrams.aws.storage import S3
from diagrams.aws.security import IAM
from diagrams.aws.general import User
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import SNS
from diagrams.aws.management import Cloudwatch

# Create architecture diagram
with Diagram("AWS S3 Static Website with CloudFront", show=True, direction="LR"):
    user = User("Website Visitor")

    with Cluster("AWS Infrastructure"):
        vpc = VPC("VPC")
        s3 = S3("S3 Bucket\n(Static Website)")
        cloudfront = CloudFront("CloudFront CDN")
        iam = IAM("IAM Role & Policies")
        lambda_func = Lambda("Lambda Edge")
        sns = SNS("Notification for S3 Changes")
        cloudwatch = Cloudwatch("Monitoring")

        # Flow of data
        user >> cloudfront >> s3
        cloudfront >> lambda_func
        lambda_func >> iam
        s3 >> sns >> cloudwatch
        vpc >> s3

