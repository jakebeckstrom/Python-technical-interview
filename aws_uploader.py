import boto3

class DDB:

def __init__(self):
    ddb = boto3.resource("dynamodb")
    self.table = ddb.Table("employees")

def upload_employees(self, data):
    for item in data:
        self.table.put_item(Item=item)

def get_employees(self):
    self.table.query()