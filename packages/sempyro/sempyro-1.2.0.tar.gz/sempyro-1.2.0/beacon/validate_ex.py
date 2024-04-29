import json

from individual import Individual
from pydantic import TypeAdapter, ValidationError, parse_obj_as

# file = "example.json"
#
#
# def parse_and_validate(file_path):
#
#     with open(file_path, "rb") as example:
#         try:
#             Individual.model_validate_json(example.read())
#         except ValidationError as e :
#             print(e)
#
#
# if __name__ == "__main__":
#     parse_and_validate(file)
from sempyro.dcat import DCATDataset
from sempyro.namespaces import GeoSPARQL

data = {
    "title": [{"value": "My dataset", "language": "en"}],
    "description": [{"value": "What my dataset is about", "language": "en"}],
    "spatial": [{"bounding_box": {"value": "POLYGON((-180 90,180 90,180 -90,-180 -90,-180 90))",
                                  "datatype": GeoSPARQL.wktLiteral}}]
}

DCATDataset.model_validate_json(json.dumps(data))
