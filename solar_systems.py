import data
import db

def insert():
	cursor = db.cursor()
	sde_files = data.sde_solar_systems()
	for sde_file in sde_files:
		cursor.insert_system((
			sde_file['solarSystemID'],
			sde_file['security'],
		))

def main():
	insert()

if __name__ == '__main__':
	main()
