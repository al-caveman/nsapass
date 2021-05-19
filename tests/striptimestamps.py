import sys
import json
input_file = sys.argv[1]
with open(input_file, 'r') as f:
    db = json.load(f)
for tags in db:
    del db[tags]['timestamp']
print(json.dumps(db, indent=4))
