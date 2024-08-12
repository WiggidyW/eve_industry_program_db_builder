from kind import Kind
from dedup_storage import DedupStorage
from minerals import MINERALS

class Products(DedupStorage):
    def set_blueprint_products(
        self,
        blueprint_id,
        kind: Kind,
        products, # blueprints.yaml, products
    ):
        blueprint_products = set()
        for product in products:
            product_id = product['typeID']
            blueprint_products.add((
                product_id,
                product['quantity'],
                product.get('probability', 1.0),
                MINERALS.set_installation_minerals(
                    product_id,
                    kind.installation_materials(product_id),
                ),
            ))
        return self.update(
            frozenset(blueprint_products),
            (kind,
            blueprint_id),
        )
    
    def insert_one(self, cursor, key, entry):
        cursor.insert_product((
            key,
            entry[0],
            entry[1],
            entry[2],
            entry[3],
        ))

PRODUCTS = Products()

def insert():
    PRODUCTS.insert()
