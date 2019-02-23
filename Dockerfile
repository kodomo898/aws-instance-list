FROM python:3.7

ARG project_dir=/app/

# ADD requirements.txt $project_dir
ADD aws $project_dir/aws
ADD aws-man.py $project_dir
ADD static $project_dir/static
ADD templates $project_dir/templates
WORKDIR $project_dir

RUN pip install flask boto3
# RUN pip install -r requirements.txt

CMD ["python", "aws-man.py"]
