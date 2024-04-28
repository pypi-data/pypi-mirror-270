import json
from datetime import datetime

from bson import ObjectId
from pymongo import DESCENDING

from komodo.core.tools.mongo.mongo_connect import get_mongo_client
from komodo.framework.komodo_tool import KomodoTool


class MongoDBQuery(KomodoTool):
    name = "MongoDB Query"
    purpose = "Executes a query on a specified collection in a MongoDB database."
    shortcode = "mongodb_query"

    definition = {
        "type": "function",
        "function": {
            "name": shortcode,
            "description": purpose,
            "parameters": {
                "type": "object",
                "properties": {
                    "database_name": {
                        "type": "string",
                        "description": "The name of the MongoDB database to query."
                    },
                    "collection_name": {
                        "type": "string",
                        "description": "The name of the collection within the database to query."
                    },
                    "query": {
                        "type": "string",
                        "description": "A JSON string representing the query to execute on the collection."
                    },
                    "sort_field": {
                        "type": "string",
                        "description": "The field to sort the results by. Defaults to 'createdDate'."
                    },
                    "sort_order": {
                        "type": "integer",
                        "description": "The order to sort the results by. Defaults to -1 (DESCENDING)."
                    },
                    "page": {
                        "type": "integer",
                        "description": "The page number to retrieve. Defaults to 1.",
                        "default": 1
                    },
                    "pageSize": {
                        "type": "integer",
                        "description": "The number of items per page. Defaults to 20.",
                        "default": 20
                    }
                },
                "required": ["database", "collection", "query"]
            },
            "returns": {
                "type": "string",
                "description": "The results of the query sorted by sort_field and sort_order."
            }
        }
    }

    def __init__(self, connection_string=None):
        super().__init__(shortcode=self.shortcode,
                         name=self.name,
                         definition=self.definition,
                         action=self.action)
        self.connection_string = connection_string

    def action(self, args, runtime):
        try:
            default_sort_field = runtime.config.get_value("mongo_sort_field", "created_at")
            default_sort_order = runtime.config.get_value("mongo_sort_order", DESCENDING)
            default_page_size = runtime.config.get_value("mongo_page_size", 20)

            client = get_mongo_client(self.connection_string)
            database_name = args["database_name"]
            collection_name = args["collection_name"]
            query_string = args["query"]
            page = args.get("page", 1)
            pageSize = args.get("pageSize", default_page_size)
            sort_field = args.get("sort_field", default_sort_field)
            sort_order = args.get("sort_order", default_sort_order)

            # Convert the query string to a dictionary
            query = json.loads(query_string)

            # Calculate the number of documents to skip
            skips = pageSize * (page - 1)

            db = client[database_name]
            collection = db[collection_name]

            results = list(collection.find(query).sort(sort_field, sort_order).skip(skips).limit(pageSize))
            client.close()

            # Custom JSON Encoder to handle ObjectId and datetime
            class CustomEncoder(json.JSONEncoder):
                def default(self, obj):
                    if isinstance(obj, ObjectId):
                        return str(obj)
                    if isinstance(obj, datetime):
                        return obj.isoformat()
                    return json.JSONEncoder.default(self, obj)

            return json.dumps(results, cls=CustomEncoder)

        except Exception as e:
            return "Error: Could not execute MongoDB query: " + str(e)
