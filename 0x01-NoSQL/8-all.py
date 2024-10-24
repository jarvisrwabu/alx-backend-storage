#!/usr/bin/env python3
"""List all documents in Python."""


def list_all(mongo_collection):
    """
    List all documents in a collection.

    :param mongo_collection:
    :return:
    """
    documents = mongo_collection.find()
    return documents
