import data

_DOGMA_GROUPS = None

def dogma_groups() -> dict:
    global _DOGMA_GROUPS
    if _DOGMA_GROUPS is None:
        _DOGMA_GROUPS = get_groups()
    return _DOGMA_GROUPS

def get_groups():
	dogma_groups = {}
	dogma_categories = {}
	groups = {}

	cfg = data.cfg_dogma_groups()

	# cfg_dogma_groups = cfg.get('Groups, {}')
	cfg_dogma_groups = cfg['Groups']
	for group_str, group_ids in cfg_dogma_groups.items():
		for group_id in group_ids:
			dogma_groups.setdefault(group_id, [])\
				.append(group_str)

	# cfg_dogma_categories = cfg.get('Categories', {})
	cfg_dogma_categories = cfg['Categories']
	for category_str, category_ids in cfg_dogma_categories.items():
		for category_id in category_ids:
			dogma_categories.setdefault(category_id, [])\
				.append(category_str)

	sde_types = data.sde_type_ids()
	sde_groups = data.sde_group_ids()
	for type_id, type_data in sde_types.items():
		dogma_list = []
		group_id = type_data['groupID']
		dogma_list.extend(dogma_groups.get(group_id, []))
		category_id = sde_groups[group_id]['categoryID']
		dogma_list.extend(dogma_categories.get(category_id, []))
		if len(dogma_list) > 0:
			groups.update({type_id: dogma_list})

	# print(dogma_categories)

	return groups

def main():
	print(get_groups())

if __name__ == '__main__':
	main()
