import sys
import json
input_file = sys.argv[1]
with open(input_file, 'r') as f:
    s = json.load(f)
s_new = {}
for tags in s:
    s_new[tags] = []
    for rev in s[tags]:
        del rev["timestamp"]
        s_new[tags].append(rev)
print(json.dumps(s_new, indent=4))
