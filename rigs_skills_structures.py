from dedup_storage import DedupStorage
from efficiencies import EFFICIENCIES

class RigsSkillsStructures(DedupStorage):
    def set_blueprint_efficiencies(
        self,
        blueprint_id,
        kind,
        skills,
        groups, # iterable of dogma groups
    ):
        kind_efficiencies = EFFICIENCIES[kind]
        blueprint_rss = set()

        for valid_efficiency in kind_efficiencies.valid_efficiencies:
            blueprint_rss.add(valid_efficiency.type_id)

        for skill in skills:
            for kind_efficiency in kind_efficiencies\
                .skill_efficiencies\
                .get(skill['typeID'], []):
                blueprint_rss.add(kind_efficiency.type_id)

        for group in groups:
            for kind_efficiency in kind_efficiencies\
                .group_efficiencies\
                .get(group, []):
                blueprint_rss.add(kind_efficiency.type_id)

        return self.update(
            frozenset(blueprint_rss),
            (blueprint_id,
            kind),
        )
    
    def insert_one(self, cursor, key, entry):
        cursor.insert_rig_skill_structure((
            key,
            entry,
        ))
    
RIGS_SKILLS_STRUCTURES = RigsSkillsStructures()

def insert():
    RIGS_SKILLS_STRUCTURES.insert()
