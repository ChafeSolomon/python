import boto3

def lambda_handler(event, context):
    ssm_client = boto3.client('ssm')

    def create_association(laptop_instance):
        # Specify the required parameters based on your SSM document for chef
        SourceInfo = '{""}'
        SourceInfo2 = '{""}'
        SourceInfo3 = '{""}'
        targets = [{'Key': 'InstanceIds', 'Values': laptop_instance}]

        # Specify the association parameters
        parameters = {
            "ChefClientVersion": ['18'],
            "ChefClientArguments": [""],
            "ComplianceSeverity": ["None"],
            "ComplianceType": ["Custom:Chef"],
            "RunList": [""],
            "SourceInfo": [SourceInfo],
            "SourceInfo2": [SourceInfo2],
            "SourceInfo3": [SourceInfo3],
            "SourceType": ["S3"],
            "executionTimeout":['7200'],
            "WhyRun": ["False"]
        }

        # Create a Systems Manager client
        ssm_client = boto3.client('ssm')

        # Create the association
        try:
            response = ssm_client.create_association(
                AssociationName=laptop_instance[0],
                Name='Tresata-ApplyCincRecipes', 
                DocumentVersion='$DEFAULT',
                Targets=targets,
                OutputLocation={
                    'S3Location': {
                        'OutputS3Region': 'us-east-1',
                        'OutputS3BucketName': '',
                        'OutputS3KeyPrefix': 'history'
                    }
                },
                Parameters=parameters
            )
            print(response)
            return "Association created successfully:", response

        except Exception as e:
            return e

    try:
        response = ssm_client.describe_instance_information(
            Filters=[
                {
                    'Key': 'PingStatus',
                    'Values': ['Online']
                }
            ]
        )

        online_instances = [
            {'InstanceID': instance['InstanceId'], 'Status': instance['PingStatus']}
            for instance in response.get('InstanceInformationList', [])
        ]

        laptop_instances = [x['InstanceID'] for x in online_instances if x['InstanceID'].startswith('mi')]
        for laptop_instance in laptop_instances:
            laptop_instance = [laptop_instance]
            print(laptop_instance[0])
            result = create_association(laptop_instance)
            print(result)

    except Exception as e:
        print(e)
