from flask import Flask
from boto.s3.key import Key
import boto
import boto.s3.connection
import uuid


app = Flask(__name__)

@app.route("/")

def hello(data):
	try:
		connection = boto.connect_s3()
		bucket_name = "shashin-test"
		bucket = connection.get_bucket(bucket_name)
		key = Key(bucket)
		guid = uuid.uuid4()
		key.key = guid
		key.set_contents_from_string(data)
		key.make_public()
		print "Success"
	except Exception, exception:
		return exception

if __name__ == "__main__":
    app.run()
    