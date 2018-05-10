Welcome to the Cube Me Program!
==============================================

This is a Python application deployed to AWS Lambda to be run as a serverless function, invoked by a RESTful endpoint 
exposed by API Gateway.  The deployment pipeline consists of an AWS Cloudformation template which deploys the application 
as well as the API Gateway and SNS Topic which can be used to send out SMS, and Email notifications.

It will take a curl command entry and return the cube of the number.

Deployment
-----------
Note: <<BUCKET_NAME>> needs to be the name of an S3 bucket in your account in the region (e.g. us-east-1) you plan on deploying the application to

In command line, type the following:

    aws cloudformation package --template-file template.yml --s3-bucket <<BUCKET_NAME>> --output-template-file template-export.yml

    aws cloudformation deploy --template-file template-export.yml --stack-name myapp --region us-east-1 --capabilities CAPABILITY_IAM

Once deployed, login to AWS and go to API Gateway, and grab the URL.  


Execution
-----------

Curl Command:

curl -XPOST 'https://r7ta5wdsrk.execute-api.us-west-1.amazonaws.com/Prod/' -d '{"number_to_cube":4}'



What's Here
-----------

This sample includes:

* README.md - this file
* index.py - this file contains the sample Python code for the web service
* template.yml - this file contains the Serverless Application Model (SAM) used
  by AWS Cloudformation to deploy your application to AWS Lambda and Amazon API
  Gateway.


What Do I Do Next?
------------------

If you have checked out a local copy of your repository you can start making changes
to the sample code.  We suggest making a small change to index.py first.

Learn more about Serverless Application Model (SAM) and how it works here:
https://github.com/awslabs/serverless-application-model/blob/master/HOWTO.md

AWS Lambda Developer Guide:
http://docs.aws.amazon.com/lambda/latest/dg/deploying-lambda-apps.html
