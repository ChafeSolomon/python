# AWS SSM Association Lambda Function

This Lambda function creates AWS Systems Manager (SSM) associations for instances that are online. It targets instances whose IDs start with "mi" and applies a predefined set of Chef recipes.

## Prerequisites

- AWS Lambda
- AWS Systems Manager (SSM)
- IAM Role with appropriate permissions for SSM and Lambda execution

## Setup

1. **Create the Lambda Function:**
   - Go to the AWS Lambda Console.
   - Click "Create function".
   - Choose "Author from scratch".
   - Enter a name for your function.
   - Choose a runtime (e.g., Python 3.8).
   - Create or choose an existing execution role with the necessary permissions for SSM.

2. **Add the Code:**
   - Copy the content of `lambda_function.py` and paste it into the Lambda function code editor.


Give me a star!
Chafe Solomon
