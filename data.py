import yml

SDE_SOLAR_SYSTEMS = None
SDE_TYPE_IDS = None
SDE_GROUP_IDS = None
SDE_TYPE_MATERIALS = None
SDE_BLUEPRINTS = None
SDE_TYPE_DOGMA = None

CFG_DOGMA_GROUPS = None
CFG_DOGMA_EFFECTS = None
CFG_DOGMA_ATTRIBUTES = None
CFG_KIND_MULTIPLIERS = None
CFG_PROBABILITY_SKILLS = None

FZZ_INV_VOLUMES = None

def sde_solar_systems() -> yml.SolarSystemStaticData:
    global SDE_SOLAR_SYSTEMS
    if SDE_SOLAR_SYSTEMS is None:
        SDE_SOLAR_SYSTEMS = yml.sde_solar_systems()
    return SDE_SOLAR_SYSTEMS

def sde_type_ids() -> dict:
    global SDE_TYPE_IDS
    if SDE_TYPE_IDS is None:
        SDE_TYPE_IDS = yml.sde_type_ids()
    return SDE_TYPE_IDS

def sde_group_ids() -> dict:
    global SDE_GROUP_IDS
    if SDE_GROUP_IDS is None:
        SDE_GROUP_IDS = yml.sde_group_ids()
    return SDE_GROUP_IDS

def sde_type_materials() -> dict:
    global SDE_TYPE_MATERIALS
    if SDE_TYPE_MATERIALS is None:
        SDE_TYPE_MATERIALS = yml.sde_type_materials()
    return SDE_TYPE_MATERIALS

def sde_blueprints() -> dict:
    global SDE_BLUEPRINTS
    if SDE_BLUEPRINTS is None:
        SDE_BLUEPRINTS = yml.sde_blueprints()
    return SDE_BLUEPRINTS

def sde_type_dogma() -> dict:
    global SDE_TYPE_DOGMA
    if SDE_TYPE_DOGMA is None:
        SDE_TYPE_DOGMA = yml.sde_type_dogma()
    return SDE_TYPE_DOGMA

def cfg_dogma_groups() -> dict:
    global CFG_DOGMA_GROUPS
    if CFG_DOGMA_GROUPS is None:
        CFG_DOGMA_GROUPS = yml.cfg_dogma_groups()
    return CFG_DOGMA_GROUPS

def cfg_dogma_effects() -> dict:
    global CFG_DOGMA_EFFECTS
    if CFG_DOGMA_EFFECTS is None:
        CFG_DOGMA_EFFECTS = yml.cfg_dogma_effects()
    return CFG_DOGMA_EFFECTS

def cfg_dogma_attributes() -> dict:
    global CFG_DOGMA_ATTRIBUTES
    if CFG_DOGMA_ATTRIBUTES is None:
        CFG_DOGMA_ATTRIBUTES = yml.cfg_dogma_attributes()
    return CFG_DOGMA_ATTRIBUTES

def cfg_kind_multipliers() -> dict:
    global CFG_KIND_MULTIPLIERS
    if CFG_KIND_MULTIPLIERS is None:
        CFG_KIND_MULTIPLIERS = yml.cfg_kind_multipliers()
    return CFG_KIND_MULTIPLIERS

def cfg_probability_skills() -> dict:
    global CFG_PROBABILITY_SKILLS
    if CFG_PROBABILITY_SKILLS is None:
        CFG_PROBABILITY_SKILLS = yml.cfg_probability_skills()
    return CFG_PROBABILITY_SKILLS

def fzz_inv_volumes() -> dict:
    global FZZ_INV_VOLUMES
    if FZZ_INV_VOLUMES is None:
        FZZ_INV_VOLUMES = yml.fzz_inv_volumes()
    return FZZ_INV_VOLUMES
