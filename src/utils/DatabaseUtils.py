

from pymongo import MongoClient

def connect_to_database(mongo_uri):
    """
    Establishes a connection to a MongoDB database.

    Args:
        mongo_uri (str): The MongoDB connection URI.

    Returns:
        MongoClient: The MongoDB client instance.
    """
    client = MongoClient(mongo_uri)
    return client

def insert_data(client, database_name, collection_name, data):
    """
    Inserts data into a MongoDB collection.

    Args:
        client (MongoClient): The MongoDB client instance.
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.
        data (list): A list of dictionaries representing the documents to be inserted.

    Returns:
        InsertManyResult: The result of the insert operation.
    """
    db = client[database_name]
    collection = db[collection_name]
    result = collection.insert_many(data)
    return result

def query_data(client, database_name, collection_name, query=None):
    """
    Queries data from a MongoDB collection.

    Args:
        client (MongoClient): The MongoDB client instance.
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.
        query (dict, optional): The query filter. If not provided, returns all documents.

    Returns:
        list: A list of dictionaries representing the queried documents.
    """
    db = client[database_name]
    collection = db[collection_name]
    if query:
        documents = list(collection.find(query))
    else:
        documents = list(collection.find())
    return documents