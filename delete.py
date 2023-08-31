xgb_predictor.delete_endpoint(delete_endpoint_config=True)



bucket_to_delete = boto3.resource('s3').Bucket(bucket_name)
bucket_to_delete.objects.all().delete()