from app.core.adapters.weaiate import Weaviate
from .dataloader import Data

import weaviate
import json

class Pipeline:
    def run(self):
        candidates = Data().load_json()
        for candidate in candidates:
            for id in candidate.items():
                print(id)
            break

client = weaviate.Client("http://216.153.51.169:8080/")
# weaviate = Weaviate()

# class_obj = {
#     "class": "Publication",
#     "description": "A description of this class, in this case, it is about publications",
#     "properties": [
#         {
#             "dataType": [
#                 "string"
#             ],
#             "description": "The name of the Publication",
#             "name": "name",
#         }
#     ]
# }

# # add the schema
# client.schema.create_class(class_obj)

# get the schema
schema = client.schema.get()

# print the schema
print(json.dumps(schema, indent=4))