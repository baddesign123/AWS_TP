import boto3
import json
from botocore.exceptions import NoCredentialsError

class GestionSondage:
    def __init__(self):
        self.aws_access_key_id = 'AKIAWUBR7KZH34UZJA2F'
        self.aws_secret_access_key = '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'
        self.bucket_name = 'devoirpythonan'
        self.file_name_s3 = 'reponses_sondage.json'

    


