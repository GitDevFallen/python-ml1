import json
from google.cloud import aiplatform

aiplatform.init()

endpoint_id = '983354821371232256'

endpoint = aiplatform.Endpoint(endpoint_name=endpoint_id, location='europe-west3')

instances = [
     {"temp": 26.1, "max": 18.4, "min": 15.5, "wdsp": 5.6, "dewp": 11.5, "slp": 1007.2, "visib": 15.6},
]

predictions = endpoint.predict(instances=instances)

print(predictions)
