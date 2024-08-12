from pathlib import Path
import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

class SolarSystemStaticData:
    def __init__(self):
        self.paths = list(Path("sde/universe")\
            .rglob("solarsystem.yaml"))
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.paths):
            raise StopIteration
        f = open(self.paths[self.index])
        yml = yaml.load(f, Loader)
        f.close()
        self.index += 1
        return yml
    
def sde_solar_systems():
    return SolarSystemStaticData()

def sde_type_ids():
    with open('sde/fsd/types.yaml', 'r', encoding='utf8') as f:
        return yaml.load(f, Loader)

def sde_group_ids():
    with open('sde/fsd/groups.yaml', 'r', encoding='utf8') as f:
        return yaml.load(f, Loader)

def sde_type_materials():
    with open('sde/fsd/typeMaterials.yaml', 'r', encoding='utf8') as f:
        return yaml.load(f, Loader)

def sde_blueprints():
    with open('sde/fsd/blueprints.yaml', 'r') as f:
        return yaml.load(f, Loader)
    
def sde_type_dogma():
    with open('sde/fsd/typeDogma.yaml', 'r') as f:
        return yaml.load(f, Loader)

def cfg_dogma_attributes():
    with open('cfg/dogma_attributes.yml', 'r') as f:
        return yaml.load(f, Loader)

def cfg_dogma_effects():
    with open('cfg/dogma_effects.yml', 'r') as f:
        return yaml.load(f, Loader)

def cfg_probability_skills():
    with open('cfg/probability_skills.yml', 'r') as f:
        return yaml.load(f, Loader)

def cfg_kind_multipliers():
    with open('cfg/kind_multipliers.yml', 'r') as f:
        return yaml.load(f, Loader)

def cfg_dogma_groups():
    with open('cfg/dogma_groups.yml', 'r') as f:
        return yaml.load(f, Loader)
    
def fzz_inv_volumes():
    volumes = {}
    with open('fuzzworks/invVolumes.csv', 'r') as f:
        f.readline() # skip the header
        for line in f:
            line = line\
                .strip('\n')\
                .strip('\t')
            type_id, volume = line.split(',')
            volumes.update({
                int(type_id): float(volume),
            })
    return volumes
