from aws import aws_session

def bucket():
    s3list = aws_session.aws_get().resource('s3')
    return(s3list)
