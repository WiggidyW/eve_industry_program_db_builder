import db

class DedupStorage:
    def __init__(self):
        self.inner = {}
        self.index = 1
    
    def update(self, key, value):
        entry = self.inner.setdefault(key, {
            'id': self.index,
            'values': set(),
        })
        entry['values'].add(value)
        entry_id = entry['id']
        if entry_id == self.index:
            self.index += 1
        return entry_id
    
    def insert(self):
        cursor = db.cursor()
        for entries, key in self.inner.items():
            key = key['id']
            for entry in entries:
                self.insert_one(cursor, key, entry)

    def insert_one(self, _cursor, _key, _entry):
        raise NotImplementedError
