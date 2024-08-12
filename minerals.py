from dedup_storage import DedupStorage


from enum import Enum

class MineralsKind(Enum):
    BLUEPRINT = 1
    INSTALLATION = 2
        
class Minerals(DedupStorage):
    def set_blueprint_minerals(
        self,
        blueprint_id,
        kind,
        minerals, # SDE blueprints materials
    ):
        blueprint_minerals = set()
        for mineral in minerals:
            blueprint_minerals.add((
                mineral['typeID'],
                mineral['quantity'],
            ))
        return self.update(
            frozenset(blueprint_minerals),
            (MineralsKind.BLUEPRINT,
            blueprint_id,
            kind),
        )
        
    def set_installation_minerals(
        self,
        product_id,
        minerals,
    ):
        installation_minerals = set()
        for mineral in minerals:
            installation_minerals.add((
                mineral['materialTypeID'],
                mineral['quantity'],
            ))
        return self.update(
            frozenset(installation_minerals),
            (MineralsKind.INSTALLATION,
            product_id),
        )
    
    def insert_one(self, cursor, key, entry):
        cursor.insert_mineral((
            key,
            entry[0],
            entry[1],
        ))

MINERALS = Minerals()

def insert():
    MINERALS.insert()
