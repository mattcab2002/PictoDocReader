from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import uuid

credentials = GoogleCredentials.get_application_default()
service = discovery.build('storage', 'v1', credentials=credentials)

filename = 'images/img1.png'
bucket = 'pictodocreader-bucket'

body = {'name': 'assets/{}.png'.format(uuid.uuid1())}
req = service.objects().insert(bucket=bucket, body=body, media_body=filename)
resp = req.execute()
