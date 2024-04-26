import boto3

def choose_bucket(session: boto3.session.Session) -> str:
    """
    Lists available S3 buckets associated with the provided Boto3 session
    and allows the user to select one.

    Args:
        session: An active Boto3 session.

    Returns:
        str: The name of the selected bucket.
    """

    s3_client = session.client('s3')  # Create an S3 client using the session

    response = s3_client.list_buckets()

    if 'Buckets' in response:
        buckets = response['Buckets']
        if buckets:
            print("Available S3 buckets:")
            for i, bucket in enumerate(buckets):
                print(f"{i+1}. {bucket['Name']}")

            while True:
                try:
                    choice = int(input("Choose a bucket by number: "))
                    if 0 < choice <= len(buckets):
                        return buckets[choice - 1]['Name']
                    else:
                        print("Invalid selection. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            print("No S3 buckets found.")
    else:
        print("An error occurred while listing buckets.")

    return None  # Return None if no buckets are available or an error occurs
