# AWS Demo

A simple Demo app to connect to AWS S3 to upload and list files.

## Requirements

In order to run this app you will first need:

- An Amazon AWS account. A Identity and Access Management (IAM) user with Amazon S3 permission (e.g. AmazonS3FullAccess)
- An S3 bucket already created.
- Python 3 and the Flask framework

## Instructions

1. Ensure you create the following files for your AWS Credentials: `~/.aws/credentials` and `~/.aws/config`.
2. In your ~/.aws/credentials file you should have the following:

    ```ini
    [default]
    aws_access_key_id = YOUR_ACCESS_KEY
    aws_secret_access_key = YOUR_SECRET_KEY
    ```

3. You may also want to set a default region. This can be done in the configuration file. By default, its location is at `~/.aws/config`:

    ```ini
    [default]
    region=us-east-1
    ```

4. Create Python Virtual environment:

    ```bash
    python -m venv venv
    ```

5. Activate Python Virtual environment

    ```bash
    source venv/bin/activate
    ```

6. Install application requirements:

    ```bash
    pip install -r requirements.txt
    ```

7. Start application development server:

    ```bash
    python app.py
    ```

8. Browse to <http://localhost:8080>