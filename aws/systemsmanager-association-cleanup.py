import boto3
# Make sure you set this to run on a schedule. 

def lambda_handler(event, context):
    ssm_client = boto3.client('ssm')

    # Describe all associations
    paginator = ssm_client.get_paginator('list_associations')
    response_iterator = paginator.paginate()

    association_ids = []
    
    for page in response_iterator:
        for association in page['Associations']:
            association_ids.append(association['AssociationId'])

    # Delete each association
    for association_id in association_ids:
        try:
            ssm_client.delete_association(AssociationId=association_id)
            print(f"Deleted association {association_id}")
        except Exception as e:
            print(f"Error deleting association {association_id}: {str(e)}")
    
    return {
        'statusCode': 200,
        'body': 'Successfully deleted all associations'
    }
