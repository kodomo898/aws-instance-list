from aws import aws_session

def rds_list():
    rdslist = aws_session.aws_get().client('rds')
    return(rdslist)

