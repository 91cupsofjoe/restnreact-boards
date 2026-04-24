# Module for helper functions
from fastapi import HTTPException
from backend.database import database as db

# Check if created entry/entries are valid
def check_entries(entries, code: int, msg: str):
    if entries == None:
        raise HTTPException(
            status_code=code,
            detail=msg
        )
    return entries

# Create a new user, thread, or post
def create_new_entry(params, keys, response_schema,
                create_method, entry_type: str):
    with db.get_connection() as conn:
        entry = check_entries(
            create_method(
                conn,
                params
            ),
            500,
            f"Failed to create {entry_type}!"
        )

    return get_schema(
        entry,
        keys,
        response_schema
    )

# Fetch search results from the database
def get_search_results(query, params, keys, schema, entry_type: str,
                single_result = False):
    with db.get_connection() as conn:
        entries = check_entries(
            db.fetch_results(
                conn,
                query,
                params
            ),
            404,
            f"No matching {entry_type}!"
        )
        
    if single_result:
        return [get_schema(
            entries[0],
            keys,
            schema)]
    
    return get_schemas(
        entries,
        keys,
        schema)

# Return the a schema of the schema type
def get_schema(entry, keys, schema):
    return schema(**dict(zip(keys, entry)))

# Return a list of the schema type
def get_schemas(entries, keys, schema):
    return [
        schema(**dict(zip(keys, entry)))
        for entry in entries
    ]