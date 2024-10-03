#!/usr/bin/env node

// See ../1-json-primer.md for an explanation
var json_text = '{"foo": {"bar": [{"nato": "oscar"}, {"nato": "papa"}, {"nato": "quebec"}]}}';
var data = JSON.parse(json_text);

var nato_letter = data["foo"]["bar"][1]["nato"];  // "papa"
var nato_letter2 = data.foo.bar[1].nato;  // JS dotted object syntax
console.log(nato_letter);

data["foo"]["quux"] = {"stuff": "nonsense", "nums": [2.718, 3.142]}

var result = JSON.stringify(data, null, 4);
console.log(result);
