import sqlite3
import queries

CONN = sqlite3.connect("output/db.sqlite")

class Cursor(sqlite3.Cursor):
	def create_tables(self):
		self.execute(queries.CREATE_SYSTEMS)
		self.execute(queries.CREATE_BLUEPRINTS)
		self.execute(queries.CREATE_EFFICIENCIES)
		self.execute(queries.CREATE_MINERALS)
		self.execute(queries.CREATE_RIGS_SKILLS_STRUCTURES)
		self.execute(queries.CREATE_PRODUCTS)
		self.execute(queries.CREATE_VOLUMES)
		self.execute(queries.CREATE_NAMES)

	def insert_system(self, v):
		self.execute(queries.INSERT_SYSTEM, v)

	def insert_blueprint(self, v):
		self.execute(queries.INSERT_BLUEPRINT, v)

	def insert_efficiency(self, v):
		self.execute(queries.INSERT_EFFICIENCY, v)

	def insert_mineral(self, v):
		self.execute(queries.INSERT_MINERAL, v)

	def insert_rig_skill_structure(self, v):
		self.execute(queries.INSERT_RIG_SKILL_STRUCTURE, v)

	def insert_product(self, v):
		self.execute(queries.INSERT_PRODUCT, v)

	def insert_volume(self, v):
		self.execute(queries.INSERT_VOLUME, v)

	def insert_name(self, v):
		self.execute(queries.INSERT_NAME, v)

def cursor() -> Cursor:
	return CONN.cursor(Cursor)

def commit():
	CONN.commit()

def create_table_validator():
	conn = sqlite3.connect("output/table_validator.sqlite")
	cursor = conn.cursor(Cursor)
	cursor.create_tables()
	conn.commit()
