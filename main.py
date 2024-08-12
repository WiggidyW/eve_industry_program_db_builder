import efficiencies
import blueprints
import minerals
import products
import rigs_skills_structures
import solar_systems
import volumes
import db
import names

def main():
    cursor = db.cursor()
    cursor.create_tables()

    efficiencies.add_all_efficiencies()

    efficiencies.insert()
    blueprints.insert()
    minerals.insert()
    products.insert()
    rigs_skills_structures.insert()

    volumes.insert()

    solar_systems.insert()

    names.insert()

    db.commit()

if __name__ == '__main__':
    main()
