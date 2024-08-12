import data
import db

def insert():
    cursor = db.cursor()
    for type_id, type_data in data.sde_type_ids().items():
        name = type_data.get('name', {}).get('en', f'{type_id}')
        cursor.insert_name((
            type_id,
            name,
        ))
