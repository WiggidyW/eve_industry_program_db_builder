from kind import Kind
import data
import db

from enum import Enum
import copy

class DogmaAttributeError(Exception):
    def __init__(self, type_id, attribute_id, reason):
        super().__init__(
            "Dogma Attribute Error for type_id: [{}]".format(type_id)\
                + ", attribute_id: [{}]".format(attribute_id)\
                + ", Reason: [{}]".format(reason),
        )

class EfficiencyKind(Enum):
    TIME_EFFICIENCY = 1
    MATERIAL_EFFICIENCY = 2
    COST_EFFICIENCY = 3
    HIGH_SEC_MULTIPLIER = 4
    LOW_SEC_MULTIPLIER = 5
    ZERO_SEC_MULTIPLIER = 6

    def efficiency_str(self):
        if self == EfficiencyKind.TIME_EFFICIENCY:
            return "time_efficiency"
        elif self == EfficiencyKind.MATERIAL_EFFICIENCY:
            return "material_efficiency"
        elif self == EfficiencyKind.COST_EFFICIENCY:
            return "cost_efficiency"
        elif self == EfficiencyKind.HIGH_SEC_MULTIPLIER:
            return "high_sec_multiplier"
        elif self == EfficiencyKind.LOW_SEC_MULTIPLIER:
            return "low_sec_multiplier"
        elif self == EfficiencyKind.ZERO_SEC_MULTIPLIER:
            return "zero_sec_multiplier"

    def is_security(self):
        if self in [
            EfficiencyKind.HIGH_SEC_MULTIPLIER,
            EfficiencyKind.LOW_SEC_MULTIPLIER,
            EfficiencyKind.ZERO_SEC_MULTIPLIER,
        ]:
            return True
        else:
            return False

class ValueKind(Enum):
    CORRECT = 1
    NEGATIVE_WHOLE_NUMBER = 2
    DIFFERENCE_FROM_1 = 3
    ANY_WHOLE_NUMBER = 4

class Efficiency:
    def __init__(
        self,
        type_id: int,
        # kind: Kind,
        material_efficiency: float,
        time_efficiency: float,
        cost_efficiency: float,
        probability_multiplier: float,
        zero_sec_multiplier: float,
        low_sec_multiplier: float,
        high_sec_multiplier: float,
    ):
        self.type_id = type_id
        # self.kind = kind
        self.time_efficiency = time_efficiency
        self.material_efficiency = material_efficiency
        self.cost_efficiency = cost_efficiency
        self.probability_multiplier = probability_multiplier
        self.high_sec_multiplier = high_sec_multiplier
        self.low_sec_multiplier = low_sec_multiplier
        self.zero_sec_multiplier = zero_sec_multiplier

    def set_parsed_field(self, key, value):
        if getattr(self, key) is None:
            setattr(self, key, value)
        else:
            if getattr(self, key) != value:
                raise DogmaAttributeError(
                    self.type_id,
                    None,
                    "Multiple attributes applying different values to the same field",
                )

    def set_field(self, key, value, value_kind):
        if value_kind == ValueKind.CORRECT:
            pass
        elif value_kind == ValueKind.DIFFERENCE_FROM_1:
            value = 1.0 - value
        elif value_kind == ValueKind.NEGATIVE_WHOLE_NUMBER\
            or value_kind == ValueKind.ANY_WHOLE_NUMBER\
        :
            value = abs(value) / 100.0
        self.set_parsed_field(key, round(value, 10))

    def mutate_from_dogma(self, cfg_attribute, dogma_attribute):
        self.set_field(
            EfficiencyKind(cfg_attribute['efficiency']).efficiency_str(),
            dogma_attribute['value'],
            ValueKind(cfg_attribute['value_kind']),
        )

    def set_skill_probability(self, probability):
        self.set_parsed_field(
            'probability_multiplier',
            probability,
        )

    def set_defaults(self):
        if self.time_efficiency is None:
            self.time_efficiency = 0.0
        if self.material_efficiency is None:
            self.material_efficiency = 0.0
        if self.cost_efficiency is None:
            self.cost_efficiency = 0.0
        if self.probability_multiplier is None:
            self.probability_multiplier = 0.0
        if self.high_sec_multiplier is None:
            self.high_sec_multiplier = 1.0
        if self.low_sec_multiplier is None:
            self.low_sec_multiplier = 1.0
        if self.zero_sec_multiplier is None:
            self.zero_sec_multiplier = 1.0

class ValidityKind(Enum):
    VALID = 1
    REQUIRED_SKILL = 2
    REQUIRED_GROUP = 3

def dogma_groups(type_dogma: dict):
    groups = set()
    for dogma_effect in type_dogma['dogmaEffects']:
        group = data\
            .cfg_dogma_effects()\
            .get(dogma_effect['effectID'])
        if group:
            groups.add(group)
    return groups

# returns the validity kind, potentially the groups, and the kinds
def new_efficiency(type_id: int, type_dogma: dict):
    kinds = {
        Kind.MANUFACTURING: False,
        Kind.INVENTION: False,
        Kind.COPY: False,
        Kind.REACTION: False,
    }
    efficiency = None
    validity_kind = None
    groups = None
    set_new_efficiency_by_security = False

    for dogma_attribute in type_dogma['dogmaAttributes']:
        cfg_attribute = data\
            .cfg_dogma_attributes()\
            .get(dogma_attribute['attributeID'])
        if cfg_attribute:
            efficiency_kind = EfficiencyKind(cfg_attribute['efficiency'])
            set_new_efficiency = False

            if efficiency is None:
                efficiency = Efficiency(
                    type_id,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                )
                set_new_efficiency = True
                if efficiency_kind.is_security():
                    set_new_efficiency_by_security = True

            for kind in Kind: # Hack Fix to problem of conflicting kinds
                if cfg_attribute.get(kind.to_str(), False):
                    kinds[kind] = True

            if set_new_efficiency_by_security\
                and not efficiency_kind.is_security()\
                or (set_new_efficiency
                and not set_new_efficiency_by_security)\
            :
                set_new_efficiency_by_security = False
                if cfg_attribute['check_dogma_group']:
                    validity_kind = ValidityKind.REQUIRED_GROUP
                    groups = dogma_groups(type_dogma)
                elif cfg_attribute['check_required_skill']:
                    validity_kind = ValidityKind.REQUIRED_SKILL
                else:
                    validity_kind = ValidityKind.VALID

            elif not efficiency_kind.is_security():
                if cfg_attribute['check_dogma_group']:
                    if validity_kind != ValidityKind.REQUIRED_GROUP:
                        raise DogmaAttributeError(
                            type_id,
                            dogma_attribute['attributeID'],
                            "Attributes with conflicting validities",
                        )
                elif cfg_attribute['check_required_skill']:
                    if validity_kind != ValidityKind.REQUIRED_SKILL:
                        raise DogmaAttributeError(
                            type_id,
                            dogma_attribute['attributeID'],
                            "Attributes with conflicting validities",
                        )
                elif validity_kind != ValidityKind.VALID:
                    raise DogmaAttributeError(
                        type_id,
                        dogma_attribute['attributeID'],
                        "Attributes with conflicting validities",
                    )
    
            efficiency.mutate_from_dogma(cfg_attribute, dogma_attribute)

    if validity_kind is None:
        efficiency = None # this protects us from situations where a type only has security attributes, in which case it's an invalid type for our purposes

    return (efficiency, validity_kind, kinds, groups)

class KindEfficiencies:
    def __init__(self):
        self.all_efficiencies = []

        # always valid for this kind
        self.valid_efficiencies = []

        # indexed by skill required for the activity
        self.skill_efficiencies = {}

        # indexed by group required for the activity
        self.group_efficiencies = {}

    def add_efficiency(
        self,
        efficiency: Efficiency,
        validity_kind: ValidityKind,
        groups,
    ):
        efficiency.set_defaults()
        self.all_efficiencies.append(efficiency)
        if validity_kind == ValidityKind.VALID:
            self.valid_efficiencies.append(efficiency)
        elif validity_kind == ValidityKind.REQUIRED_SKILL:
            self.skill_efficiencies\
                .setdefault(efficiency.type_id, [])\
                .append(efficiency)
        elif validity_kind == ValidityKind.REQUIRED_GROUP:
            if groups is None:
                # print(str(validity_kind))
                # print(efficiency)
                raise DogmaAttributeError(
                    efficiency.type_id,
                    0,
                    "RequiredGroup is set, but groups is None",
                )
            for group in groups:
                self.group_efficiencies\
                    .setdefault(group, [])\
                    .append(efficiency)

class Efficiencies:
    def __init__(self):
        self.inner = {
            Kind.MANUFACTURING: KindEfficiencies(), # manufacturing
            Kind.INVENTION: KindEfficiencies(), # invention
            Kind.COPY: KindEfficiencies(), # copy
            Kind.REACTION: KindEfficiencies(), # reaction
        }

    def __getitem__(self, kind) -> KindEfficiencies:
        return self.inner[kind]

    def try_add_efficiency(self, type_id, type_dogma):
        efficiency, validity_kind, kinds, groups = new_efficiency(
            type_id,
            type_dogma,
        )
        science_efficiency = None
        if efficiency is not None:
            for kind, b in kinds.items():
                if b:
                    if efficiency.material_efficiency is not None\
                        and efficiency.material_efficiency != 0.0\
                        and kind.is_science()\
                    :
                        if science_efficiency is None:
                            science_efficiency = copy.deepcopy(efficiency)
                            science_efficiency.material_efficiency = None
                        efficiency_to_add = science_efficiency
                        # print(efficiency.material_efficiency)
                        # print(science_efficiency.material_efficiency)
                    else:
                        efficiency_to_add = efficiency

                    self.inner[kind].add_efficiency(
                        efficiency_to_add,
                        validity_kind,
                        groups,
                    )

    def add_efficiency(self, efficiency, validity_kind, kinds, groups):
        for kind, b in kinds.items():
            if b:
                self.inner[kind].add_efficiency(
                    efficiency,
                    validity_kind,
                    groups,
                )

    def insert(self):
        cursor = db.cursor()
        for kind, kind_efficiencies in self.inner.items():
            for efficiency in kind_efficiencies.all_efficiencies:
                cursor.insert_efficiency((
                    efficiency.type_id,
                    kind.to_int(),
                    efficiency.time_efficiency,
                    efficiency.material_efficiency,
                    efficiency.cost_efficiency,
                    efficiency.probability_multiplier,
                    efficiency.high_sec_multiplier,
                    efficiency.low_sec_multiplier,
                    efficiency.zero_sec_multiplier,
                ))

EFFICIENCIES = Efficiencies()

def add_all_efficiencies():
    type_dogmas = data.sde_type_dogma()
    for type_id, type_dogma in type_dogmas.items():
        EFFICIENCIES.try_add_efficiency(type_id, type_dogma)

def insert():
    EFFICIENCIES.insert()

def main():
    add_all_efficiencies()
    # EFFICIENCIES.insert()

if __name__ == '__main__':
	main()
