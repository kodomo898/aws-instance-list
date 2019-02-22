from aws import aws_session

def ec2_list():
    ec2list = aws_session.aws_get().client('ec2')
    return(ec2list)
