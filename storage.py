from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import uuid

credentials = GoogleCredentials.get_application_default()
service = discovery.build('storage', 'v1', credentials=credentials)
bucket = 'pictodocreader-bucket'


def store_file(filepath, file_extension):
    body = {'name': 'assets/{}.{}'.format(uuid.uuid1(), file_extension)}
    req = service.objects().insert(bucket=bucket, body=body, media_body=filepath)
    resp = req.execute()
