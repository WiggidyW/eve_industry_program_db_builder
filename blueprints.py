import data
import db
import groups
from kind import Kind
from minerals import MINERALS
from products import PRODUCTS
from rigs_skills_structures import RIGS_SKILLS_STRUCTURES

def insert():
    cursor = db.cursor()
    for blueprint_id, sde_data in data.sde_blueprints().items():
        copy_product = [{
             'quantity': 1,
             'typeID': blueprint_id,
        }]
        activity_data = sde_data['activities']
        for kind in Kind:
            activity = activity_data.get(kind.sde_blueprints_activity())
            if activity:
                if kind != Kind.COPY\
                    and ('products' not in activity\
                    or len(activity['products']) == 0)\
                :
                    continue
                duration = activity['time']
                minerals_id = MINERALS\
                    .set_blueprint_minerals(
                        blueprint_id,
                        kind,
                        activity.get('materials', []),
                )
                products = activity.get('products', copy_product)
                if len(products) == 0:
                    products = copy_product
                products_id = PRODUCTS\
                    .set_blueprint_products(
                        blueprint_id,
                        kind,
                        products,
                )
                rigs_skills_structures_id = RIGS_SKILLS_STRUCTURES\
                    .set_blueprint_efficiencies(
                        blueprint_id,
                        kind,
                        activity.get('skills', []),
                        groups.dogma_groups().get(products[0]['typeID'], []),
                )
                cursor.insert_blueprint((
                     blueprint_id,
                     kind.to_int(),
                     duration,
                     products_id,
                     minerals_id,
                     rigs_skills_structures_id,
                ))

def main():
	insert()

if __name__ == '__main__':
	main()
