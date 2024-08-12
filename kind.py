import data

from enum import Enum

class Kind(Enum):
    MANUFACTURING = 1
    INVENTION = 2
    COPY = 3
    REACTION = 4

    def installation_materials(self, product_id):
        if self == Kind.COPY or self == Kind.INVENTION:
            product_id = data\
                .sde_blueprints()\
                .get(product_id, {})\
                .get("activities", {})\
                .get(TO_SDE_BLUEPRINTS_ACTIVITY[Kind.MANUFACTURING], {})\
                .get('products', [{'typeID': 0}])\
                [0]\
                ['typeID']
        return data\
            .sde_type_materials()\
            .get(product_id, {'materials': []})\
            ['materials']

    def sde_blueprints_activity(self):
        return TO_SDE_BLUEPRINTS_ACTIVITY[self]
    
    def to_str(self):
        return TO_STR[self]
    
    def to_int(self):
        return TO_INT[self]
    
    def is_science(self):
        return self == Kind.COPY or self == Kind.INVENTION

TO_SDE_BLUEPRINTS_ACTIVITY = {
    Kind.MANUFACTURING: "manufacturing",
    Kind.INVENTION: "invention",
    Kind.COPY: "copying",
    Kind.REACTION: "reaction",
}

TO_STR = {
    Kind.MANUFACTURING: "manufacturing",
    Kind.INVENTION: "invention",
    Kind.COPY: "copy",
    Kind.REACTION: "reaction",
}

TO_INT = {
    Kind.MANUFACTURING: 1,
    Kind.INVENTION: 2,
    Kind.COPY: 3,
    Kind.REACTION: 4,
}
