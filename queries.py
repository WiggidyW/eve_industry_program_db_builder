CREATE_SYSTEMS = """
    CREATE TABLE systems (
        system_id INTEGER PRIMARY KEY NOT NULL,
        security REAL NOT NULL
    );
"""

CREATE_BLUEPRINTS = """
    CREATE TABLE blueprints (
        type_id INTEGER NOT NULL,
        kind INTEGER NOT NULL,
        duration INTEGER NOT NULL,
        products INTEGER NOT NULL,
        minerals INTEGER NOT NULL,
        rigs_skills_structures INTEGER NOT NULL,
        PRIMARY KEY (type_id, kind)
    );
"""

CREATE_EFFICIENCIES = """
    CREATE TABLE efficiencies (
        type_id INTEGER NOT NULL,
        kind INTEGER NOT NULL,
        time_efficiency REAL NOT NULL DEFAULT 0.0,
        material_efficiency REAL NOT NULL DEFAULT 0.0,
        cost_efficiency REAL NOT NULL DEFAULT 0.0,
        probability_multiplier REAL NOT NULL DEFAULT 0.0,
        high_sec_multiplier REAL NOT NULL DEFAULT 1.0,
        low_sec_multiplier REAL NOT NULL DEFAULT 1.0,
        zero_sec_multiplier REAL NOT NULL DEFAULT 1.0,
        PRIMARY KEY (type_id, kind)
    );
"""

CREATE_MINERALS = """
    CREATE TABLE minerals (
        id INTEGER NOT NULL,
        type_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        PRIMARY KEY (id, type_id)
    );
"""

CREATE_RIGS_SKILLS_STRUCTURES = """
    CREATE TABLE rigs_skills_structures (
        id INTEGER NOT NULL,
        type_id INTEGER NOT NULL,
        PRIMARY KEY (id, type_id)
    );
"""

CREATE_PRODUCTS = """
    CREATE TABLE products (
        id INTEGER NOT NULL,
        type_id INTEGER NOT NULL,
        portion INTEGER NOT NULL DEFAULT 1,
        probability REAL NOT NULL DEFAULT 1.0,
        installation_minerals INTEGER NOT NULL DEFAULT 0
    );
"""

CREATE_VOLUMES = """
    CREATE TABLE volumes (
        type_id INTEGER PRIMARY KEY NOT NULL,
        volume REAL NOT NULL DEFAULT 0.0
    );
"""

CREATE_NAMES = """
    CREATE TABLE type_names (
        type_id INTEGER PRIMARY KEY NOT NULL,
        name TEXT NOT NULL
    );
"""

INSERT_SYSTEM = """
    INSERT INTO systems (
        system_id,
        security
    )
    VALUES (?, ?);
"""

INSERT_BLUEPRINT = """
    INSERT INTO blueprints (
        type_id,
        kind,
        duration,
        products,
        minerals,
        rigs_skills_structures
    )
    VALUES (?, ?, ?, ?, ?, ?);
"""

INSERT_EFFICIENCY = """
    INSERT INTO efficiencies (
        type_id,
        kind,
        time_efficiency,
        material_efficiency,
        cost_efficiency,
        probability_multiplier,
        high_sec_multiplier,
        low_sec_multiplier,
        zero_sec_multiplier
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

INSERT_MINERAL = """
    INSERT INTO minerals (
        id,
        type_id,
        quantity
    )
    VALUES (?, ?, ?);
"""

INSERT_RIG_SKILL_STRUCTURE = """
    INSERT INTO rigs_skills_structures (
        id,
        type_id
    )
    VALUES (?, ?);
"""

INSERT_PRODUCT = """
    INSERT INTO products (
        id,
        type_id,
        portion,
        probability,
        installation_minerals
    )
    VALUES (?, ?, ?, ?, ?);
"""

INSERT_VOLUME = """
    INSERT INTO volumes (
        type_id,
        volume
    )
    VALUES (?, ?);
"""

INSERT_NAME = """
    INSERT INTO type_names (
        type_id,
        name
    )
    VALUES (?, ?);
"""
