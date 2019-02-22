import boto3
from boto3.session import Session

profile = 'uuum-porta'
region = 'ap-northeast-1'

def aws_get():
    session = Session(profile_name=profile, region_name=region)
    return(session)
