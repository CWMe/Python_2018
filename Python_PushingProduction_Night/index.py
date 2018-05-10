import json
import datetime
import os
import boto3


def handler(event, context):
    operation = event['httpMethod']

    # If the API Gateway submits a POST request
    if operation == 'POST':

        # Get the SNS_TOPIC_ARN environment variable inserted by the Cloudformation template
        topic = os.environ['SNS_TOPIC_ARN']

        # Create the boto3 SNS client
        client = boto3.client('sns')

        # Extract the number sent by the user
        body = json.loads(event['body'])

        return process(client, topic, body)
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))


def process(client, topic, body):
    # Python program to run a Cube Function
    number_to_cube = int(body['number_to_cube'])

    # check if the number is negative, positive or zero
    if number_to_cube < 0:
        return respond("Sorry, cube does not exist for negative numbers")
    elif number_to_cube == 0:
        return respond(None, create_response(0, 0))
    elif number_to_cube > 9000:
        return respond("Scouter says its over 9000. Too High")
    else:
        num_cubed = number_to_cube ** 3
        response = create_response(number_to_cube, num_cubed)
        message = response['output']
        publish(client, topic, message, 'You have successfully cubed a number')
        return respond(None, response)


def publish(client, topic, message, subject):
    # Publish a message to the SNS Topic
    client.publish(
        TargetArn=topic,
        Message=json.dumps({
            'default': json.dumps(message),
            'sms': message,
            'email': message
        }),
        MessageStructure='json',
        Subject=subject
    )


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {'Content-Type': 'application/json'}
    }


def create_response(number_to_cube, num_cubed):
    return {
        'output': 'The cube of ' + str(number_to_cube) + ' is ' + str(num_cubed),
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
