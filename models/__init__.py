#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


storage_type = os.getenv('HBNB_TYPE_STORAGE', 'db')

if storage_type.lower() == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
