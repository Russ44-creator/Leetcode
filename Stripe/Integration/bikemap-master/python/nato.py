#!/usr/bin/env python3

import json

# See ../1-json-primer.md for an explanation
json_text = '{"foo": {"bar": [{"nato": "oscar"}, {"nato": "papa"}, {"nato": "quebec"}]}}'
data = json.loads(json_text)

nato_letter = data["foo"]["bar"][1]["nato"]
print(nato_letter)  # "papa"

data["foo"]["quux"] = {"stuff": "nonsense", "nums": [2.718, 3.142]}

result = json.dumps(data, indent=4)
print(result)
