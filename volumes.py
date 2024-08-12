import data
import db

def insert():
    packaged_volumes = data.fzz_inv_volumes()
    cursor = db.cursor()

    for type_id, type_data in data.sde_type_ids().items():
        volume = packaged_volumes.get(
            type_id,
            type_data.get('volume'),
        )
        if volume:
            cursor.insert_volume((
                type_id,
                volume,
            ))
    