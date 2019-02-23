import sys
from flask import Flask
from flask import render_template
from aws import s3, ec2, rds

app = Flask(__name__)

@app.route('/')

def index():
    my_s3_name = []
    my_s3_date = []
    my_ec2_tags = []
    my_ec2_size = []
    my_ec2_state = []
    my_ec2_pip = []
    my_rds_name = []
    my_rds_size = []

    for bucket in s3.bucket().buckets.all():
        my_s3_name.append(bucket.name)
        my_s3_date.append(bucket.creation_date)

    instances = ec2.ec2_list().describe_instances()
    for resevations in instances['Reservations']:
        for instance in resevations['Instances']:
            my_ec2_state.append(instance['State']['Name'])
            my_ec2_size.append(instance['InstanceType'])
            for privateip in instance['NetworkInterfaces']:
                my_ec2_pip.append(privateip['PrivateIpAddress'])

            for tags in instance['Tags']:
                my_ec2_tags.append(tags['Value'])

    rdsinstances = rds.rds_list().describe_db_instances()
    for list_rds in rdsinstances['DBInstances']:
        my_rds_name.append(list_rds['DBInstanceIdentifier'])
        my_rds_size.append(list_rds['DBInstanceClass'])

    return render_template('index.html', bucket_info=zip(my_s3_name, my_s3_date), ec2_info=zip(my_ec2_tags, my_ec2_state, my_ec2_size, my_ec2_pip), rds_info=zip(my_rds_name, my_rds_size))

if __name__ == '__main__':
    app.run(debug=True)
