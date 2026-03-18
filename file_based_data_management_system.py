class SimpleDB:
    def __init__(self, filename):
        self.filename = filename

    def insert(self, record):
        with open(self.filename, "a") as f:
            f.write(str(record) + "\n")
        return "Record inserted"

    def fetch_all(self):
        data = []
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    data.append(eval(line.strip()))
        except FileNotFoundError:
            return []
        return data

    def find(self, key, value):
        results = []
        records = self.fetch_all()
        for record in records:
            if record.get(key) == value:
                results.append(record)
        return results

    def delete(self, key, value):
        records = self.fetch_all()
        new_records = [r for r in records if r.get(key) != value]

        with open(self.filename, "w") as f:
            for r in new_records:
                f.write(str(r) + "\n")

        return "Delete operation complete"


# Example
db = SimpleDB("data.txt")
db.insert({"id": 1, "name": "Ravi"})
db.insert({"id": 2, "name": "Amit"})
print(db.find("name", "Ravi"))