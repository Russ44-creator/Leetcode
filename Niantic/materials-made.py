'''
There are a few raw materials "wood", "soil", "metal", "rock".
Other advanced tools can be made from the raw materials. E.g. knife can be made from 2 
units of "wood" and 1 unit of "metal".
Now, given another advanced tool along with how it can be made (it can be made from some 
other advanced tools or raw material), return a list of raw material ne‍‌‍‍‍‌‌‍‌‌‍‌‍‍‌‍‌‍‍‍eded along with 
their quantity.
E.g, given a "blender" can be made from 2 knives and 1 rock, you should return 4*"Wood", 
2*"metal", 1*"rock".
'''

# toplogical sort
# df
# bfs
import collections

raw_materials = set(["wood", "soil", "metal", "rock"])
graph = {"knife": {"wood": 2, "metal": 1}, "aa": {"wood": 2}, "bb":{"wood": 2},
        "blender": {"wood":3, "knife": 2, "aa": 1, "rock": 1}}

counter = {"blender": 1}
in_degree = collections.defaultdict(lambda: 0)
for key, value in graph.items():
    for m in value:
        in_degree[m] += 1
    in_degree[key] += 0
print(in_degree)
dq = collections.deque()
for key, value in in_degree.items():
    if value == 0: dq.append(key)

while dq:
    material = dq.popleft() 
    if material in graph:
        for next_material, value in graph[material].items():
            in_degree[next_material] -= 1
            if in_degree[next_material] == 0:
                dq.append(next_material)  
            if material in counter:
                counter[next_material] = counter.get(next_material, 0) \
                    + counter[material] * value
        if material in counter:
            del counter[material] 
                # if next_material in counter:
                #     counter[next_material] += counter[]
    
print(counter)
